# Anna Markiewicz P Homework
# Draw the letter P using asterisks

#Open output file
fout = open ("p.txt", "w")


#Draw first line

def draw_line_horizontal(length, lines):
    for y in range(0,lines):
        for x in range (0,length):
            fout.write("*", end="")
    fout.write()

def draw_opposites(length, lines):
    for y in range(0,lines):
        for x in range (0,1):
            fout.write("*", end="")
        for x in range(1,length - 1):
            fout.write(" ", end="")
        for x in range (0,1):
            fout.write("*", end="")  
        fout.write()

def draw_line_vertical(lines):
    for y in range (lines):
        fout.write("*")

def draw_triangle_bottom(length, lines):
    for y in range(0, lines):
        fout.write("*", end="")
        # ((y * 2)-1) creates a nice angle 
        for x in range(0, (y * 2)-1):
            fout.write(" ", end="")
        fout.write("*")

def draw_triangle_top(length, lines):
    for y in range(0, lines):
        fout.write("*", end="")
        # ((y * 2)-1) creates a nice angle 
        for x in range(0, length - y):
            fout.write(" ", end="")
        fout.write("*")



width = 8

draw_line_horizontal(width,1)
draw_opposites(width,2)
draw_line_horizontal(width,1)
draw_line_vertical(4)
fout.write("---------")
draw_triangle_top(5,5)
draw_triangle_bottom(5,5)

fout.close()
