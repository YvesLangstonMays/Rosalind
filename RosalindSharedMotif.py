currentLine = None
seqString = ""
seqDict = {}
with open("SharedMotif.txt", "r") as SM:
    sequence = ""
    sequenceCount = 0
    for line in SM:
        line = line.split("\n")
        line = "".join(line)
        if line[0] == ">":
            currentLine = line
            if not seqDict:
                pass
            else:
                seqDict[currentLine] = seqString
        else:
            seqString += line
print(seqDict)
