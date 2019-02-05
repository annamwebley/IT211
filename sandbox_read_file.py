fin = open("grade-records.txt", "r")

#read a single line and do nothing iwth it
fin.readline( )


#read Next single line and stick the string inthe "line" variable

line = fin.readline()


#start a loop that will begin by evaluatin "line", do work, read one more line, until it get ""

while line !="":
    print(line)

    #Now time to read next line
    line = fin.readline()