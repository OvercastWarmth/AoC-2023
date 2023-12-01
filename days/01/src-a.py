from sys import argv

with open(argv[1]) as f:
	input = f.readlines()

value = []

for line in input:

	numerals = None

	for char in line:
		if char.isnumeric():
			if numerals is None:
				numerals = [char, char]
			else:
				numerals[1] = char

	value.append(int(numerals[0] + numerals[1]))

print(sum(value))