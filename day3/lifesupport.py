generator = 0
scrubber = 0

def find_next(bin, line, one, zero):
	if line.startswith(bin + '1'):
		return [one+1, zero]
	elif line.startswith(bin + '0'):
		return [one, zero+1]
	else:
		return [one, zero]	

with open("input.txt", "r") as file:
	lines = file.readlines()
	gen_bin, scrub_bin = ["", ""]
	for i in range(1, len(lines[0].strip())+1):
		g_ones, g_zeroes, s_ones, s_zeroes = [0,0,0,0]
		for line in lines:
			g_ones, g_zeroes = find_next(gen_bin, line, g_ones, g_zeroes)
			s_ones, s_zeroes = find_next(scrub_bin, line, s_ones, s_zeroes)		
		if s_zeroes + s_ones == 1:
			scrub_bin += '1' if s_ones > s_zeroes else '0'
		else:
			scrub_bin += '0' if s_zeroes <= s_ones else '1'
		gen_bin += '1' if g_ones >= g_zeroes else '0'
	generator = int(gen_bin, 2)
	scrubber = int(scrub_bin, 2)

print(generator*scrubber)
