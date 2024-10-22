def konversisuhu(temperature, value):
#Fungsi ini mengonversi suhu antara Celsius dan Fahrenheit

    # Jika nilai 'value' adalah 'C', kita konversi dari Fahrenheit ke Celsius
    if value == 'C':
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'  # Mengembalikan suhu dalam Celsius
    else:
        # Jika nilai 'value' adalah 'F', kita konversi dari Celsius ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'  # Mengembalikan suhu dalam Fahrenheit

# Mengonversi 30 Celsius ke Fahrenheit
celsius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'C')
# Mencetak hasil konversi dari Celsius ke Fahrenheit
print(f"{celsius_temperature}℃ dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Mengonversi 86 Fahrenheit ke Celsius
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'F')
# Mencetak hasil konversi dari Fahrenheit ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celsius adalah {temperaturesuhu}°{target_value}")

# Penjelasan Elemen Kode:
# 1. 'def' digunakan untuk mendefinisikan fungsi, yang merupakan blok kode yang dapat digunakan kembali.
# 2. 'if' memeriksa suatu kondisi dan menjalankan kode jika kondisi tersebut benar.
# 3. 'else' menyediakan jalur alternatif untuk kode yang akan dijalankan jika kondisi dalam 'if' salah.
# 4. 'print' mengeluarkan informasi ke konsol, memungkinkan pengguna untuk melihat hasil dari program.