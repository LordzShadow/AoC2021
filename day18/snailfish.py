
from math import ceil, floor
import json
lines = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

def add(a, b):
    return "[" + a + "," + b + "]"

def get_number(string, idx):
    nr = ""
    while 1:
        if string[idx].isdigit():
            nr += string[idx]
            idx += 1
        else:
            break
    return int(nr)
            

def explode(line: str):
    n = 0
    last_idx = None
    explode_right = False
    explode = False
    add_value = None
    pair_starts = []
    idx = 0
    while idx < len(line):
        char = line[idx]
        if char == "[":
            pair_starts.append(idx)
        if char == "]":
            start_idx = pair_starts.pop()
            if explode:
                line = line[:start_idx] + "0" + line[idx+1:]
                idx = len(line[:start_idx] + "0")
                last_idx = [len(line[:start_idx]), len(line[:start_idx] + "0")]
                explode = False
            else:
                idx = idx+1
            continue
        n = len(pair_starts)
        if char.isdigit():
            number = get_number(line, idx)
            if add_value:
                line = line[:idx] + str(number + add_value) + line[idx+len(str(number)):]
                number = number+add_value
                add_value = None
            if n == 5:
                explode = True
                if not explode_right:
                    explode_right = True
                    if last_idx:
                        to_nr = len(line[last_idx[1]:idx])
                        idx = len(line[:last_idx[0]] + str(int(line[last_idx[0]: last_idx[1]]) + number)) + to_nr + 1
                        for i in range(len(pair_starts)):
                            if pair_starts[i] > last_idx[0] and len(line[last_idx[0]: last_idx[1]]) != len(str(int(line[last_idx[0]: last_idx[1]]) + number)):
                                pair_starts[i] += len(str(int(line[last_idx[0]: last_idx[1]]) + number))-1
                        line = line[:last_idx[0]] + str(int(line[last_idx[0]: last_idx[1]]) + number) + line[last_idx[1]:]
                else:
                    add_value = number
                    explode_right = False
                    idx = idx + len(str(number))
                    continue
            else:
                explode = False
            if not explode:
                last_idx = [idx, idx + len(str(number))]
            idx = idx + len(str(number))
            continue
        idx += 1
    return line

def split(line: str):
    idx = 0
    while idx < len(line):
        char = line[idx]
        if char.isdigit():
            number = get_number(line, idx)
            if number >= 10:
                nr_len = len(str(number))
                line = line[:idx] + "[" + str(floor(number/2)) + "," + str(ceil(number/2)) + "]" + line[idx+nr_len:]
                break
        idx += 1
    return line

def magnitude(pair):
    a = pair[0]
    b = pair[1]
    mag = 0
    if isinstance(a, int):
        mag += 3*a
    else:
        mag += 3*magnitude(a)
    if isinstance(b, int):
        mag += 2*b
    else:
        mag += 2*magnitude(b)
    return mag

# Part 1
newline = lines[0]
for i in range(1, len(lines)):
    newline = add(newline, lines[i])
    while True:
        a = explode(newline)
        a = split(a)
        if a != newline:
            newline = a
        else:
            break
print(magnitude(json.loads(newline)))

# Part 2
biggest_magnitude = -1
for i in range(0, len(lines)):
    for j in range(0, len(lines)):
        if i == j:
            continue
        line = add(lines[i], lines[j])
        while True:
            a = explode(line)
            a = split(a)
            if a != line:
                line = a
            else:
                break
        mag = magnitude(json.loads(line))
        if mag > biggest_magnitude:
            biggest_magnitude = mag

print(biggest_magnitude)
        
# This code is a mess and we are not gonna talk about it. But I finally solved it.

