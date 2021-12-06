
fishies = []
n = 80

def update(fish):
	if fish == 0:
		return 6
	else:
		return fish-1

with open("input.txt", "r") as file:
	fishies = list(map(int, file.readline.strip().split()))

for i in range(n):

