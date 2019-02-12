"""i kap 3 lærer jeg om Lists"""

bicycles = ['trek','cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

#lært at jeg kan lave lister. skrive print, så tilføj nr. jeg vil ha ud fx 0, og jeg kan få skrevet med stort mm
#og husk at list starter med 0, så nr. 3 ord er nr. 2 i listen. s. 39 i bogen

print(bicycles[2])

print(bicycles[-1])
# når jeg skriver -1, så tager den sidste ord og hvis skrevet -2, så anden sidste ord osv..

message = "my first bicycles was a " + bicycles[0].title() + "."
print (message)

#ændrer ord i listen
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#tilføje ord til list (og ofte starter vi med tom liste, og så tilføjer undervejs)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcyles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#jeg kan også indsætte på en bestemt plads ved at bruge .insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#slette et ord i listen, hvor du kender placering ved brug af del funktion
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

#fjern sidste ord med genbruge vha. pop funktion. s. 44 i bogen
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#vi kan fjerne hvilket som helst ord, og bruge det med pop. (HUSK jeg bruger pop, så fjernes det fra listen!!)
first_owned = motorcycles.pop(0)
print("My first motorcycle was " + first_owned.title())

#jeg kan bruge remove til at fjerne (HUSK at den kun fjerner det første gang den ser - så hvis ducati to gange, så kun første slettes
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#jeg kan slette ordet, så jeg kan bruge det igen
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive to me")

#sortere list fx alfabetisk (og vi kan derefter ikke ændre tilbage)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#omvendt alfabetisk
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# hvis bare midlertidig sorteret, så brug sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("here is the original list:")
print(cars)
print("\nhere is the sorted list:")
print(sorted(cars))
print("\nhere is the orginal liste again:")
print(cars)

#hvis printe listen baglæns, så brug reverse(), det ændres permanent! men jeg kan altid ændre tilbage med reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#finde længden på listen. s. 49 i bogen. (den tæller antal, så 0-1-2-3 er = 4)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

"""i KAP 4 vil jeg lære at lave simple lister, og arbejde med de individuelle elementer i en liste"""
print("#############KAP 4####################")

#lære at print navne fra en liste individuelt med "for" s. 54  (den tænker i loops)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + " that was a good trick!")

#jeg prøver at tilføje to linjer i for Loop funktion
for magician in magicians:
    print(magician.title() + " that was a good trick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")

#jeg prøver at afslutte med fælles tak. s. 56
for magician in magicians:
    print(magician.title() + " that was a good trick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone")

#på s. 57 - 60 viser de forskellige fejl der ofte gøres med indrykning

# numeriske lister, s. 61
for value in range(1,5):
    print(value)
#bemærk ved ovenstående, at den ikke printer 5 med. Den tager ikke sidste med, så skal skrive (1,6), hvis 5 med.

numbers = list(range(1,6))
print(numbers)

#fortælle hvordan vi springer over nogle tal, s. 62
even_numbers = list(range(2,11,2))
print(even_numbers)

#herunder to eksempler på at jeg kan bruge range. den første her er liste med 1-10 hvor alle er udregnet opløftet i 2.
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#denne gør det samme bare skrevet anderledes:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#hvordan finder jeg mindste, største, sum af en liste
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#jeg kan også lave list comprehensions: dvs. jeg skriver det på en linje:
squares = [value**2 for value in range(1,11)]
print(squares)

print("\nslice")
#Hvordan arbejder jeg med en del af en liste = slice:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#jeg kan lade være med at skrive først eller sidst, så begynder den enten forfra eller medtager sidste. eks.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

print(players[-3:])
#ovenfor tog jeg de sidste tre spillere

#bruge for Loop med slice, s. 66
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nKopi")
#lave kopi af liste, s. 67
my_foods = ['pizzs', 'falafel', 'carrot cake']
frind_foods = my_foods [:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(frind_foods)

#men så vil jeg vise at selvom det ligner vi lige nu bruger samme linje til de to, så er de forskellige
my_foods = ['pizzs', 'falafel', 'carrot cake']
frind_foods = my_foods [:]

my_foods.append('cannoli')
frind_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friends favorite foods are:")
print(frind_foods)

#lister der IKKE kan ændres, tuples, s. 69  - brug parantes i stedet for []

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# hvis jeg prøvede dette: dimensions[0] = 250 for at ændre 200 til 250, kan jeg ikke, fordi ikke ændre tuple!!

#vi kan dog godt overskrive en tuple:
dimensions = (200, 50)
print("Original demensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

"""God stil når jeg koder, s. 72 og 73"""
#når ændring så Python Enhancement Proposal PEP  (mange bruger PEP 8 guidelines)
#brug four spaces per indentation level (pas på at bruge space og ikke tab)
#tænk på linjeængde, nogle siger max 80, PEP 8 siger 72, andre siger max 99 osv..
#tænk på at bruge blanke linjer - ikke for meget, men kan give godt overblik