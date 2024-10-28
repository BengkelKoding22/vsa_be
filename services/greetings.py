def generate_greeting(results):
    greetings = []

    # Looping setiap hasil deteksi wajah
    for result in results:
        name = result.get("name").split(" - ")[0]  # Mengambil nama tanpa ID
        emotion = result.get("emotion")

        # Menentukan sapaan berdasarkan emosi
        if emotion == "happy":
            greeting = f"halo {name}, sepertinya hari ini wajahmu bahagia"
        elif emotion == "sad":
            greeting = f"halo {name}, mengapa wajahmu terlihat sedih, senyum dong"
        else:
            greeting = f"halo {name}"

        # Menambahkan sapaan ke daftar
        greetings.append(greeting)

    # Menggabungkan semua sapaan menjadi satu teks
    return " ".join(greetings)
