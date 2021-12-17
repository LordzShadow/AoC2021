xr, yr = [], []
with open("input.txt", "r") as file:
    line = file.readline().strip().split(",")
    xr = list(map(int, line[0].split("=")[1].split("..")))
    yr = list(map(int, line[1].split("=")[1].split("..")))

def step(vx, vy, loc):
    if loc != (0, 0) and (loc[0] > max(xr) and vx > 0) \
        or (loc[0] < min(xr) and vx < 0) or loc[1] < min(yr):
        return False
    if min(xr) <= loc[0] <= max(xr) and min(yr) <= loc[1] <= max(yr):
        return True
    new_loc = (loc[0] + vx, loc[1] + vy)
    new_x = vx + (-vx)//vx if vx != 0 else 0
    new_y = vy-1
    return step(new_x, new_y, new_loc)

highest = 0
velocities = 0
for y in range(abs(min(yr))+1, -(abs(min(yr))+1), -1):
    for x in range(-(abs(max(xr))+1), abs(max(xr))+1):
        targethit = step(x, y, (0, 0))
        if targethit:
            velocities += 1
            if highest < y:
                highest =  y

print(sum([i for i in range(1, highest+1)]))
print(velocities)