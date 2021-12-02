pos = 0
d = 0

# Part 1
with open("input.txt", "r", encoding="utf-8") as file:
	for line in file:
		c, n = line.strip().split(" ")
		n = int(n)
		if c == "forward":
               		pos += n
		elif c == "up":
                	d -= n
		elif c == "down":
                	d += n

print(pos*d)

pos = 0
d = 0
aim = 0

# Part 2
with open("input.txt", "r", encoding="utf-8") as file:
	for line in file:
		c, n = line.strip().split(" ")
		n = int(n)
		if c == "forward":
			pos += n
			d += aim*n
		elif c == "up":
			aim -= n
		elif c == "down":
			aim += n

print(pos*d)
