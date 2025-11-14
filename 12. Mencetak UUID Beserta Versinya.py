import uuid

def print_uuid_with_version():
    unique_id = uuid.uuid4()
    print(f"UUID: {unique_id} | Version: {unique_id.version}")

print_uuid_with_version()
# Fungsi: Mencetak UUID dan versinya.
# Kondisi: Ketika Anda perlu informasi lebih lanjut tentang UUID yang dibuat.
