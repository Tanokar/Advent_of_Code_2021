#AdventOfCode_Day_Three

readvar = open('Coords', 'r')
rawString = readvar.read().split('\n')
filteredString = []
for i in range(len(rawString)):
	line = ''
	for x in rawString[i]:
		if x == '0':
			line += x
		elif x == '1':
			line += x
		elif x == '2':
			line += x
		elif x == '3':
			line += x
		elif x == '4':
			line += x
		elif x == '5':
			line += x
		elif x == '6':
			line += x
		elif x == '7':
			line += x
		elif x == '8':
			line += x
		elif x == '9':
			line += x
		elif x == '-':
			line += x
		elif x == ',':
			line += '-'
	filteredString.append(line)

for i in range(len(filteredString)):
	filteredString[i] += '-'

listIGuess = []
for i in range(len(filteredString)):
	x1 = ''
	for x in filteredString[i]:
		if x == '0':
			x1 += x
		elif x == '1':
			x1 += x
		elif x == '2':
			x1 += x
		elif x == '3':
			x1 += x
		elif x == '4':
			x1 += x
		elif x == '5':
			x1 += x
		elif x == '6':
			x1 += x
		elif x == '7':
			x1 += x
		elif x == '8':
			x1 += x
		elif x == '9':
			x1 += x
		elif x == '-':
			listIGuess.append(x1)
			x1 = ''

listIGuesss = []

for i in range(len(listIGuess)):
	listIGuesss.append(int(listIGuess[i]))

Coords = []
coord = []
pair = []
count = 0
for val in range(0, len(listIGuesss), 2):
	coord.append(listIGuesss[val])
	coord.append(listIGuesss[val+1])
	pair.append(coord)
	coord = []
	count += 1
	if count == 2:
		Coords.append(pair)
		pair = []
		count = 0
	

for x in Coords[0:8]:
	print(x)

Grid = [[0 for i in range(1000)] for i in range(1000)]

for coord in Coords:
	start, end = coord
	startx, starty = start
	endx, endy = end

testCoords = [[[2,2], [2,6]], [[1,4],[7,4]], [[5,9], [9,5]], [[0,0], [4,4]]]

def drawLine(x1,y1,x2,y2):
	if x1 == x2:
		if y1 < y2:
			while y1 <= y2:
				Grid[y1][x1] += 1
				y1 += 1
		else:
			while y2 <= y1:
				Grid[y1][x1] += 1
				y1 -= 1
	elif y1 == y2:
		if x1 < x2:
			while x1 <= x2:
				Grid[y1][x1] += 1
				x1 += 1
		else:
			while x2 <= x1:
				Grid[y1][x1] += 1
				x1 -= 1
	else:
		while x1 != x2 and y1 != y2:
			Grid[y1][x1] += 1

			x1 += 1 if x1 < x2 else -1
			y1 += 1 if y1 < y2 else -1
		
		Grid[y1][x1] += 1
	# place down lines given endpoints

def printGrid():
	for x in Grid:
		for y in x:
			print('.' if y == 0 else y, end=" ")
		print()

for c in Coords:
	drawLine(c[0][0], c[0][1], c[1][0], c[1][1])
# printGrid()
OL = 0
for i in range(len(Grid)):
	for x in Grid[i]:
		if x > 1:
			OL += 1
print(OL)


#NamingConventionExcuse
