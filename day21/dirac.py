from functools import cache
from itertools import product

scores = [0,0]
positions = [0, 0]
with open("input.txt", "r") as file:
    positions[0] = int(file.readline().strip().split(" ")[-1])
    positions[1] = int(file.readline().strip().split(" ")[-1])

rolls = 0
last_sum = 297
# # Part 1
# def roll(position, score, rolls, last_sum):
#     roll_sum = (last_sum+9)%300
#     last_sum = roll_sum
#     position = (position + roll_sum - 1) % 10 + 1
#     score += position
#     rolls += 3
#     return position, score, rolls, last_sum

# to_win = 1000
# won = 0
# playing = 1

# while won == 0:
#     if playing == 1:
#         positions[0], scores[0], rolls, last_sum = roll(positions[0], scores[0], rolls, last_sum)
#         if scores[0] >= to_win:
#             won = 1
#             break
#     if playing == 2:
#         positions[1], scores[1], rolls, last_sum = roll(positions[1], scores[1], rolls, last_sum)
#         if scores[1] >= to_win:
#             won = 2
#             break
#     playing = 3-playing

# print(won, scores, positions, rolls)
# print(scores[2-won]*rolls)
     
# Part 2
to_win = 21
@cache
def play(p1, p2, p1_score, p2_score, p1_turn):
    wins = [0, 0]
    for p_rolls in product([1,2,3], repeat=3):
        if p1_turn:
            new_pos = (sum(p_rolls)+p1-1) % 10 + 1
            new_p1_score = p1_score + new_pos
            if new_p1_score >= to_win:
                wins[0] += 1
                continue
            outcome = play(new_pos, p2, new_p1_score, p2_score, False)
            wins[0] += outcome[0]
            wins[1] += outcome[1]
        else:
            new_pos = (sum(p_rolls)+p2-1) % 10 + 1
            new_p2_score = p2_score + new_pos
            if new_p2_score >= to_win:
                wins[1] += 1
                continue
            outcome = play(p1, new_pos, p1_score, new_p2_score, True)
            wins[0] += outcome[0]
            wins[1] += outcome[1]
    return wins

print(max(play(positions[0], positions[1], 0, 0, True)))