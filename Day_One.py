#AdventOfCode_Day_One

#part_one

readvar = open('input', 'r')
listInput = readvar.read().split('\n')
inputListSize = len(listInput) - 3
inc = 0

for i in range(inputListSize):
	index = i
	next = i + 1
	numA = int(listInput[i])
	numB = int(listInput[i+1])
	if numB > numA:
		inc = inc + 1
print(inc)

#part_two

readvar = open('input', 'r')
listInput = readvar.read().split('\n')
inputListSize = len(listInput) - 3
inc = 0

for i in range(inputListSize):
	index = i
	next = i + 1
	groupA = int(listInput[i]) + int(listInput[i+1]) + int(listInput[i+2])
	gropuB = int(listInput[i+1]) + int(listInput[i+2]) + int(listInput[i+3])
	if gropuB > groupA:
		inc = inc + 1
print(inc)

#NamingConventionExcuse
