# Definisikan fungsi konversisuhu dengan dua parameter: temperature dan value
def konversisuhu(temperature, value):
    # Jika value menunjukkan 'C', konversi dari Fahrenheit ke Celsius
    if value == 'C' :
        temperaturesuhu = (temperature - 32) * 5/9  # Rumus untuk konversi Fahrenheit ke Celsius
        return temperaturesuhu, 'C'  # Kembalikan hasil konversi beserta satuan Celsius
    # Jika value bukan 'C', konversi dari Celsius ke Fahrenheit
    else:
        temperaturesuhu = (temperature * 9/5) + 32  # Rumus untuk konversi Celsius ke Fahrenheit
        return temperaturesuhu, 'F'  # Kembalikan hasil konversi beserta satuan Fahrenheit

# Nilai suhu dalam Celsius yang akan dikonversi
celsius_temperature = 30
# Panggil fungsi konversisuhu untuk mengonversi suhu dari Celsius ke Fahrenheit
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
# Cetak hasil konversi
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Nilai suhu dalam Fahrenheit yang akan dikonversi
fahrenheit_temperature = 86
# Panggil fungsi konversisuhu untuk mengonversi suhu dari Fahrenheit ke Celsius
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
# Cetak hasil konversi
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")
