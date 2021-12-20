
image = []
alg = ""

with open("input.txt", "r") as file:
    alg = file.readline().strip()
    for line in file.readlines()[1:]:
        image.append([a for a in line.strip()])

def prettyprint(img):
    for line in img:
        print(line)
    print()

def enhance(map, inf_val):
    new_map = [[inf_val for i in range(-1,len(map[0])+1)]]
    [new_map.append([inf_val] + map[i] + [inf_val]) for i in range(len(map))]
    new_map.append([inf_val for i in range(-1,len(map[0])+1)])
    h = len(map)
    for i in range(-1, h+1):
        w = len(map[0])
        for j in range(-1, w+1):
            new_val = ""
            for y in range(i-1, i+2):
                for x in range(j-1, j+2):
                    if 0 <= x < w and 0 <= y < h:
                        new_val += map[y][x]
                    else:
                        new_val += inf_val
            new_val = "".join(["0" if v == "." else "1" for v in new_val])
            new_map[i+1][j+1] = alg[int(new_val, 2)]
    idx = "".join(["0" if v == "." else "1" for v in inf_val*9])
    return (new_map, int(idx, 2))

# Part 1 n = 2
n = 50
(image, inf_idx) = enhance(image, ".")
for i in range(n-1):
    (image, inf_idx) = enhance(image, alg[inf_idx])
pixels = 0
for line in image:
    for char in line:
        if char == "#":
          pixels += 1
print(pixels)  

