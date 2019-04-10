ccw = [1977, 4, 13, "Han", "Shanghai", "Yunnan", 176, 72]
lh = [1977,9,9, 'Han', 'Yunnan', 'Yunnan', 160, 56]
astring = " "
for element in lh:
    astring += str(" "  + str(element))
print(astring)
lh[2] = 13
ccw.insert(2, 32)
print("ccw".upper() + "'s birthday is\t" + str(ccw[0]) + "-" + str(ccw[1]) + "-" + str(ccw[2]) + ". He born in " + ccw[5])
del ccw[2]
print("ccw".upper() + "'s birthday is\t" + str(ccw[0]) + "-" + str(ccw[1]) + "-" + str(ccw[2]) + ". He born in " + ccw[5])
print("lh".upper() + "'s birthday is\t" + str(lh[0]) + "-" + str(lh[1]) + "-" + str(lh[2]))

for cell in lh:
    if cell == "Yunnan":
        print(str(cell.upper()))
    else:
        print(str(cell))

popped_ccw = ccw.pop(6)
print(ccw)
print(popped_ccw)

ccw.remove(72)
print(ccw)

ccw.remove("Han")
ccw.remove('Shanghai')
ccw.remove('Yunnan')
ccw.sort()
print(ccw)

number = [3, 56, 14, 4.5]
print("Original order is: " + str(number))
print("Length is: " + str(len(number)))
print("Temp sorted: " + str(sorted(number)))
number.reverse()
print("Reversed 1st: " + str(number))
number.reverse()
print("Reversed 2nd: " + str(number))

s = []
#for value in range(1.0, 1.3):
#    s.insert(0, value)
#print(s)

for value in range(1,11,2):
    s.append(value ** 2)
print(s)

s = [value for value in range(1,11)]
#print(str(min(s)))
#print(str(max(s)))
#print(str(sum(s)))
print(s)
print(s[0:len(s)])
a = s[:]
a.append(100)
s.append((1000))
print(a)
print(s)

car = 'bmw'
if car == 'audi':
    print ('True')
else:
    print('False')

pizza = []
if pizza:
    print('OK\n')
else:
    print('Empty\n')

crc = {'FirstName' : 'ruochu', 'LastName' : 'Chen',
       'BirthYear' : 2009, 'BirthMonth' : 7, 'BirthDay' : 24}
ccw = {'FirstName' : 'changwei', 'LastName' : 'Chen',
       'BirthYear' : 1977, 'BirthMonth' : 4, 'BirthDay' : 13}
lh = {'FirstName' : 'hong', 'LastName' : 'Li',
       'BirthYear' : 1977, 'BirthMonth' : 9, 'BirthDay' : 9}

crc['Gender'] = False
ccw['Gender'] = True
lh['Gender'] = False

FamilyChen = []
FamilyChen.append(crc)
FamilyChen.append(ccw)
FamilyChen.append(lh)
for member in FamilyChen:
    if member['FirstName'] == 'changwei':
        print("Family Host:")
    else:
        print("Family Member:")
    if member['Gender']:
        strGender = '(M)'
    else:
        strGender = '(F)'
    print(str(member['FirstName'].title()) + strGender)

crc2 = {'FirstName' : 'Ruochu', 'LastName' : 'Chen',
       'BirthYear' : 2009, 'BirthMonth' : 7, 'BirthDay' : 24,
        'Gender' : False}

if crc == crc2:
    print("Equal")

del crc2['Gender']
if crc != crc2:
    print('Deleted')

for key, value in crc2.items():
    print(str(key) + "\t:\t" + str(value))
listA = crc2.keys()
for a in listA:
    print(str(a))
print(str(crc2.keys()))
print(str(crc2.values()))

FamilyChen.append(crc2)
#FamilyOne = [crc={}, ccw = {}, lh = {}]

#SayHello = "Tell me something: "
#message = ''
#while message != 'quit':
#    message = input(SayHello)
#    if message != 'quit':
#        print('Copy: ' + message.title() + "\n")

#for a in range(1, 100, 3):
#    if a % 2 == 0:
#        continue
#    else:
#        b = int(input(str(a) + ' is an odd number. Please given a factor: ' ))
#        print ('The value is: ' + str(a * b))

def printHello(value1, value2, value3 = ''):
    if value3:
        print("Hello, " + str(value1 * value2 * 1) + "!")
    else:
        print("Hello, " + str(value1 * value2 * 0) + "!")
printHello(2,3)

City1 = {'Country' : 'Holand', 'City' : 'Amsterdam', 'Capital' : False}
City2 = {'Country' : 'Italy', 'City' : 'Milan', 'Capital' : False}
City3 = {'Country' : 'France', 'City' : 'Paris', 'Capital' : True}

CityList=[City1, City2, City3]

def HelloCity(City, Country, Capital):
    if Capital == True:
        print("\"" + City + ", Capital of " + Country + "\"")
    else:
        print("\"" + City + ", "  + Country + "\"")

HelloCity(City1['City'], City1['Country'], City1['Capital'])
HelloCity(City2['City'], City2['Country'], City2['Capital'])
HelloCity(City3['City'], City3['Country'], City3['Capital'])

for city in CityList:
    HelloCity(city['City'], city['Country'], city['Capital'])

def InputCity():
   city = input("Input a name of City (input q to exit): \n")
   if city == 'q':
       return False;
   country = input("The city is located in (input q to exit): \n")
   if country == 'q':
       return False;
   strcapital = input("Is it the capital (input q to exit)? Y (yes)/N (no)\n")
   if strcapital.lower() == 'y':
       capital = True
   elif strcapital.lower() == 'n':
       capital = False
   elif strcapital == 'q':
       return False;
   else:
       capital = False
   citymember = {'Country' : country, 'City': city, 'Capital' : capital}
   return citymember


City4 = {'Country' : 'China', 'City' : 'Shanghai', 'Capital' : False}

CityList.append(City4)

print("Total " + str(len(CityList)) + " cities in the list")

ACity = InputCity()
while ACity != False:
    ACity = InputCity()
#print("The city is " + ACity['City'].title())
#print("It is in " + ACity['Country'].title())
#if ACity['Capital'] == True:
#    print("It's the capital.")
#    CityList.append(ACity)

print("Total " + str(len(CityList)) + " cities in the list")

def HelloCities(cities):
    for city in cities:
        HelloCity(city['City'], city['Country'], city['Capital'])

def HelloACity(city):
    HelloCity(city['City'], city['Country'], city['Capital'])


for city in CityList:
    HelloCity(city['City'], city['Country'], city['Capital'])

for city in CityList:
    HelloACity(city)

HelloCities(CityList)


exit(1)