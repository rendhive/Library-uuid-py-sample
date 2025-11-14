import uuid

uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
print("UUID Versi 5:", uuid5)
# Fungsi: Membuat UUID berdasarkan hash SHA-1 dari namespace dan nama.
# Kondisi: Untuk menghasilkan UUID yang konsisten dengan hash SHA-1.
