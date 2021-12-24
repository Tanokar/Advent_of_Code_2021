#AdventOfCode_Day_Six

#part_one

readvar = open('LanternFish', 'r')
Stringfish = readvar.read().split(',')
fish = []
for i in range(len(Stringfish)):
	fish.append(int(Stringfish[i]))

def dayPass(fishList):
	Days = int(input('Days?: '))
	Flist = fishList.copy()
	for num in range(Days):
		for fish in range(len(Flist)):
			if Flist[fish] == 0:
				Flist[fish] = 6
				Flist.append(8)
			else:
				Flist[fish] -= 1
	return len(Flist)
print(dayPass(fish))
print(len(fish))


#part_two

FIDL = [0,0,0,0,0,0,0,0,0,]

for i in fish:
	if i == 1:
		FIDL[1] += 1
	if i == 2:
		FIDL[2] += 1
	if i == 3:
		FIDL[3] += 1
	if i == 4:
		FIDL[4] += 1
	if i == 5:
		FIDL[5] += 1
	if i == 6:
		FIDL[6] += 1

def life(fiddle):
	Days = int(input('Days?:'))
	Flist = fiddle.copy()
	for day in range(Days):
		Babies = Flist[0]
		Flist[0] = Flist[1]
		Flist[1] = Flist[2]
		Flist[2] = Flist[3]
		Flist[3] = Flist[4]
		Flist[4] = Flist[5]
		Flist[5] = Flist[6]
		Flist[6] = Flist[7] + Babies
		Flist[7] = Flist[8]
		Flist[8] = Babies
	return Flist[0] + Flist[1] + Flist[2] + Flist[3] + Flist[4] + Flist[5] + Flist[6] + Flist[7] + Flist[8]


print(life(FIDL))



#NamingConventionExcuse
