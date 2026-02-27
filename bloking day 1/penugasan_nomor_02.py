import math

#TABUNG
r = float(input("Masukkan jari-jari tabung:"))
t = float(input("Masukkan tinggi tabung:"))
volume_tabung = math.pi * r * r * t
print("Volume Tabung =",volume_tabung)

#BALOK
p = float(input("\nMasukkan panjang balok:"))
l = float(input("Masukkan lebar balok:"))
t = float(input("Masukkan tinggi balok:"))
volume_balok = p * l * t
print("Volume Balok =",volume_balok) 