import uuid

def generate_uuid_grid(n):
    return [uuid.uuid4() for _ in range(n)]

print("Grid UUID:", generate_uuid_grid(5))
# Fungsi: Menghasilkan daftar UUID.
# Kondisi: Ketika Anda perlu membuat banyak UUID sekaligus.
