#Lektion 2, lister og loops
print("#########Lektion 2 - OPGAVER#######")

print("Opgave 0")
#her har jeg installeret GIT og forsøgt at gemme hans løsninger mm (find Git med hans løsninger under ugeplan, lektion 2, kode)

#Opgave 1, definition af lister og loops
print("\nOpgave 1")
yndlingsforfatter = ['Hansen', 'Jensen', 'Linde', 'Borggaard', 'Nielsen']
print(yndlingsforfatter)

for forfatter in yndlingsforfatter:
    print(forfatter)

#opgave 2, modifikation, tilføjelse og sletning af lister
print("\nOpgave 2")

#her tilføjer jeg et navn til sidst
yndlingsforfatter.append("Kurtsen")
print(yndlingsforfatter)

#her sletter jeg ord nr. 2
del yndlingsforfatter[1]
print(yndlingsforfatter)

#opgave 3, længden af en liste
print("\nOpgave3")

print(len(yndlingsforfatter))
lengde = (len(yndlingsforfatter))
print(lengde)

#opgave 4, reverse
print("\nOpgave 4")
yndlingsforfatter.reverse()
print(yndlingsforfatter)

#Opgave 5, lister af tal
print("\nOpgave 5")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste)

for value in range(1,11):
    print(value)

tal_liste = list(range(3,100,3))
print(tal_liste)

#opgave 6, andre operationer på lister
print("\nOpgave 6")

til_beregning = tal_liste
print(min(til_beregning))
print(max(til_beregning))
print(sum(til_beregning))

#finde gennemsnit
print("\nfinde gennemsnit")

#finder antal/længde i til_beregning
print(len(til_beregning))

#dividere sum af linjen med antal i længden
gennemsnit = sum(til_beregning)//(len(til_beregning))
print(gennemsnit)

#Opgave 7, slicing af lister
print("\nOpgave 7")

yndlingsforfatter = ['Hansen', 'Jensen', 'Linde', 'Borggaard', 'Nielsen']
print(yndlingsforfatter[0:3])
print(yndlingsforfatter[-2:])
#husk til mig selv, at den ikke tager det sidste med - fx i den første skulle jeg skrive 3, selvom det er fra 0 til 2

#Opgave 8, kopiering af en liste
print("\nOpgave 8")
yndlingsforfatter = ['Hansen', 'Jensen', 'Linde', 'Borggaard', 'Nielsen']

""" dette herunder køre fejl, hvis jeg lavede det - så nu har jeg bare skrevet. Det er ikke en kopi!!
kopi = yndlingsforfatter
kopi.append(“Dostojevski”)
print(kopi)
print(yndlingsforfatter)
"""

kopi = yndlingsforfatter [:]
kopi.append("Dostojevski")
print(kopi)

#ny kommentar, øve GIT