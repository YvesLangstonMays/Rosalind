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
    in_one = False
    in_two = False
    in_three = False
    while i < len(values[index_value]):
        current_substring = values[index_value][x:i]

        if index_value == 0:
            if current_substring in values[index_value + 1]:
                in_two = True
            if current_substring in values[index_value + 2]:
                in_three = True
        elif index_value == 1:
            if current_substring in values[index_value + 1]:
                if len(current_substring) > len(longest):
                    longest = current_substring
                if current_substring in values[index_value - 1]:
                    in_one = True
        elif index_value == 2:
            if current_substring in values[index_value - 1]:
                in_two = True
                if current_substring in values[index_value - 2]:
                    in_one = True
        else:
            print("Out")
            pass
        if in_one and in_two and in_three:
            longest = current_substring
        i += 1

    index_value += 1
print(f"longest: {longest}")
