# Felix Magnusson, TK21
# Moment02:a + tillägg
# Jag tycker att jag inte stötte på några större problem i skapande av koden.
# Det en som jag anser ett problem är att jag hade svårt med mellan rummet på svaren.
# Jag hade senare problem med att göra if else funktionen att ge dem resultat jag ville genom att göra om radien
# till int
# men det funkade inte, så sen insåg jag att jag bara behövde göra så att float funktionen inte hade några decimaler
#

# Import för att få tag i konstanten PI
import math

# För att etablera för vem som helst vad det är för något.
print("Detta är en cirkel kalkylator som kommer ge dig din cirkels area och omkrets, om du ger den din cirkelns radie, "
      "i cm.")
svar = input("Har din radie en decimal (om du inte svarar med något annat så behandlas det som ett nej)"
             ", svara med ja eller nej? ")
print("Skriv cirkelns radie utan måttet i raden nedan.")
# Början av variablerna och input
radie = float(input("Ange cirkelns radie här: "))
pi = math.pi
area = radie * radie * pi
Omkrets = 2 * pi * radie

# Outputen från variablerna + if else selektion
if svar == "ja":
    print(f"Radien du gav var: {radie:>12.02f} cm")
else:
    print(f"Radien du gav var: {radie:>12.0f} cm")

print(f"Din cirkels area är: {area:>10.02f} cm\u00b2")
print(f"Dess Omkrets är: {Omkrets:>14.02f} cm")
