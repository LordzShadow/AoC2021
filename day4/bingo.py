numbers = []
# {board: [], last_number: int, won_at: int}
boards = []
boards_i = 0

def checkForWin(board):
	for i in range(len(board)):
		if set(board[i]) == set(["*"]):
			return True
	for i in range(len(board[0])):
		found = 0
		for j in range(len(board)):
			if board[j][i] == "*":
				found += 1
		if found == len(board):
			return True
	return False 

def calculate(board, last):
	value = 0
	for line in board:
		for number in line:
			if number.isnumeric():
				value += int(number)
	print(value, last)
	return value * int(last)		

with open("input.txt", "r") as file:
	numbers = file.readline().strip().split(",")
	for line in file.readlines():
		line = line.strip()
		if line == "":
			boards.append({"board": [], "last_number": None, "won_at": None})
		else:
			line = line.split()
			boards[-1]["board"].append(line)
	boards_i = len(boards)
	for n in range(boards_i): 
		for (idx, number) in enumerate(numbers):
			for k in range(len(boards[n]["board"])):
				for (j, x) in enumerate(boards[n]["board"][k]):
					if x == number:
						boards[n]["board"][k][j] = "*"
						boards[n]["last_number"] = number
					
			if checkForWin(boards[n]["board"]):
				boards[n]["won_at"] = idx
				break

# Part 1
win_board = {}
won_at = len(numbers)
for i in range(boards_i):
	if boards[i]["won_at"] <= won_at:
		won_at = boards[i]["won_at"]
		win_board = boards[i]

print(calculate(win_board["board"], win_board["last_number"]))

# Part 2
lose_board = {}
won_at = 0
for i in range(boards_i):
        if boards[i]["won_at"] >= won_at:
                won_at = boards[i]["won_at"]
                lose_board = boards[i]

print(calculate(lose_board["board"], lose_board["last_number"]))

