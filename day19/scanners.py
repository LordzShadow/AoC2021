from collections import Counter
import itertools

scanners = []

with open("input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            continue
        elif line[:3] == "---":
            scanners.append([])
        else:
            beacon = [x, y, z] = tuple(map(int, line.strip().split(",")))
            scanners[-1].append(beacon)

translations = [(dimension, invert) for invert in [1, -1] for dimension in range(3)]

""" 
    I match only for one dimension at a time because someone on reddit told so
    and it really made it easier :)                                 
"""
def try_overlap(aligned_s, candidate_s):
    res = [] # shifted beacons
    shift = [] # candidate shift from 0,0,0 (aka scanner 0)
    checked_dim = set() # already checked dimension values
    # go through x y and z
    for dimension in range(3):
        # Get aligned scanner's beacons' dimension values
        a = [pos[dimension] for pos in aligned_s]
        # go through translations for candidate for one dimension
        for (dim_b, invert) in translations:
            if dim_b in checked_dim:
                continue
            b = [pos[dim_b]*invert for pos in candidate_s] # candidate scanner's beacons' dimension values
            dists = [last-first for (first, last) in itertools.product(a, b)] # Find the distaces from scanner to maybe a scanner with beacons
            counter = Counter(dists).most_common(1) # get the most common distance aka our correct distance between beacons if more than 12
            if counter[0][1] >= 12:
                break
        # If not enough overlaps,return -> no overlap between these two.
        if counter[0][1] < 12:
            return None
        checked_dim.add(dim_b)
        res.append([x - counter[0][0] for x in b]) # calculate shifted beacon values (pos[dim] - shift[dim])
        shift.append(-counter[0][0])
    # beacons and scanner pos from 0,0,0
    return (list(zip(res[0], res[1], res[2])), shift)

finished = set()
nextup = [scanners[0]]
todo = scanners[1:]
pos_shifts = [(0,0,0)]
while nextup:
    positioned = nextup.pop()
    temp = []
    for candidate in todo:
        res = try_overlap(positioned, candidate)
        if res:
            (updated, shift) = res
            pos_shifts.append(tuple(shift))
            nextup.append(updated)
        else:
            temp.append(candidate)
    todo = temp
    finished.update(positioned)

print(len(finished))

max_distance = 0
for i in range(len(pos_shifts)):
    for j in range(i + 1, len(pos_shifts)): 
        distance = abs(pos_shifts[i][0] - pos_shifts[j][0])
        distance += abs(pos_shifts[i][1] - pos_shifts[j][1])
        distance += abs(pos_shifts[i][2] - pos_shifts[j][2])
        max_distance = max(max_distance, distance)
print(max_distance)



                

