file = open("inputFile.txt", 'r')
passfile = open("passFile.txt", 'w')
failfile = open("failFile.txt", 'w')
for line in file:
    splitline = line.split()
    if splitline[2] == "P":
        passfile.write(line)
    else:
        failfile.write(line)


file.close()
passfile.close()