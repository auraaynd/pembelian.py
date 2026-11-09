nama_barang = input("Masukkan nama barang: ")
jumlah = int(input("Masukkan jumlah beli: "))
harga_satuan = int(input("Masukkan harga satuan (Rp): "))

total_belanja = jumlah * harga_satuan
dapat_diskon = total_belanja >= 200000

print("Barang:", nama_barang)
print("Total Belanja: Rp", total_belanja)
print("Dapat Diskon:", dapat_diskon)