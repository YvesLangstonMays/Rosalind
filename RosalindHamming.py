s = "CATATCGCGTCGCCCGATCAACTGATGGTACCCCCTCGCCTGCCAGCCCGGGGCGAAAGTGGCCTGCCGCGCACGAGATATACAACAGACATTGTCTCCGTTTATGGGACACAGGGCTTTTGTAAACATGCACATCCGTCGTCGCAACCGTTACTATTCGATGTTCTGGAGAAGCTAGAGCGCGATGATCGTGGATGTCATCACGCTAGAGGAACCTCGTTTAGTGCCCGGACAGAAAGTCTTTTGCACACCGCATCGCATTGTGAGCCTTCGGAGCCGTGTTAGAAATGGGACAGCATGAATTGCCATATAGCCAGACGGAAAGCGATATACGGTGGTGCGTAAAATGACACCCACATCTGGAAATGTGGGAGCCAGCTGGTATCATTCGCAGTAGGGATGCTTATGAGTCTACGGGGGTGTAAAATATGAAAGCGTTAATGCCATGATGATAGCACTTCCCGGCATGGGATGCGACAGTACGCACTCTCATCCTCTTGACCAGTAACTGTTGGTTTGAGCGTCACTCTACCGACTGCCACCAGCGATTCACTACTTGTAATTTTATGGGTTTCTACTTGTAACAGAGCCAGTGTATTTGCCAAGCTGTCCGCACTCAAGTGTTCAAGACTGGCTGAGGTTAGATCTGTACGGACCAAGTAACCTATTCGCATTGGCTTAACTAGTGGTTACGTGATACCGCAGTGCCATCTCCGGATGTGGCTGAAGTAGAAACGTGTAATGCACCTCACATTTGCTTATCCCGCTGGTCTATTGTGTCACAATAACAAGTGTAGCCGGCTGCAGATGAATCAGGCCGCGTTTAACGGTGTTCGCACTTTTTGATTTAGTCTTGCCCTACAGAGAGAGAAGGCCGCAAATGGGGAGCGATGGAGTGGTGGAGCACTGTATTCCTACGAATAG"
t = "ACCATGGCAATATTGTATCAACTGCCCGTGACGCTTCCCCAGCGAGGCAGAGTCGAATGTAAACTGACACGAGTTATGTGGCGAAGGGTTACGGACACCGATGATGAGATCAAGTGATTTATTAGACGTGTTGATATGACCTTGAACCCCTGAACACTGATTGTAAAGCTGAAGACAGCCCTCCATTCAAGTGGAGGCCAACGACGCAAAGGAGCCCCGTTATGGGAGAAGTCAGTCAGCAATCTTCAAAGCGCAAGCACTACGCAAAACTACGACTCGGTTGTTAATAATCACTGCATGTTGGGCATTATTTAGGGATTAAATGCGAAAAACGGTGGTTGGAGAGTCGACCCACTCATCTCTAATTGGACGACTCACCCGTTACGCGGAGAATCGGGATTAACTTTGTGTCGGCGTCCCAATGATTTGTGAGTCAGCGATTCAGCTCATGATTTCACGTTCCGGCCTGTGGCCGACTAGAGTGTCAGTTCCTTATGTAAGCCAAAAAATGTTTGGATCCAGATCTGCCAAGTGACGGCCACCAGATAAGGACTCATTGGATTTTCACGCATCTCTCCTTGTATGTGAGCAAGCATATCAGCATAAGTGACGGTACTCAATGGATTGAAACCGGCAACTTTCGAACACATAAGCTCAAAGCGTCCAGCCACTTGAGGTCCGACTCGTCGTAAAGTAATAGCACACTTCCAAGTCATTCGGAAGATTAATCGCGATTGACCAAAGCTGGTATCTCTATAGTAACCTGTCAGGCTGTAGGGACGGAGAACGTAGTTCAGGGGGCTCCAGATGAGTGAGTGCGTGCTTGCCGGGGTTCGTTTCCTTCGTTCCGACCTTGCCTACGAGTGAGATTTTCCAGTAAAGAGCGCCTTTTGCAGGGGCTAAGTTGTGTGTTCGTCGGTCTCC"

s = list(s)
t = list(t)

x = 0

hamming = 0
while x < len(s):
    if s[x] == t[x]:
        pass
    else:
        hamming += 1
    x += 1
print(hamming)