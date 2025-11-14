import uuid

def create_user_uuid(username):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, username))

print("UUID untuk Pengguna:", create_user_uuid("user123"))
# Fungsi: Membuat UUID berdasarkan nama pengguna.
# Kondisi: Ketika Anda perlu menjaga UUID konsisten untuk pengguna berdasarkan nama.
