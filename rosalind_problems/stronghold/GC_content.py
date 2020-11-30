def readFile(filePath):
    '''Reading a file and returning a list of lines'''
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def GCcontent(seq):
    #tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    #for nuc in seq:
    #    tmpFreqDict[nuc] += 1
    #return tmpFreqDict["G"], tmpFreqDict["C"]
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

FASTAFile = readFile('../test_data/rosalind_gc.txt')
FASTADict = {}
FASTALabel = ""

print(FASTAFile)

# Converting FASTA file into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# Format the data
# Using Dictionary Comprehension to generate a new dictionary with GC content
RESULTDict = {key: GCcontent(value) for (key, value) in FASTADict.items()}

print(RESULTDict)

# Looking for max value in values() of our new dictionary
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

# Print Rosalind formatted result
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')