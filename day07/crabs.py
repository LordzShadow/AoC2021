crabs = []

def part1(crab, i):
	# difference
	return abs(crab-i)

def part2(crab, i):
	# Sum of series 1..difference  n(1+n)/2
	return (part1(crab, i) * (part1(crab, i) + 1)) // 2

with open("input.txt", "r") as file:
	crabs = list(map(int, file.readline().split(",")))
	minimum = min(crabs)
	maximum = max(crabs)
	values = min([sum([part1(crab, i) for crab in crabs]) for i in range(minimum, maximum+1)])
	print(values)
	values = min([sum([part2(crab, i) for crab in crabs]) for i in range(minimum, maximum+1)])
	print(values)
