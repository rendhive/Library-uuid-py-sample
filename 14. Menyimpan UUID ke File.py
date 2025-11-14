import uuid

with open('uuid_file.txt', 'w') as file:
    file.write(str(uuid.uuid4()))
print("UUID telah disimpan ke 'uuid_file.txt'.")
# Fungsi: Menyimpan UUID ke file untuk referensi di masa mendatang.
# Kondisi: Ketika Anda ingin menyimpan UUID untuk penggunaan selanjutnya.
