

week = int(input("Hur många veckor vill du beräkna budget för?"))
print("Hur mycket vill du spendera per vecka på;")

hyra = int(input("Hur mycket vill du lägga på hyra: "))
mat = int(input("Hur mycket vill du lägga på mat: "))
kläder = int(input("Hur mycket vill du lägga på kläder: "))
mobilräkning = int(input("Hur mycket vill du lägga på mobilräkning: "))
nöje = int(input("Hur mycket vill du lägga på nöje: "))

summa = (hyra + mat + kläder + mobilräkning + nöje) * week
print("Du är uppe i " + str(summa) + " kronor.")

if summa == 5000:
    print("Exakt 5000")
elif summa > 5000:
     print("Du har passerat budgeten")
else:
    print("Mindre än 5k du är fattig!")
