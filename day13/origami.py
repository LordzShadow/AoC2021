
paper = []
folds = []
with open("input.txt", "r") as file:
    folding = False
    for line in file:
        if len(line.strip()) == 0:
            folding = True
            continue
        if folding:
            fold = tuple(line.split(" ")[2].split("="))
            folds.append(fold)
        else:
            x, y =  list(map(int, line.strip().split(",")))
            y_max = len(paper)
            x_max = len(paper[0]) if len(paper) > 0 else 0
            if y >= y_max:
                for i in range(y-y_max+1):
                    length = len(paper[0]) if len(paper) > 0 else 0
                    p = ["." for i in range(length)]
                    paper.append(p)
            if x >= x_max:
                for p in range(len(paper)):
                    [paper[p].append(".") for i in range(x-x_max+1)]
            paper[y][x] = "#"

def foldit(f):
    global paper
    c = int(f[1])
    if f[0] == "y":
        for y in range(c+1, len(paper)):
            new_y = c-(y-c)
            for x in range(len(paper[y])):
                if paper[y][x] == "#":
                    paper[new_y][x] = "#"
        paper = paper[:c]
    else:
        for y in range(len(paper)):
            for x in range(c+1, len(paper[y])):
                new_x = c-(x-c)
                if paper[y][x] == "#":
                    paper[y][new_x] = "#"
            paper[y] = paper[y][:c]




for fold in folds:
    foldit(fold)

for line in paper:
    print(line)
