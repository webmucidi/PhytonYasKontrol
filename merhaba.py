ad=str(input("Adınızı girin: "))
sinav1=int(input("1.sınav notunuzu girin: "))
sinav2=int(input("2.sınav notunuzu girin: "))
performans=int(input("Performans notunuzu girin: "))

ortalama=int((sinav1+sinav2+performans)/3)


if ortalama>=50:
    print ("Tebrikler,geçtiniz :)")
else:
    print("Maalesef kaldınız :(")

print (ortalama)

