import uuid

uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
print("UUID Versi 3:", uuid3)
# Fungsi: Membuat UUID berdasarkan hash MD5 dari namespace dan nama.
# Kondisi: Ketika Anda ingin menghasilkan UUID yang konsisten untuk input yang sama.
