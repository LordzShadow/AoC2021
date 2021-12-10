corrupt_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
closing_points = {")": 1, "]": 2, "}": 3, ">": 4}

opened = ["<", "(", "[", "{"]
closed = [">", ")", "]", "}"]

corrupted = []
closing_sums = []

with open("input.txt", "r") as file:
	for line in file:
		line = line.strip()
		openings = []
		for char in list(line):
			if char in opened:
				openings.append(char)
			elif char in closed and closed.index(char) == opened.index(openings.pop()):
				continue
			else:
				corrupted.append(char)
				openings = []
				break
		# Part 2
		sum = 0
		for i in range(len(openings)):
			char = openings.pop()
			closingchar = closed[opened.index(char)]
			sum *= 5
			sum += closing_points[closingchar]
		if sum > 0:
			closing_sums.append(sum)

corrupted_sum = 0
for char in corrupted:
	corrupted_sum += corrupt_points[char]
print(corrupted_sum)

print(sorted(closing_sums)[len(closing_sums)//2])
