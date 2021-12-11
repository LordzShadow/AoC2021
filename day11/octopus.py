
n = 100

octopuses = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        octopuses.append([])
        for oct in line:
            octopuses[-1].append(int(oct))

def run(n):
    flashes = 0
    x = 0
    while 1:
        x += 1
        add_energy()
        flashed = set()
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                if octopuses[i][j] > 9 and str(i) + str(j) not in flashed:
                    flashed  = flash(i, j, flashed)
        if x <= n:
            flashes += len(flashed)
        # Part 2
        if len(flashed) == len(octopuses)*len(octopuses[0]):
            print(x)
            break
    print(flashes)

def add_energy():
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1

def flash(i, j, flashed):
    octopuses[i][j] = 0
    flashed.add(str(i) + str(j))
    i_max = min(i+2, len(octopuses))
    j_max = min(j+2, len(octopuses[0]))
    for i_n in range(max(0, i-1), i_max):
        for j_n in range(max(0, j-1), j_max):
                if str(i_n) + str(j_n) in flashed:
                    continue
                else:
                    octopuses[i_n][j_n] += 1
                    if octopuses[i_n][j_n] > 9:
                        flashed = flash(i_n, j_n, flashed)
    return flashed

run(n)
                    

