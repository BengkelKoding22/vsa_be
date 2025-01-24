from loguru import logger
import os

def configure_logger():
    if not os.path.exists("log"):
        os.makedirs("log")

    logger.remove()

    logger.add(
        "log/app.log",  # Menyimpan log di folder 'log'
        rotation="1 week",  # Rotasi log setiap minggu
        retention="2 weeks",  # Simpan log selama 2 minggu
        compression="zip",  # Kompres log lama menjadi ZIP
        format=(
            "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name}:{function}:{line} | {message}"
        ),  # Format log
        backtrace=True,  # Tampilkan stack trace lengkap
        diagnose=True,  # Tampilkan detail debugging untuk error
    )

# Konfigurasi logger
configure_logger()

# Log pesan informasi
logger.info("Logger telah dikonfigurasi dengan benar.")
