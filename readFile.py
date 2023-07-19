file = open("inputFile.txt", 'r')
passfile = open("passFile.txt", 'w')
failfile = open("failFile.txt", 'w')
namesfile = open("namesFile.txt", 'w')
count = 0
for line in file:
    count += 1
    splitline = line.split()
    if splitline[2] == "P":
        passfile.write(f"{count}. {line}")
    else:
        failfile.write(f"{count}. {line}")
    namesfile.write(f"{count}. {splitline[0]}\n")


file.close()
passfile.close()