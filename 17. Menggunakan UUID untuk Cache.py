import uuid

cache = {}

def cache_data(data):
    cache_key = str(uuid.uuid4())
    cache[cache_key] = data
    print(f"Data cached with key: {cache_key}")

cache_data("some valuable data")
# Fungsi: Menggunakan UUID sebagai kunci untuk menyimpan data dalam cache.
# Kondisi: Ketika Anda perlu menyimpan data sementara dan mendemonstrasikan ID unik untuk mengaksesnya.
