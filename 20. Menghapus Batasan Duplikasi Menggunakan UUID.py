import uuid

data_set = set()

for _ in range(10):
    data_set.add(str(uuid.uuid4()))

print("UUID Unik tanpa Duplikasi:", data_set)
# Fungsi: Menghasilkan sekumpulan UUID yang unik.
# Kondisi: Saat Anda ingin memastikan tidak ada ID yang duplikat.
