inputs = []
outputs = []
uniques = {2:1, 4:4, 3:7, 7:8}
sum = 0
with open("input.txt", "r") as file:
	for line in file: 
		display = ["" for i in range(7)]
		digits = ["" for i in range(10)]
		unknown = []
		input, output = line.split("|")
		input = input.split()
		output = output.split()
		for digit in input:
			if len(digit) in uniques.keys():
				n = uniques[len(digit)]
				digits[n] = digit
			else:
				unknown.append(digit)

		display[0] = digits[7]
		for digit in digits[1]:
			display[0] = display[0].replace(digit, "")
		
		bd = digits[4]
		for digit in digits[1]:
			bd = bd.replace(digit, "")		

		for digit in unknown:
			if len(digit) == 6:
				for i in bd:
					if i not in digit:
						digits[0] = digit
						display[3] = i
				for i in digits[1]:
					if i not in digit:
						digits[6] = digit
						display[2] = i
						display[5] = digits[1].replace(i, "")
				if digit in digits:
					continue
				digits[9] = digit
		for digit in digits:
			unknown.remove(digit) if digit in unknown else None
		x = digits[4]
		y = digits[9]
		z = digits[6]
		not_found = "abcdefg"
		for i in display:
			not_found = not_found.replace(i, "")
			x = x.replace(i, "")
			y = y.replace(i, "")
			z = z.replace(i, "")
		display[1] = x
		display[6] = y.replace(x, "")
		display[4] = z.replace(x, "").replace(display[6], "")
		for digit in unknown:
			if display[4] in digit:
				digits[2] = digit
			elif display[2] in digit and display[5] in digit:
				digits[3] = digit
			else:
				digits[5] = digit
		
		number = ""
		for digit in output:
			for i in digits:
				if len(i) != len(digit):
					continue
				dig = digit
				for j in i:
					dig = dig.replace(j, "")
				if len(dig) == 0:
					number += str(digits.index(i))
					
		sum += int(number)

print(sum)
