import edge_tts
import asyncio

# Fungsi untuk melakukan TTS dalam bahasa Indonesia
async def text_to_speech(text, output_file='output.mp3'):
    # Atur suara yang diinginkan (contoh: ArdiNeural untuk Bahasa Indonesia)
    voice = "id-ID-GadisNeural"  # Anda bisa mencoba "id-ID-AndikaNeural" juga
    
    # Konfigurasikan edge-tts dan buat output audio
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    
    print(f"Audio telah disimpan di: {output_file}")
    return output_file

# Fungsi untuk menjalankan text_to_speech dan mengembalikan nama file
async def run_edge_tts(text, output_file='output.mp3'):
    return await text_to_speech(text, output_file)