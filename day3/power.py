gamma = 0
epsilon = 0

with open("input.txt", "r") as file:
	gamma_binary = ''
	epsilon_binary = ''
	lines = file.readlines()
	for i in range(len(lines[0].strip())):
		ones = 0
		zeroes = 0
		for line in lines:
			if line[i] == '0':
				zeroes += 1
			elif line[i] == '1':
				ones += 1
		if ones > zeroes:
			gamma_binary += '1'
			epsilon_binary += '0'
		else:
			gamma_binary += '0'
			epsilon_binary += '1'
	
	gamma = int(gamma_binary, 2)
	epsilon = int(epsilon_binary, 2)


print(gamma * epsilon)	
