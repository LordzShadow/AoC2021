counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
n = 256

with open("input.txt", "r") as file:
	for fish in file.readline().strip().split(","):
		counter[int(fish)] += 1

for i in range(n):
	temp_c = dict(counter)
	for j in range(9):
		if j == 0:
			temp_c[8] += counter[j]
			temp_c[6] += counter[j]
		else:
			temp_c[j-1] += counter[j]
		temp_c[j] -= counter[j]
	counter = dict(temp_c)

sum = 0
for i in range(9):
	sum +=  counter[i]
print(sum)
