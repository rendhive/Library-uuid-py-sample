import uuid

def check_uuid_valid(uuid_string):
    try:
        val = uuid.UUID(uuid_string, version=4)
        return val
    except ValueError:
        return "Invalid UUID"

print("Cek UUID Valid:", check_uuid_valid("550e8400-e29b-41d4-a716-446655440000"))
# Fungsi: Memeriksa apakah UUID yang dimasukkan adalah valid.
# Kondisi: Saat Anda ingin memastikan format atau kevalidan UUID.
