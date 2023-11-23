seq = []


def getSeq():
    with open("RestrictionSites.txt", "r") as RS:
        for line in RS:
            line = line.split("\n")
            line = list(filter(None, line))
            for index in line:
                seq.append(index)

    s = ""
    for item in seq:
        if item[0] == ">":
            pass
        else:
            s += item

    return s


def complement(seq):
    complement = {"A": "T", "C": "G", "T": "A", "G": "C"}
    bases = list(seq)
    bases = [complement[base] for base in bases]
    bases = bases[::-1]
    comp = "".join(bases)
    return comp


def restrictionSites():
    size = 4
    s = getSeq()
    lengthof = len(s)
    reverse_palin_list = []
    complemented = complement(s)

    while size < len(complemented):
        x = 0
        y = size
        for_y = len(s)
        for_x = for_y - size
        while y < len(complemented) + 1:
            forward = s[for_x:for_y]
            rev = complemented[x:y]

            # print(f"3' {rev} 5' <-> 5' {forward[::-1]} 3'  Length: {size}\n")

            if rev == forward[::1]:
                reverse_palin_list.append([for_x + 1, size, forward, rev])

            for_x -= 1
            for_y -= 1
            x += 1
            y += 1

        size += 1
    reverse_palin_list.sort()
    finalList = []
    for item in reverse_palin_list:
        format = str(abs(item[0])), str(item[1])
        finalList.append(" ".join(format))

    for item in finalList:
        print(item)


restrictionSites()
