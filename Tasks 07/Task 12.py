name = "Piotr Sklad"
university = "Krakow University of Economics"
field = "Applied Informatics"


file = open('student.txt', "w")
file.write(name + "\n")
file.write(university + "\n")
file.write(field)


file.close()

file = open('student.txt', "r")

for line in file:
    print(line, end = '')

file.close()