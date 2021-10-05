"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""


# Sekuensial
# print('Ibu berkata, "Pergi ke toko"')
# print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
# print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
# print("Maka Budi berangkat ke toko")
# print("Dan mulai berbelanja")

# Percabangan
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu, dan jika ada telor beli 6 telor"\n')

jumlah_botol_susu = 10
jumlah_telur = 6
print(f"Jumlah botol susu {jumlah_telur} botol")
print(f"Jumlah telur {jumlah_telur} butir\n")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Budi membeli 1 botol susu")
else:
    print("Anak Pulang ke rumah")
if jumlah_telur > 0:
    print("Budi membeli 6 butir telur\n")
else:
    pass
print("Budi pulang ke rumah")
print("Menyerahkan hasil belanjanya kepada Ibu")
#done