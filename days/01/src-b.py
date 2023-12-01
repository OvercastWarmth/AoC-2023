from sys import argv

with open(argv[1]) as f:
	input = f.readlines()

MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


values = []

for line in input:

	numerals = None
	for i, char in enumerate(line):
		if char.isnumeric():
			if numerals is None:
				numerals = [(char, i), (char, i)]
			else:
				numerals[1] = (char, i)

	words = None
	for word in list(MAP.keys()):
		start_index = 0
		while True:
			result_index = line.find(word, start_index)
			if result_index == -1: break
			if words is None: words = [(MAP[word], start_index), (MAP[word], start_index)]
			else: words[1] = (MAP[word], start_index)
			start_index += len(word)
			print(start_index)

	print(numerals, words)

	if numerals is None:
		values.append(int(words[0][0] + words[1][0]))
	elif words is None:
		values.append(int(numerals[0][0] + numerals[1][0]))
	else:
		values.append(int(
			(numerals[0][0] if numerals[0][1] < words[0][1] else words[0][0]) +
			(numerals[1][0] if numerals[1][1] > words[1][1] else words[1][0])
		))

print(values)
print(sum(values))