right = set()
down = set()
board = ()
with open("input.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            coord = str(j)+"|"+str(i)
            match char:
                case ">":
                    right.add(coord)
                case "v":
                    down.add(coord)
                case _:
                    continue
    board = (j+1, i+1)

def pretty(r, d):
    for i in range(board[1]):
        for j in range(board[0]):
            if str(j)+str(i) in r:
                print(">", end="")
            elif str(j)+str(i) in d:
                print("v", end="")
            else:
                print(".", end="")
        print()
    print()

def step(r,d, n):
    new_r = set()
    new_d = set()
    changed = False
    for i in r:
        coords = list(map(int, i.split("|")))
        n_coords = str(coords[0]+1 if coords[0]+1 < board[0] else 0)+"|"+str(coords[1])
        if n_coords in d or n_coords in r:
            new_r.add(i)
        else:
            new_r.add(n_coords)
            changed = True
    for i in d:
        coords = list(map(int, i.split("|")))
        n_coords = str(coords[0])+"|"+str(coords[1]+1 if coords[1]+1 < board[1] else 0)
        if n_coords in d or n_coords in new_r:
            new_d.add(i)
        else:
            new_d.add(n_coords)
            changed = True
    if changed:
        return step(new_r, new_d, n+1)
    else:
        return n

print(step(right, down, 1))
