#AdventOfCode_Day_Three

#part_one

PC = 0
GRS = ''
ERS = ''

readvar = open('input', 'r')
binlib = readvar.read().split('\n')

for fore in range(len(binlib[0])): # 0 - 12
	ones = 0
	zeds = 0
	for four in range(len(binlib)): # number of listings
		if binlib[four][fore] == '1':
			ones += 1
		else:
			zeds += 1
	if ones > zeds:
		GRS += '1'
		ERS += '0'
	else:
		GRS += '0'
		ERS += '1'
GR = int(GRS, 2)
ER = int(ERS, 2)
PC = GR * ER
print('PC = ' + str(PC))
print(GRS)
print(ERS)

#part_two

readvar = open('input', 'r')
binlib = readvar.read().split('\n')

OxyGen = 0
ScrubbaDub = 0
LifeSupport = 0
OxyGenList = []
ScrubbaDubList = []
firstPass = True

for bit in range(len(binlib[0])):
	ones = 0
	zeds = 0
	notOnes = 0
	notZeds = 0
	Common = ''
	if firstPass:
		firstPass = False
		for data in range(len(binlib)):
			if binlib[data][bit] == '1':
				ones += 1
			else:
				zeds += 1
		if ones >= zeds:
			Common = '1'
		else:
			Common = '0'
		for data in range(len(binlib)):
			if binlib[data][bit] == Common:
				OxyGenList.append(binlib[data])
			else:
				ScrubbaDubList.append(binlib[data])
	else:
		print(bit)
		for data in range(len(OxyGenList)):
			if OxyGenList[data][bit] == '1':
				ones += 1
			else:
				zeds += 1
		if ones >= zeds:
			Common = '1'
		else:
			Common = '0'
		for data in range(len(OxyGenList)-1, -1, -1):
			if OxyGenList[data][bit] != Common:
				OxyGenList.pop(data)
		for data in range(len(ScrubbaDubList)):
			if ScrubbaDubList[data][bit] == '1':
				notOnes += 1
			else:
				notZeds += 1
		if notOnes >= notZeds:
			unCommon = '0'
		else:
			unCommon = '1'
		for data in range(len(ScrubbaDubList)-1, -1, -1):
			if len(ScrubbaDubList) > 1:
				if ScrubbaDubList[data][bit] != unCommon:
					ScrubbaDubList.pop(data)
print(OxyGenList)
print('\n')
print(ScrubbaDubList)
OxyGen = int(OxyGenList[0], 2)
ScrubbaDub = int(ScrubbaDubList[0], 2)
LifeSupport = OxyGen * ScrubbaDub
print('Life Support Rating: ' + str(LifeSupport))

#NamingConventionExcuse
