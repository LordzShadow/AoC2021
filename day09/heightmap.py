import math
low_points = []
hmap = []
basins = []
used = set()

def compare(point1, point2):
	if point1 >= point2:
		return False
	return True

# Part 2 basically
def find_basin(point, i, j):
	if point == 9 or str(i)+str(j) in used:
		return 0
	sum = 1
	used.add(str(i)+str(j))
	if i > 0 and hmap[i-1][j] > point:
		sum += find_basin(hmap[i-1][j], i-1, j)
	if i < len(hmap)-1 and hmap[i+1][j] > point:
		sum += find_basin(hmap[i+1][j], i+1, j)
	if j > 0 and hmap[i][j-1] > point:
		sum += find_basin(hmap[i][j-1], i, j-1)
	if j < len(hmap[i])-1 and hmap[i][j+1] > point:
		sum += find_basin(hmap[i][j+1], i, j+1)
	return sum
	

with open("input.txt", "r") as file:
	for line in file:
		points = list(map(int, list(line.strip())))
		hmap.append(points)

for i in range(len(hmap)):
	for j in range(len(hmap[i])):
		point = hmap[i][j]
		low = True
		if i > 0:
			low = compare(point, hmap[i-1][j])
		if i < len(hmap)-1 and low:
			low = compare(point,hmap[i+1][j])		 
		if j > 0 and low:
			low = compare(point, hmap[i][j-1])
		if j < len(hmap[i])-1 and low:
			low = compare(point, hmap[i][j+1])
		if low:
			low_points.append(point)
			basin = find_basin(point, i, j)
			basins.append(basin)

print(sum(low_points)+len(low_points))
print(math.prod(sorted(basins, reverse=True)[:3]))
