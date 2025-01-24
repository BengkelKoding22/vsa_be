# ELEVEN LABS RESPONSE TIME = 1.6339738368988037 s
# EDGE TTS RESPONSE TIME = 0.6185522079467773 s
# GOOGLE TTS RESPONSE TIME = 0.28463220596313477 s

from fastapi import FastAPI, HTTPException, UploadFile, File, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import TextRequest, ApiResponse
from services.text_generation import generate_text_response
from services.face_recognition import detect_faces
from utils.helpers import create_response, audio_to_base64
from services.voice_elevenlabs import generate_speech as elevenlabs_generate_speech
from services.greetings import generate_greeting
from services.tts_edge import run_edge_tts
from services.tts_google import gtts_text_to_speech
from services.gemini_service import GeminiService

import re
import os
import time
import logging
import datetime

router = APIRouter()

@router.post("/generate-audio/eleven-labs", response_model=ApiResponse)
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
        response_text, link = GeminiService.generate_text_response(input_text)
        clean_text = re.sub(r'\n', '', response_text)

      
        # ElevenLabs TTS: Start time
        start_time_elevenlabs = time.time()
        audio_elevenlabs = elevenlabs_generate_speech(clean_text)
        end_time_elevenlabs = time.time()
        elevenlabs_tts_time = end_time_elevenlabs - start_time_elevenlabs


        audio_base64 = audio_to_base64(audio_elevenlabs)
        os.remove(audio_elevenlabs)

        if link:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={
                    "response": clean_text,
                    "link": link,
                    "audio": audio_base64,
                    "response_timess": elevenlabs_tts_time,
                }
            )
        else:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={
                    "response": clean_text,
                    "audio": audio_base64,
                    "response_timess": elevenlabs_tts_time,
                }
            )
    except Exception as e:
        return create_response(
            status="error",
            code=500,
            message=str(e),
            data={}
        )



@router.post("/generate-audio/edget-tts", response_model=ApiResponse)
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
        response_text, link = GeminiService.generate_text_response(input_text)
        clean_text = re.sub(r'\n', '', response_text)

        # Edge TTS: Start time
        start_time_edge = time.time()
        audio_edge = await run_edge_tts(clean_text, "audio")
        end_time_edge = time.time()
        edge_tts_time = end_time_edge - start_time_edge

        # Select the audio you want to return, in this case just as an example:
        audio_base64 = audio_to_base64(audio_edge)
        os.remove(audio_edge)

        if link:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={
                    "response": clean_text,
                    "link": link,
                    "audio": audio_base64,
                    "response_times": edge_tts_time,
                }
            )
        else:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={
                    "response": clean_text,
                    "audio": audio_base64,
                    "response_times": edge_tts_time,
                }
            )
    except Exception as e:
        return create_response(
            status="error",
            code=500,
            message=str(e),
            data={}
        )


@router.post("/generate-audio/google-tts", response_model=ApiResponse)
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
        response_text, link = GeminiService.generate_text_response(input_text)
        clean_text = re.sub(r'\n', '', response_text)

        start_time_google = time.time()
        audio_google = gtts_text_to_speech(clean_text)
        end_time_google = time.time()
        google_tts_time = end_time_google - start_time_google

        audio_base64 = audio_to_base64(audio_google)
        os.remove(audio_google)

        if link:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={
                    "response": clean_text,
                    "link": link,
                    "audio": audio_base64,
                    "response_times": google_tts_time,
                }
            )
        else:
            return create_response(
                status="success",
                code=200,
                message="Request successful",
                data={
                    "response": clean_text,
                    "audio": audio_base64,
                    "response_times": google_tts_time,
                }
            )
    except Exception as e:
        return create_response(
            status="error",
            code=500,
            message=str(e),
            data={}
        )

