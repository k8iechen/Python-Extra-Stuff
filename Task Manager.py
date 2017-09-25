print "HACKcode Project"
#C:\Users\Owner\Documents\ComSci\Python\HACKcode.py

print "Example 1: Task Scheduler"
def print_schedule():
	print "1. Print Schedule"
	print "2. Add a Task"
	print "3. Remove a Task"
	print "4. Lookup a task"
	print "5. Total Workload in Hours"
	print "6. Quit"
	print
schedule = {}
schedule_choice = 0
print_schedule()

ldd = []
ls = []
ld = []
lh = []

while schedule_choice != 6:
	schedule_choice = input("Type in a number (1-5):")
	if schedule_choice == 1:
		print "Schedule: "
		for x in schedule.keys():
			print "Task Name: ",x," \tDue Date: ",schedule[x][0]," \tSubject: ",schedule[x][1],  " \tDifficulty: ",schedule[x][2], " \tHours Needed: ",schedule[x][3]
		print
	elif schedule_choice == 2:
		print "Add Task and Description."
		name = raw_input("Task Name: ")
		dd = raw_input("Due Date: ")
		#ldd.append(dd)
		s = raw_input("Subject: ")
		#ls.append()
		d = raw_input("Difficulty: ")
		#ld.append()
		h = input("Estimated Hours Needed: ")
		lh.append(h)
		l = [dd,s,d,h]
		schedule[name] = l
	elif schedule_choice == 3:
		print "Remove Completed Tasks"
		name = raw_input("Task Name:")
		if schedule.has_key(name):
			del schedule[name]
		else:
			print name," was not found"
	elif schedule_choice == 4:
		print "Lookup Task Details"
		name = raw_input("Name: ")
		if schedule.has_key(name):
			print "Task Description: "," \tDue Dates: ",schedule[name][0]," \tSubject: ",schedule[name][1],  " \tDifficulty: ",schedule[name][2], " \tHours Needed: ",schedule[name][3]
		else:
			print name," was not found"
	elif schedule_choice == 5:
		print sum(lh)
	elif schedule_choice != 5:
		print_schedule()
print 

#--------------------------------------------------------------------------------------------------------

print "Example 2: Student Grades"
print
max_points = [25,50,100,100,100]
assignments = ['hw ch 1','hw ch 2','quiz','hw ch 3','test']
students = {'#Max':max_points} #dictionary (Name; Grade)
#"#Max" is used since "#" is in front of all alphabet characters

def print_schedule():
	print "1. Add student"
	print "2. Remove student"
	print "3. Print grades"
	print "4. Record grade"
	print "5. Print Menu"
	print "6. Exit"

def print_all_grades():
	print '\t',
	for i in range(len(assignments)):
		print assignments[i],'\t',
	print
	keys = students.keys()
	keys.sort()
	for x in keys:
		print x,'\t',
		grades = students[x]
		print_grades(grades)

def print_grades(grades):
	for i in range(len(grades)):
		print grades[i],'\t\t',
	print

print_schedule()
schedule_choice = 0
while schedule_choice != 6:
	print
	schedule_choice = input("Menu Choice (1-6):")
	if schedule_choice == 1: #adds student names with empty lists
		name = raw_input("Student to add:")
		students[name] = [0]*len(max_points)#array of 0s same length as max_points list
	elif schedule_choice == 2:#deletes similar to the phone book concept
		name = raw_input("Student to remove:")
		if students.has_key(name):
			del students[name]
		else:
			print "Student Name: ",name," not found"
	elif schedule_choice == 3:
		print_all_grades()

	elif schedule_choice == 4:
		print "Record Grade"
		name = raw_input("Student:")
		if students.has_key(name):
			grades = students[name]
			print "Type in the number of the grade to record"
			print "Type a 0 (zero) to exit"
			for i in range(len(assignments)):
				print i+1,' ',assignments[i],'\t', #prints # and assignment title
			print
			print_grades(grades)
			which = 1234
			while which != -1:
				which = input("Change which Grade:")
				which = which-1
				if 0 <= which < len(grades):
					grade = input("Grade:")
					grades[which] = grade
				elif which != -1:
					print "Invalid Grade Number"
		else:
			print "Student not found"
	elif schedule_choice != 6:
		print_schedule()