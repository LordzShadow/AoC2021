def get_coords(string:str):
    splitted = string.split("..")
    return (int(splitted[0].split("=")[1]), int(splitted[1]))

def get_dim_overlap(min1, max1, min2, max2):
    return [max(min1, min2), min(max1, max2)]

def volume(b):
    return (b[0][1]-b[0][0]+1)*(b[1][1]-b[1][0]+1)*(b[2][1]-b[2][0]+1)

def get_overlap(box, rest:list):
    res = 0
    for idx, b in enumerate(rest):
        x = get_dim_overlap(box[0][0], box[0][1], b[0][0], b[0][1])
        y = get_dim_overlap(box[1][0], box[1][1], b[1][0], b[1][1])
        z = get_dim_overlap(box[2][0], box[2][1], b[2][0], b[2][1])
        if x[1] - x[0] >= 0 and y[1] - y[0] >= 0 and z[1] - z[0] >= 0:
            overlap_box = [x, y, z]
            res += volume(overlap_box) - get_overlap(overlap_box, rest[idx+1:])
    return res

instr = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        box = tuple(map(get_coords, line[1].split(",")))
        c = line[0]
        instr.append([c, box])

on = 0
boxes = []
instr.reverse()
for i in instr:
    box = i[1]
    # Part 1
    # if abs(box[0][0]) > 50 or abs(box[1][0]) > 50 or abs(box[2][0]) > 50:
    #     continue
    if i[0] == "on":
        on += volume(box) - get_overlap(box, boxes)
    boxes.append(box)

print(on)