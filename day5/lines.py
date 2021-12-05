points = set()
atleast_2 = set()

def add_point(x, y):
	point = str(x) + "," + str(y)
	if point in points:
		atleast_2.add(point)
	else:
		points.add(point)

with open("input.txt", "r") as file:
	for line in file:
		x1, y1 = list(map(int, line.strip().split()[0].split(",")))
		x2, y2 = list(map(int, line.strip().split()[2].split(",")))
		# Part 1, vertical
		if x1 == x2:
			step = -1 if y1 > y2 else 1
			for y in range(y1, y2+step, step):
				add_point(x1, y)
		# Part 1, horizontal
		elif y1 == y2:
			step = -1 if x1 > x2 else 1
			for x in range(x1, x2+step, step):
				add_point(x, y1)
		# Part 2, diagonal
		else:
			delta = abs(x2-x1)
			d_y = -1 if y1 > y2 else 1
			d_x = -1 if x1 > x2 else 1
					
			for i in range(delta+1):
				add_point(x1+(i*d_x), y1+(i*d_y))

print(len(atleast_2))	



