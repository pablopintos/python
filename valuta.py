#FRÅGA EFTER NAMN
name = input("Vad heter du?")
#VÄLKOMNA ANVÄNDAREN
print("Välkommen, " + name)
print("-"*30)
print("Valutakonverteraren")
print("="*20)
#V
antalet = int(input("Antal SEK: "))
kurs = 6.905
print("Växelkurs: 6.905")

summa = (antalet) / (kurs)
print("För " + str(antalet) + " kronor får du " + str(summa) + " dollar.")
