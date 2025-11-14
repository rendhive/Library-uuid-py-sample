import uuid

def generate_transaction_id():
    return str(uuid.uuid4())

print("Transaction ID:", generate_transaction_id())
# Fungsi: Menghasilkan ID transaksi unik.
# Kondisi: Ketika Anda perlu memberikan ID unik untuk transaksi atau operasi penting lainnya.
