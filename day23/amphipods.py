from heapq import *

board = [".",".", "", ".", "", ".", "", ".", "", ".", "."]

# Part 1: input.txt, Part 2: input2.txt
with open("input2.txt", "r") as file:
    for line in file.readlines()[2:]:
        if line.strip().startswith("####"):
            continue
        room = 0
        if line.startswith("###"):
            line = line[2:]
        for char in line.strip():
            if char == "#":
                room += 2
            else:
                board[room] += char

costs = {"A": 1, "B":10, "C":100, "D": 1000}
dests = {"A": 2, "B": 4, "C": 6, "D": 8}
destIdx = set(dests.values())

def canReach(a, b, board):
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end+1):
        if i == a:
            continue
        if i in destIdx:
            continue
        if board[i] != '.':
            return False
    return True

def getC(room):
    for c in room:
        if c != ".":
            return c

def addRoom(c, room):
    room = list(room)
    d = room.count(".")
    assert d != 0
    room[d-1] = c
    return "".join(room), d

def checkRoom(board: list[str], c, dest):
    roomVals = board[dest]
    return roomVals.count(".") + roomVals.count(c) == len(roomVals)

def possibleMoves(board, pos):
    space = board[pos]
    if pos not in destIdx:
        if canReach(pos, dests[space], board) and checkRoom(board, space, dests[space]):
            return [dests[space]]
        return []
    
    letter = getC(space)
    if pos == dests[letter] and checkRoom(board, letter, pos):
        return []

    possible = []
    for dest in range(len(board)):
        if dest == pos or (dest in destIdx and dests[letter] != dest):
            continue
        if dests[letter] == dest:
            if not checkRoom(board, letter, dest):
                continue
        if canReach(pos, dest, board):
            possible.append(dest)
    return possible

def move(board, pos, dest):
    new_board = board[:]
    distance = 0
    letter = getC(board[pos])
    if len(board[pos]) == 1:
        new_board[pos] = "."
    else:
        new_room = ""
        for idx, c in enumerate(board[pos]):
            distance += 1
            if c == ".":
                new_room += c
            else:
                new_room += "." + board[pos][idx+1:]
                break
        new_board[pos] = new_room
    
    distance += abs(pos-dest)

    if len(board[dest]) == 1:
        new_board[dest] = letter
        return new_board, distance*costs[letter]
    else:
        new_board[dest], add_distance = addRoom(letter, board[dest])
        distance += add_distance
        return new_board, distance*costs[letter]

# Kinda looks like dijkstra but it isn't? idk if you would call it that. maybe. Basically. Yes? No...
def solve(board):
    states = {tuple(board): 0}
    q = [board]
    while q:
        board = q.pop()
        for pos, room in enumerate(board):
            if getC(room) is None:
                continue
            moves = possibleMoves(board, pos)
            for m in moves:
                new_board, move_cost = move(board, pos, m)
                new_cost = states[tuple(board)] + move_cost
                new_board_t = tuple(new_board)
                cost = states.get(new_board_t, float('inf'))
                if new_cost < cost:
                    states[new_board_t] = new_cost
                    q.append(new_board)
    return states

gates = {2: "A", 4: "B", 6: "C", 8: "D"}
solved_board = tuple(['.' if i not in gates.keys() else gates[i]*len(board[2]) for i in range(len(board))])
states = solve(board)
print(states[solved_board])
