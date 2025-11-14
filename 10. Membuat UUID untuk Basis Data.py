import uuid

def generate_db_uuid():
    return str(uuid.uuid4())

print("UUID untuk Basis Data:", generate_db_uuid())
# Fungsi: Menghasilkan UUID untuk digunakan sebagai ID dalam Basis Data.
# Kondisi: Saat Anda ingin memberikan ID unik untuk entitas di basis data.
