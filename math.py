import math  # Library untuk operasi matematika

# Lambda function untuk menghitung luas lingkaran
# Fungsi ini menerima jari-jari (r) dan menghitung luas lingkaran menggunakan rumus: π * r^2
luas_lingkaran = lambda r: math.pi * r * r

# Contoh penggunaan
jari_jari = 7  # Mendefinisikan jari-jari lingkaran
area = luas_lingkaran(jari_jari)  # Menghitung luas lingkaran dengan jari-jari yang diberikan

# Menampilkan hasil dengan format dua desimal
# Menggunakan f-string untuk mencetak hasil dengan format dua angka di belakang koma
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")