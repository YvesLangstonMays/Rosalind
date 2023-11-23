# Problem 1
# s = "ATTAACCTTAAGAAGGTGGAAATTGCGGGTTAGGAAGGAGACAGGTTCATGCACTGTTCTGAACAACCTGAAAGCTAACGAAGACCGTCCATCGTCGAGGTACGATCGGACGTGTTTTCCCGTAGATGAAAATGCCGGTGAGCTGTAGTTCACTCAGCATTATCCAATTCAGACTTGCTGTACGGAGCCCCGCGAAGCCGAGTAGGGGCAGTAGCGCCACGCTTACTGGATATCATCACCAAAGATTAACATTCTACTCACGTACACCGGAAGCTGTAGGTGAGAATATACCCAACCTTAAGACCAGATACTTGTTACGAGACATATTTCATAATCACAGGGAGCTTACCTGTAAATATGAGAATTACTTAAAGTCGGTCATCAGTCCTGAAAACATTACAGAGGGATAGCGGTCGACGCTCCAGGCCTTCTTCAGCGCGCTGGAGCGGGAAGACATAGATGATCTCGCCGAGGGAGACTCGGTTTCCCAGACTGTCACGAATTTTAAGTCTGACTCCCCGGCCGCAGTTCCGCAGACAAGAAAAGGTCAATGAACCTTGAATCGTAATGAGACGTAGCGCAGGTCCCCTGGACATAACGACCTGGACAACTGCGTACCTCTCGGCTCTCGGCCACGATGTGATATGAAGCCCACGGGAAATCGTTCTATGACAGATCGCTCCCCACAACTAAGATTCAACAGATAGACTCGAGTCGCGAAGAATATTGACGTAATAACCGATTAAGTAGACGCCCCGCATGTTGCGAATTCCATATGCCAAATATAGGAGAACAGGAACGTGCATTGCTGCCCTGTATCAATATGCTCGGGGCATTAGGTGT"
# print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))


# Problem 2
# s = "GCATAACGCTCATGTTAAGCTATTGAGATCTTATACGCTACCTAAAATCTAATCACACACTCTGGACCTTGCCGTCGTAAGGTTCGTAAACGCAGGGGTATAAATGCATTCCCCCTTCTTTTGGGTCGCTTTCAAGACAACGCATAAGCTGTCCTCAGATAATCATACTTTGACCGTCCCATCGCCAGGTTCCCCGTGCATAGCTACATCGCTTCAGCAGCCATTCTAAGCGGCATCTTCCGCGGGTTGGCTAGTCTGCCGTGGGTCATGTGGAGATCTAAGAGACTTGTTTTTAGAGGCCTCCGCGTACAAGATAGCAAACAACTCAACCATCGGGCGCCAACTCGTGCACTACTTACAAAATGGCGAGTGGTAGCTCTGCTGCTGGTTTTAAAAGTAAGTTGGTGCCCCGTTCATACCATGGTCCGAGTTCTGATAGTCACGACCACTGGCGGCTGTAAGTGTACTATGAGACAGCGCACCACACATCCGTAGCTCGGTTTTAGGGTACGCTTCGCAAACTTCTTAGCGGCCACTGCGCACTTGCAGACTAGAATCCTGGGGCGGGTGTACGGACCTTAGTACATACAGTCAATCTCTCGACCACGAGATGCTCCCAGCGCTCCTTAGAGGTAGCTTGCGTGAGCGTAAGCATTCAGCGAAAGATACAACGTTTTAAGACTCTAGTTTTAGCGAAGAAATTGCAAACCGTGAGTACGTGCACAGGTGCATGGACTTATAGGTGGATTCTTCGATCCCGGGGTCCCGCAAGAAACGCGAAAGCAAAGCCATTACATCTCGGGCGGCGTTTGCTATCTAGCCAGGGGTACTCGTTTTTACCGTATGTCATGGCCAACGTCATCCGAATCTTTTGACACTTTCGCTGTGGGGGGAAAGTAGTATCTAGCAGTTATAGCGTCTCCCTCGTGAGTCCAATTGTGGATCTTCCTGTTTGGGTG"
# s = s.replace("T", "U")
# print(s)

# Problem 3
# print("\n")
# s = "TGCTCATGAATCCATCGCCTCGAAATAATAGAGTGGGTCAGCTGGCCTACTCACGGTTTCTATTAATTAATGTATAAGATCACCGCTCGAAAAATAGGCATGTCGCACTACCTACGCGGCTGTGGAGACCCGGTCAACTTTACCCAATATTCATGCGACGGCGCGCCCTGCCTAGACGGTCGCTTCATCTTAACAATCGTTGGCACAAGACGTAGCATTTTTAACGTAAACCCGCACGAACCTATCCGCCAGGTCTCGTCGGTGGGCGCATCATTATCGATTTCGCGACTTGATGCGTAACTCCAAACTCTATGTTTTAGGCTAGCACACGGGCTATCCGCGAGGGCTCTGTTGATATGGCAGAGGATCAATGGCGTATGAGATGGGGACAGGAAATCCACCCGGCTTGAGTGTACTTAAATCCCCTTCCCCGGAGTTGACTAGGGGGGACCTGTGCTGATTCGGCAGGCTGACAGCGGAATTACATTATAAAGTGATGACTTGGCACTGGGGCCGCTTTCGATCAGCGCCTGGACAACTGGAACCAAAAGCGAGTAACTGTGACAGGGTTCACTTGACACCCGCCAAGTGAAAGGCCAGGCAATTAAAAATGCGCACAGCTCTTCTATGAGTTGCCGTTGTCGGGTGAGCTCGGCTTTCTGCGTCGAGACGAGATTAAACGCCATATGGTCGGGGGCGTCAGTGTAGGGTAGAGGCGACTTGGACATGGCACAACGCGCCATTCCTTTAGCTTCCCTTCCCTCAAGAAGGTCTTTATACAGGTAAGACACTTACACTGAACAACCCGTCGCGTTAGTGAGGTATGAGTTCCCGACTAGCATGCCATGACTTCTCTATCGGGCCGTCGTTCTATTCACTTCAAATCTGTTGACTCTCCTCCAGCCAAC"


# def complement(seq):
#     complement = {"A": "T", "C": "G", "T": "A", "G": "C"}
#     bases = list(seq)
#     bases = [complement[base] for base in bases]
#     bases = bases[::-1]
#     print("".join(bases))


# complement(s)

# Problem 4
# lines = []

# content_dict = {}
# with open("GC_Content_Sample.txt", "r") as GC:
#     for line in GC:
#         line = line.split("\n")
#         line = list(filter(None, line))
#         for index in line:
#             lines.append(index)

# current = None
# for index in lines:
#     if index[0] == ">":
#         GC_content = 0
#         total = 0
#         G = 0
#         C = 0
#         linelen = 0
#         content_dict[index] = ""
#         current = index

#     else:
#         line = list(index)
#         linelen += len(line)
#         G += line.count("G")
#         C += line.count("C")
#         GC_content = (G + C) / linelen
#     content_dict[current] = float("{:.6f}".format(GC_content))


# highest = 0.0
# for key in content_dict:
#     if highest < content_dict[key]:
#         highest = content_dict[key]
#         index = key[1::]
# highest = "{:.6f}".format(highest * 100)
# print(f"{index}\n{highest}")
