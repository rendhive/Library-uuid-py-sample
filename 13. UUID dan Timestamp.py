import uuid
import time

def uuid_with_timestamp():
    unique_id = uuid.uuid1()
    print(f"UUID: {unique_id} | Timestamp: {unique_id.time}")

uuid_with_timestamp()
# Fungsi: Menghasilkan UUID berdasarkan waktu dan mencetak timestamp.
# Kondisi: Ketika Anda perlu analisis waktu yang terkait dengan UUID.
