# Z1
var = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

# Z2
name = "Adam"
surname = "Stepanczuk"
nameLetter = name[1]
surnameLetter = surname[2]
print("W tekscie jest %i liter '%s' oraz %i liter '%s'" % (var.count(nameLetter), nameLetter, var.count(surnameLetter), surnameLetter))

# Z4
zmienna_typu_string = var
print(dir(zmienna_typu_string))
help(zmienna_typu_string.islower)

# Z5
print((name[-1:-5:-1]).capitalize() + " " + (surname[-1:-11:-1]).capitalize())

# Z6
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list1[5:]
list1 = list1[:5]
print(list1, list2)

# Z7
list3 = list1 + list2
list3.insert(0, 0)
list3copy = list3.copy()
list3copy.sort(reverse=True)
print(list3copy)

# Z8
student1Tuple = (100001, "imie1 nazwisko1")
student2Tuple = (100002, "imie2 nazwisko2")
student3Tuple = (100003, "imie3 nazwisko3")
student4Tuple = (100004, "imie4 nazwisko4")
student5Tuple = (100005, "imie5 nazwisko5")
studentListTuple = student1Tuple, student2Tuple, student3Tuple ,student4Tuple, student5Tuple
print(studentListTuple)

# Z9
dictionary = {}
for element in studentListTuple:
    dictionary[element[0]] = element[1]

dataForPair1 = [27, "mail1@mail.com", 1994, "Sloneczna 10/10"]
dataForPair2 = [25, "mail2@mail.com", 1996, "Sloneczna 32"]
dictionary["para1"] = dataForPair1
dictionary["para2"] = dataForPair2
print(dictionary)

# Z10
phoneList = [111222333, 444555666, 777888999, 777888999, 111222333, 777888999]
phoneList = set(phoneList)
print(phoneList)
# Z11
listZ11 = []
for i in range(1, 11):
    listZ11.append(i)
print(listZ11)

# Z12
listZ12 = []
for i in range(100, -21, -5):
    listZ12.append(i)
print(listZ12)

# Z13
dictionary1 = {"one": 1, "two": 2, "three": 3}
dictionary2 = dictionary
listZ13 = []
listZ13.append(dictionary1) 
listZ13.append(dictionary2) 
varString = ""
for element in listZ13:
    for key, value in element.items():
        if isinstance(value, list):
            for element2 in value:
                varString += str(element2) + ", "
        else:
            varString += str(value) + ", "
print(varString)
