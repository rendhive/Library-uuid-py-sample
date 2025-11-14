import uuid

with open('uuid_file.txt', 'r') as file:
    read_uuid = file.read()
print("UUID dibaca dari file:", read_uuid)
# Fungsi: Membaca UUID yang telah disimpan dari file.
# Kondisi: Ketika Anda perlu memuat kembali UUID yang sebelumnya disimpan.
