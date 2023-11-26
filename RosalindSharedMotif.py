seqString = ""
seqDict = {}

title = None
current = []


def FASTA_open(file):
    with open(file, "r") as f:
        for line in f:
            if line[0] == ">":
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
for item in seqDict:
    print(seqDict[item])
