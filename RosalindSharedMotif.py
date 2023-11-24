seqString = ""
seqDict = {}
with open("SharedMotif.txt", "r") as SM:
    for line in SM:
        print(line)
        line = line.split("\n")
        line = "".join(line)


print(seqDict)
