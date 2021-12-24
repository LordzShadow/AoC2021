# THIS PROGRAM ONLY CHECKS THE SOLUTIONS. THE ACTUAL SOLUTION PART IS IN MATH.MD

from math import trunc
from copy import deepcopy
vars = {"x": 0, "y": 0, "z": 0, "w": 0}
def inp(var:str, val:int=None):
    if val == None:
        val = int(input())
    vars[var] = val

def add(a:str, b):
    if isinstance(b, int):
        inp(a, vars[a]+b)
    else:
        inp(a, vars[a]+vars[b])

def mul(a:str, b):
    if isinstance(b, int):
        inp(a, vars[a]*b)
    else:
        inp(a, vars[a]*vars[b])

def div(a:str, b):
    assert b != 0
    if isinstance(b, int):
        inp(a, trunc(vars[a]/b))
    else:
        inp(a, trunc(vars[a]/vars[b]))

def mod(a:str, b):
    assert vars[a] >= 0 and b > 0
    if isinstance(b, int):
        inp(a, vars[a]%b)
    else:
        inp(a, vars[a]%vars[b])

def eql(a:str, b):
    if isinstance(b, int):
        inp(a, 1 if vars[a] == b else 0)
    else:
        inp(a, 1 if vars[a] == vars[b] else 0)

def run(instr, digit):
    idx = 0
    for i in deepcopy(instr):
        command, params = i
        if command == "inp":
            params.append(int(str(digit)[idx]))
            idx += 1 
        globals()[command](params[0], params[1] if len(params) >= 2 else None)
    return vars["z"] == 0


instructions = []
with open("input.txt", "r") as file:
    for line in file:
        command, params = line.strip().split(maxsplit=1)
        params = params.split()
        if len(params) == 2 and params[1].lstrip("-").isdigit():
            params[1] = int(params[1])
        instructions.append([command, params])
print(run(instructions, 94992994195998))
vars = {"x": 0, "y": 0, "z": 0, "w": 0}
print(run(instructions, 21191861151161))
print(vars)