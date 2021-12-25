#AdventOfCode_Day_Eight

readvar = open('codes','r')
codes = readvar.read().split('\n')
ans = 0

#part_one

splitCode = []
left = []
right = []
smolright = []
ans = 0
for i in range(len(codes)):
	t = codes[i].split('|')
	splitCode.extend(t)
count = 1
for i in range(len(splitCode)):
	if count == 1:
		left.append(splitCode[i])
	if count == 2:
		right.append(splitCode[i])
		count = 0
	count += 1
for i in range(len(right)):
	g = right[i].split()
	smolright.extend(g)
for i in range(len(smolright)):
	if len(smolright[i]) == 2 or len(smolright[i]) == 4 or len(smolright[i]) == 3 or len(smolright[i]) == 7:
		ans += 1
print(ans)

#part_two

newlist = [codes[i].split(' | ') for i in range(len(codes))]
newlist = [[g[0].split(), g[1].split()] for g in newlist]


def thealgorithm(sigpats, display):
	# print('running the algorithm')
	key = {num:'' for num in range(10)}
	fives = []
	sixes = []
	top = ''
	topLeft = ''
	botLeft = ''
	for i in range(len(sigpats)):
		if len(sigpats[i]) == 2:
			key[1] = sigpats[i]
		if len(sigpats[i]) == 3:
			key[7] = sigpats[i]
		if len(sigpats[i]) == 4:
			key[4] = sigpats[i]
		if len(sigpats[i]) == 7:
			key[8] = sigpats[i]
		if len(sigpats[i]) == 5:
			fives.append(sigpats[i])
		if len(sigpats[i]) == 6:
			sixes.append(sigpats[i])
	seven = set(key[7])
	one = set(key[1])
	top = seven.difference(one)
	# print('top is ' + str(top))
	# finds 3 pattern
	for i in range(len(fives)):
		before = len(fives[i])
		x = set(fives[i])
		y = set(key[1])
		after = len(x.difference(y))
		# print('Looking for 3')
		if before == after + 2:
			key[3] = fives[i]
			# print('target 3 identified')
			fives.pop(i)
			break
	# if key[3] == '':
		# print('3 was not found')
	# finds 9 pattern
	for i in range(len(sixes)):
		x = set(sixes[i])
		y = set(key[3])
		if x.issuperset(y):
			key[9] = sixes[i]
			# print('target 9 identified')
			sixes.pop(i)
			nine = set(key[9])
			three = set(key[3])
			topLeft = nine.difference(three)
			# print('top left is ' + str(topLeft))
			break
	
	# finds 2 and 5 patterns
	which = set(fives[0])
	isit = set(topLeft)
	if isit.issubset(which):
		key[5] = fives[0]
		key[2] = fives[1]
	else:
		key[2] = fives[0]
		key[5] = fives[1]
	
	#finds 6 patterns
	for i in range(len(sixes)):
		x = set(sixes[i])
		y = set(key[5])
		if x.issuperset(y):
			key[6] = sixes[i]
			# print('target 6 identified')
			sixes.pop(i)
			six = set(key[6])
			five = set(key[5])
			botLeft = six.difference(five)
			# print('bottom left is ' + str(botLeft))
			break
	key[0] = sixes[0]
	
	number = ''
	for i in range(len(display)):
		d = set(display[i])
		for x in range(10):
			if d == set(key[x]):
				number += str(x)
				break
	number = int(number)

	return number
	
for i in newlist:
	ans += thealgorithm(i[0],i[1])
print(ans)


#NamingConventionExcuse
