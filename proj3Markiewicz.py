# Anna Markiewicz
# Project 3 Homework
# Source Code file: proj3Markiewicz.py
# Input file: grade-records.txt

# Fields in grade-records.txt input file:
# stud_id, last_name, first_name, course_number, course_name, prof_name, credit_hours, grade

#input first and last name by the user

desired_first_name = input('What is your first name: ')
desired_last_name = input('What is your last name: ')

#initialize total_credit_hours and total_grade_points

total_credit_hours = 0
total_grade_points = 0

# Opening text file that will read the first line

fin = open("grade-records.txt", "r")

# Reads the first line and throws it away

fin.readline( )

# Read second line after first has been deleted

line = fin.readline( ) 

# Begin while statement when the line is not empty

while line != "":
	fields = line.split(",")
	last_name = fields[1].strip( )
	first_name = fields[2].strip( )
	credit_hours = int(fields[6].strip( ))
	grade = fields[7].strip('\n')
	if first_name == desired_first_name and last_name == desired_last_name:
		if grade == "A":
			grade_points = credit_hours * 4
		elif grade == "B":
			grade_points = credit_hours * 3
		elif grade == "C":
			grade_points = credit_hours * 2
		elif grade == "D":
			grade_points = credit_hours * 1
		else:
			grade_points = credit_hours * 0

		# End of if ... else statements 

		total_credit_hours += credit_hours
		total_grade_points += grade_points
		# End of if ... else statements 
	
	# Read the next line
	line = fin.readline( )
# Close the file

fin.close( )

# Compute the GPA and print result

gpa = total_grade_points / total_credit_hours
print(f"GPA for {desired_first_name} {desired_last_name} is {round(gpa, 2)}.")



