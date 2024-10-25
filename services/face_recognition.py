import numpy as np
import cv2
import torch
from ultralytics import YOLO
from fastapi import UploadFile
from utils.helpers import extract_embedding, match_face
from .emotion_detection import predict_emotion, class_to_emotion

# Memuat model YOLO untuk mendeteksi wajah
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('model_weights/yolov8n-face.pt').to(device)

async def detect_faces(file: UploadFile) -> list:
    try:
        # Membaca file yang diupload sebagai byte
        contents = await file.read()
        
        # Mengonversi byte menjadi array numpy
        image = np.frombuffer(contents, np.uint8)
        
        # Mengonversi array numpy menjadi gambar menggunakan OpenCV
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

        if frame is None:
            raise ValueError("Error: Gambar tidak dapat di-decode, periksa format gambar")

        # Melakukan deteksi wajah menggunakan model YOLO
        results = model(frame)
        detections = []

        # Loop untuk mengambil setiap deteksi dari hasil YOLO
        for result in results:
            for box in result.boxes.xyxy:  # Mengakses bounding boxes
                # Crop wajah dari gambar berdasarkan bounding box
                cropped_face = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                
                # Mengambil embedding untuk wajah yang dipotong
                embedding = extract_embedding(cropped_face)
                
                # Mencocokkan embedding dengan database wajah
                name, similarity = match_face(embedding)
                
                # Memprediksi emosi dari wajah yang dipotong
                predicted_emotion = predict_emotion(cropped_face)
                emotion_text = class_to_emotion(predicted_emotion)

                # Menambahkan hasil deteksi ke dalam daftar
                detections.append({
                    "bounding_box": box.tolist(),  # Mengubah box ke dalam format list
                    "name": name,
                    "similarity": similarity,
                    "emotion": emotion_text,
                })

        # Mengembalikan hasil deteksi dalam bentuk list
        return detections

    except Exception as e:
        # Jika terjadi kesalahan, log error dan naikkan exception
        print(f"Error dalam proses deteksi wajah: {e}")
        raise e
