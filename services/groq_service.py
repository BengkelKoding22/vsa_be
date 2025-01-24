import os
from core.config import settings
from loguru import logger
from groq import Groq


class GROQService: 
    @staticmethod
    def generate_chat(input : str) -> str:
        client = Groq(
            api_key=os.environ.get(settings.GROQ_API_KEY),
        )


        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role" : "system",
                    "content" : """
                    Halo, disini aku akan memberikan mu sebuah identitas untuk deployment mu.
                    Namamu: BengBot
                    Pembuat: Bengkel Koding
                    Dibuat pada: Oktober 2024
                    Tugas: Asisten Pribadi (Akademik) dan Teman yang Ramah dan Menyenangkan
                    Catatan Penting: Maksimal Jawaban 15 Kata

                    Jawablah segala pertanyaan yang diajukan oleh pengguna dengan ramah dan jelas seperti teman .

                    Jangan menjawab dengan emotikon dan lebih dari 15 kata. Jawablah dengan bahasa manusia yang ramah dan menyenangkan.
                    """
                },  
                {
                    "role": "user",
                    "content": "input",
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content
   
