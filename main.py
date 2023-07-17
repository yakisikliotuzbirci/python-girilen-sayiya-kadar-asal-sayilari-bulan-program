sayi = int(input("Sayi giriniz : "))
asalsayilar = []

for i in range(1, sayi):
    for asal in range(2, i):
        if i % asal == 0:
            break
        if not i % asal == 0 and (asal == i-1):
            asalsayilar.append(i)

print(f"{sayi} sayisina kadar bulunan asal sayilar : {asalsayilar}")