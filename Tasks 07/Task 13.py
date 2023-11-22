array = ["Star Wars", "Fast and Furious", "Indiana Jones", "Mumia", "Lord of the Rings"]


file = open('films.txt', "w")

for title in array:
    file.write(title + "\n")


file = open("films.txt")

for line in file:
    print(line, end = "")

file.close()