from gtts import gTTS
from datetime import datetime

def gtts_text_to_speech(text):
    # Tentukan bahasa Indonesia
    language = "id"
    
    # Menentukan nama file berdasarkan waktu
    output_file = f"gtts_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    
    # Membuat audio dan menyimpannya
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    
    print(f"Audio telah disimpan di: {output_file}")
    return output_file

