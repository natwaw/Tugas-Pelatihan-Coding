print("Program Konversi Suhu")

mulai = (input("Apakah anda ingin meng-konversi suhu? jika ya tekan enter")) 

print("1.  konversi Celcius ke Reamur")
print("2.  konversi Celcius ke Farenheit")
print("3.  konversi Celcius ke Kelvin")
print("4.  konversi Reamur ke Celcius")
print("5.  konversi Reamur ke Fahrenheit")
print("6.  konversi Reamur ke Kelvin")
print("7.  konversi Fahrenheit ke Celcius")
print("8.  konversi Fahrenheit ke Reamur")
print("9.  konversi Fahrenheit ke Kelvin")
print("10. konversi Kelvin ke Celcius")
print("11. konversi Kelvin ke Reamur")
print("12. konversi Kelvin ke Fahrenheit")

Opsi = int(input("Pilih menu : "))

#keterangan : a = Celcius ; b = Reamur ; c = Farenheit ; d = Kelvin

if Opsi == 1:
    a = float(input("Masukkan suhu yang ingin di konversi : "))
    b = 4/5*a
    print("Hasil konversi Celcius ke Reamur adalah", b,"R")

if Opsi == 2:
    a = float(input("Masukkan suhu yang ingin di konversi : "))
    c = (9/5*a)+32
    print("Hasil konversi Celcius ke Farenheit adalah", c,"F")

if Opsi == 3:
    a = float(input("Masukkan suhu yang ingin di konversi : "))
    d = a +273
    print("Hasil konversi Celcius ke Kelvin adalah", d,"K")

if Opsi == 4:
    b = float(input("Masukkan suhu yang ingin di konversi : "))
    a = 5/4*b
    print("Hasil konversi Reamur ke Celcius adalah", a,"C")

if Opsi == 5:
    b = float(input("Masukkan suhu yang ingin di konversi : "))
    c = 9/4*(b+32)
    print("Hasil konversi Reamur ke Farenheit adalah", c,"F")

if Opsi == 6:
    b = float(input("Masukkan suhu yang ingin di konversi : "))
    d = 5/4*(b+273)
    print("Hasil konversi Reamur ke Kelvin adalah", d,"K")

if Opsi == 7:
    c = float(input("Masukkan suhu yang ingin di konversi : "))
    a = (c-32)*5/9
    print("Hasil konversi Farenheit ke Celcius adalah", a,"C")

if Opsi == 8:
    c = float(input("Masukkan suhu yang ingin di konversi : "))
    b = 4/9*(c-32)
    print("Hasil konversi Farenheit ke Reamur adalah", b,"R")

if Opsi == 9:
    c = float(input("Masukkan suhu yang ingin di konversi : "))
    d = (c-32)*5/9+273.15
    print("Hasil konversi Farenheit ke Kelvin adalah", d,"K")

if Opsi == 10:
    d = float(input("Masukkan suhu yang ingin di konversi : "))
    a = d-273.15
    print("Hasil konversi Kelvin ke Celcius adalah", a,"C")

if Opsi == 11:
    d = float(input("Masukkan suhu yang ingin di konversi : "))
    b = 4/5*(d-273.15)
    print("Hasil konversi Kelvin ke Reamur adalah", b,"R")

if Opsi == 12:
    d = float(input("Masukkan suhu yang ingin di konversi : "))
    c = 9/5*(d-273.15)+32
    print("Hasil konversi Kelvin ke Farenheit adalah", c,"F")
    
    