import google.generativeai as genai
# from config import API_KEY, GENERATION_CONFIG, DEFAULT_TEXT
from core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

class GeminiService:
    @staticmethod
    def generate_text_response(input_text: str) -> str:
        keywords = ["reservasi", "pinjam", "peminjaman", "pinjam ruangan", "meminjam", "pinjam ruangan", "peminjaman ruangan", "reservasi ruangan"]

        if any(keyword in input_text.lower() for keyword in keywords):
            return "Jika anda ingin memesan atau melakukan reservasi silahkan mengunjungi link berikut: https://bengkelkoding.com", "https://bengkelkoding.com"        


        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": [
                """
                    Halo, disini aku akan memberikan mu sebuah identitas untuk deployment mu.
                    Namamu: BengBot
                    Pembuat: Bengkel Koding
                    Dibuat pada: Oktober 2024
                    Tugas: Asisten Pribadi (Akademik) dan Teman yang Ramah dan Menyenangkan
                    Catatan Penting: Maksimal Jawaban 15 Kata

                    Jawablah segala pertanyaan yang diajukan oleh pengguna dengan ramah dan jelas seperti teman .

                    Jangan menjawab dengan emotikon dan lebih dari 15 kata. Jawablah dengan bahasa manusia yang ramah dan menyenangkan.
                """
                ]},
                {"role": "user", "parts": [input_text]},
            ]
        )
        response = chat.send_message(input_text, generation_config={
            "candidate_count": 1,
            "max_output_tokens": 100,
            "temperature": 1.0
        })
        return response.text, None

