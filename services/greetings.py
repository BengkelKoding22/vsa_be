# def generate_greeting(results):
#     greetings = []

#     # Looping setiap hasil deteksi wajah
#     for result in results:
#         name = result.get("name").split(" - ")[0]  # Mengambil nama tanpa ID
#         emotion = result.get("emotion")

#         # Menentukan sapaan berdasarkan emosi
#         if emotion == "happy":
#             greeting = f"halo {name}, sepertinya hari ini cerah sekali ya, semoga harimu menyenangkan"
#         elif emotion == "sad":
#             greeting = f"halo {name}, mengapa wajahmu terlihat sedih, senyum dong"
#         elif emotion == "angry":
#             greeting = f"halo {name}, mengapa wajahmu terlihat murung, senyum dong"
#         elif emotion == "surprise":
#             greeting = f"halo {name}, ada kabar apa hari ini"
#         else:
#             greeting = f"halo {name}"

#         # Menambahkan sapaan ke daftar
#         greetings.append(greeting)

#     # Menggabungkan semua sapaan menjadi satu teks
#     return " ".join(greetings)

def generate_greeting(results):
    greetings = []

    if results:
        name = results[0].get("name").split(" - ")[0]
        emotion = results[0].get("emotion")

        if emotion == "happy":
            greeting = f"halo {name}, sepertinya hari ini cerah sekali ya, semoga harimu selalu menyenangkan"
        elif emotion == "sad":
            greeting = f"halo {name}, mengapa wajahmu terlihat sedih, senyum dong"
        elif emotion == "angry":
            greeting = f"halo {name}, mengapa wajahmu terlihat murung, senyum dong"
        elif emotion == "surprise":
            greeting = f"halo {name}, ada kabar apa hari ini"
        else:
            greeting = f"halo {name}, saya bengbot, asisten pribadi anda. Ada yang bisa saya bantu?"

        greetings.append(greeting)

    return " ".join(greetings)
