from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
import cv2
import numpy as np
import pickle
import onnxruntime
from ultralytics import YOLO
from scipy.spatial.distance import cosine
from PIL import Image
import torch

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mengambil API Key dari environment
api_key = os.getenv("API_KEY")

if not api_key:
    raise Exception("API Key tidak ditemukan. Pastikan API Key sudah ada di .env")
else:
    genai.configure(api_key=api_key)

# Konfigurasi pengaturan generasi teks
generation_config = genai.types.GenerationConfig(
    candidate_count=1,
    max_output_tokens=500,
    temperature=1.0
)

# Teks default untuk history percakapan
default_text = """
        Halo, disini aku akan memberikan mu sebuah identitas untuk deployment mu.
        Namamu: BengBot
        Pembuat: Bengkel Koding
        Dibuat pada: Oktober 2024
        Tugas: Asisten Pribadi (Akademik)
"""

# Inisialisasi FastAPI
app = FastAPI()

# Menambahkan middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model data untuk permintaan
class TextRequest(BaseModel):
    text: str

# Load YOLOv8-face model and move to GPU if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('yolov8n-face.pt').to(device)

# Load FaceNet ONNX model for face recognition
facenet_session = onnxruntime.InferenceSession('facenet_model.onnx')

# Load Emotion Detection ONNX model
emotion_session = onnxruntime.InferenceSession('emotion.onnx')

# Load the saved embeddings from the .pkl file
with open('embeddings.pkl', 'rb') as f:
    embeddings_db = pickle.load(f)

# Fungsi untuk praproses wajah
def preprocess_face(face_image):
    img = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
    img = img.resize((160, 160))
    img = np.array(img).astype(np.float32)
    img = (img - 127.5) / 128.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img

def extract_embedding(face_image):
    preprocessed_face = preprocess_face(face_image)
    embedding = facenet_session.run(None, {'input': preprocessed_face})[0].flatten()
    return embedding

def match_face(embedding, threshold=0.6):
    min_distance = float('inf')
    best_match = "Unknown"
    best_similarity = 0.0

    for person_name, saved_embedding in embeddings_db.items():
        distance = cosine(embedding, saved_embedding)
        similarity = 1 - distance

        if distance < min_distance and distance < threshold:
            min_distance = distance
            best_match = person_name
            best_similarity = float(similarity)

    return best_match, best_similarity

def preprocess_emotion_image(face_image):
    img = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (48, 48))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    return img

def predict_emotion(face_image):
    preprocessed_img = preprocess_emotion_image(face_image)
    input_name = emotion_session.get_inputs()[0].name
    output_name = emotion_session.get_outputs()[0].name
    result = emotion_session.run([output_name], {input_name: preprocessed_img.astype(np.float32)})
    predicted_class = np.argmax(result[0])
    return predicted_class

def class_to_emotion(predicted_emotion):
    res_dict = {0: 'angry', 1: 'disgusted', 2: 'fearful', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprised'}
    return res_dict.get(predicted_emotion, "Unknown")

@app.post("/generate")
async def generate_text(request: TextRequest):
    input_text = request.text

    if not input_text:
        raise HTTPException(status_code=400, detail="Teks tidak ditemukan pada body request.")

    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": [default_text]},
            {"role": "user", "parts": [input_text]},
        ]
    )

    response = chat.send_message(input_text, generation_config=generation_config)

    return {"response": response.text}

@app.get("/exit")
async def exit_chat():
    return {"message": "Chatbot telah dihentikan."}

@app.post("/detect/")
async def detect_face(file: UploadFile = File(...)):
    contents = await file.read()
    image = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

    results = model(frame)
    detections = []

    for result in results:
        for box in result.boxes.xyxy:
            cropped_face = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            embedding = extract_embedding(cropped_face)
            name, similarity = match_face(embedding)
            predicted_emotion = predict_emotion(cropped_face)
            emotion_text = class_to_emotion(predicted_emotion)

            detections.append({
                "bounding_box": box.tolist(),
                "name": name,
                "similarity": similarity,
                "emotion": emotion_text,
            })

    return {"results": detections}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
