seqString = ""
seqDict = {}

title = None
current = []


def FASTA_open(file):
    with open(file, "r") as f:
        for line in f:
            if line[0] == ">":
                line = line[1:]
                if len(current) > 0:
                    seqDict[title] = ["".join(item) for item in current]
                    current.clear()
                title = line.replace("\n", "")
                title = "".join(title)
            else:
                line = line.replace("\n", "")
                current.append(line)
    seqDict[title] = [item for item in current]
    current.clear()


FASTA_open("SharedMotif.txt")

testing = []
combined = ""
for key in seqDict:
    testing.append(seqDict[key])


final = []
for item in testing:
    items = []
    for index in item:
        items.append(index)
        new = "".join(items)
    final.append(new)

print(final)


# combinet = ""
# lst = ["A", "B", "C"]
# for i in lst:
#     combinet = combinet + lst[lst.index(i)]
#     print(i)
# print(combinet)


# print(testing)

# for key in seqDict:
#     for item in testing:
#         seqDict[key] = item

# motif = "test"
# shortest_index = testing.index(min(testing, key=len))
# shortest = testing[shortest_index]
# for i in range(len(shortest)):
#     x = 0
#     proceed = True
#     while proceed:
#         for sequence in testing:
#             if shortest[i : i + x] not in sequence or x > 999:
#                 proceed = False
#                 break
#         if proceed:
#             motif = max(shortest[i : i + x], motif, key=len)
#         x += 1

# print(motif)
