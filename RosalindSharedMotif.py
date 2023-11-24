seq = {}
currentLine = None

with open("SharedMotif.txt", "r") as SM:
    for line in SM:
        line = line.split("\n")
        line = list(filter(None, line))

        if line[0][0] == ">":
            currentLine = line[0]
            pass
        else:
            seq[currentLine] = line[0]

values = []
for key in seq:
    values.append(seq[key])


x = 0
index_value = 0
longest = ""

while index_value < len(values):
    i = 0
    while i < len(values[index_value]):
        current_substring = values[index_value][x:i]
        print(current_substring)

        if index_value == 0:
            if current_substring in values[index_value + 1]:
                if len(current_substring) > len(longest):
                    longest = current_substring
            elif current_substring in values[index_value + 2]:
                if len(current_substring) > len(longest):
                    longest = current_substring
        elif index_value == 1:
            if index_value == 0:
                if current_substring in values[index_value + 1]:
                    if len(current_substring) > len(longest):
                        longest = current_substring
        elif index_value > 2:
            if current_substring in values[index_value - 1]:
                if len(current_substring) > len(longest):
                    longest = current_substring
        else:
            print("Out")
            pass
        i += 1

    index_value += 1
print(longest)
