
n = 0

#PART1
with open("input.txt", "r") as file:
	lines = file.readlines();
	for i in range(len(lines)-1):
		d_a, d_b = list(map(int, lines[i:i+2]))
		n += 1 if d_b > d_a else 0

print(n)

n = 0

#PART2
with open("input.txt", "r") as file:
	lines = file.readlines()
	for i in range(len(lines)-3):
		d_a = lines[i:i+3]
		d_b = lines[i+1:i+4]
		d_a = list(map(int, d_a))
		d_b = list(map(int, d_b))
		if (sum(d_b) > sum(d_a)):
			n += 1

print(n)
					
