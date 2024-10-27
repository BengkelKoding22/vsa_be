from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import TextRequest,ApiResponse  
from services.text_generation import generate_text_response
from services.face_recognition import detect_faces
from utils.helpers import create_response, audio_to_base64
from services.voice_elevenlabs import generate_speech
import re
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate",response_model=ApiResponse)
async def generate_text(request: TextRequest):
    input_text = request.text
    if not input_text:
        intro = audio_to_base64("audio/introduction.mp3")
        return create_response(
            status="success",
            code=200,
            message="Request successful",
            data={
                "response" : "Hey dear... How was your day?",
                "audio" :  intro
            }
        )

    try:
        response_text, link = generate_text_response(input_text)
        clean_text = re.sub(r'[^\w\s]', '', response_text)
        clean_text = re.sub(r'\n', '', clean_text)
        audio = generate_speech(clean_text)
        audio_base64 = audio_to_base64(audio)
        os.remove(audio)
        if link:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={"response" : clean_text , "link" : link, "audio" :audio_base64}
            )
        else:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={"response" : clean_text, "audio" : audio_base64}
            )   
    except Exception as e:
        return create_response(
            status="error",
            code=500,
            message=str(e),
            data={}
        )

@app.get("/exit")
async def exit_chat():
    return {"message": "Chatbot telah dihentikan."}

@app.post("/detect/", response_model=ApiResponse)
async def detect_face(file: UploadFile = File(...)):
    try:
        if not file:
            raise ValueError("No file uploaded")

        result = await detect_faces(file)

        return create_response(
            status="success",
            code=200,
            message="Face detection successful",
            data={"results": result}
        )
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return create_response(
            status="error",
            code=400,
            message=str(ve),
            data={}
        )
    except Exception as e:
        logging.error(f"Unexpected error during face detection: {e}")
        return create_response(
            status="error",
            code=500,
            message="Error in face detection",
            data={}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# const voiceId = "8EkOjt4xTPGMclNlh1pk"; // Replace with the desired voice ID
#   const voiceSettings = {
#     stability: 0.8,
#     similarity_boost: 0.6,
#     style: 0.4,
#   };