#AdventOfCode_Day_Two

#part_one

readvar = open('input', 'r')
ISL = readvar.read().split('\n')
ITL = [loopName.split(' ') for loopName in ISL]
netUp = 0
netDown = 0
netForward = 0
for nameforLoop in ITL:
	if nameforLoop[0] == 'up':
		netUp += int(nameforLoop[1])
	elif nameforLoop[0] == 'down':
		netDown += int(nameforLoop[1])
	else:
		netForward += int(nameforLoop[1])

netDepth = netDown - netUp
answer = netDepth * netForward
print('Totals\n\n-Up = ' + str(netUp) + '\n-Down = ' + str(netDown) + '\n-Forward = ' + str(netForward) + '\n-Depth = ' + str(netDepth) + '\n\n-Answer = ' + str(answer))

#part_two

readvar = open('input', 'r')
ISL = readvar.read().split('\n')
ITL = [loopName.split(' ') for loopName in ISL]
netUp = 0
netAim = 0
netDown = 0
netForward = 0
for nameforLoop in ITL:
	if nameforLoop[0] == 'up':
		netAim -= int(nameforLoop[1])
	elif nameforLoop[0] == 'down':
		netAim += int(nameforLoop[1])
	else:
		netForward += int(nameforLoop[1])
		extraDown = netAim * int(nameforLoop[1])
		netDown += extraDown

netDepth = netDown - netUp
answer = netDepth * netForward
print('Totals\n\n-Up = ' + str(netUp) + '\n-Down = ' + str(netDown) + '\n-Forward = ' + str(netForward) + '\n-Depth = ' + str(netDepth) + '\n\n-Answer = ' + str(answer))

#NamingConventionExcuse
