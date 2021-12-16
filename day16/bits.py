import binascii
import math
binary = ""
with open("input.txt", "r") as file:
    hexline = file.readline().strip()
    for char in hexline:
        binary += bin(int(char, 16))[2:].zfill(4)

version_sum = 0

def get_number(type, numbers):
    if type == 0:
        return sum(numbers)
    if type == 1:
        return math.prod(numbers)
    if type == 2:
        return min(numbers)
    if type == 3:
        return max(numbers)
    if type == 5:
        return 1 if numbers[0] > numbers[1] else 0
    if type == 6:
        return 1 if numbers[0] < numbers[1] else 0
    if type == 7:
        return 1 if numbers[0] == numbers[1] else 0

def decode_bin(string):
    not_parsed = ""
    numbers = []
    global version_sum
    version = int(string[:3], 2)
    version_sum += version
    type = int(string[3:6], 2)
    i = 6
    if type != 4:
        len_type = int(string[6])
        if len_type == 0:
            total_len = int(string[7:7+15],2)
            substring = string[22: 22+total_len]
            while len(substring) > 0:
                number, substring = decode_bin(substring)
                numbers.append(number)
            not_parsed = string[22+total_len:]

        else:
            subpackets = int(string[7:7+11], 2)
            substring = string[18:]
            for p in range(subpackets):
                number, substring = decode_bin(substring)
                numbers.append(number)
            not_parsed = substring
    elif type == 4:
        number = ""
        last = False
        while not last:
            first = string[i]
            last = True if first == "0" else False
            number += str(string[i+1:i+5])
            i += 5
        return (int(number, 2), string[i:])
    
    return (get_number(type, numbers), not_parsed)

print(decode_bin(binary)[0])
print(version_sum)