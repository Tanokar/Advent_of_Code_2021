#AdventOfCode_Day_Seven

readvar = open('crabbies', 'r')
kerbs = readvar.read().split(',')
for i in range(len(kerbs)):
	kerbs[i] = int(kerbs[i])

#part_one

maxwell = max(kerbs)
fuelcost = [0 for i in range(maxwell)]
position = 0
for t in range(maxwell):
	for i in range(len(kerbs)):
		if kerbs[i] > position:
			val = kerbs[i] - position
			fuelcost[position] += val
		if kerbs[i] < position:
			val = position - kerbs[i]
			fuelcost[position] += val
	position += 1
			
	

print(min(fuelcost))

#part_two

maxwell = max(kerbs)
fuelcost = [0 for i in range(maxwell)]
position = 0
for t in range(maxwell):
	for i in range(len(kerbs)):
		if kerbs[i] > position:
			val = kerbs[i] - position
			x = val * (val + 1)
			y = x/2
			fuelcost[position] += y
		if kerbs[i] < position:
			val = position - kerbs[i]
			x = val * (val + 1)
			y = x/2
			fuelcost[position] += y
	position += 1
			
	

print(min(fuelcost))

#NamingConventionExcuse
