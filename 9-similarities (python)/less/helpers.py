def lines(a, b):                                        # Return lines in both a and b
    matchedLines = []
    aList = a.split('\n')                               # Divides string at \n
    bList = b.split('\n')

    if len(aList) < len(bList):                         # Decides what is compared to what
        cycleRange = len(aList)
        indexer = aList
        control = bList
    else:
        cycleRange = len(bList)
        indexer = bList
        control = aList

    for i in range(cycleRange):                         # Cycle through both lists
        if indexer[i] in control:
            if indexer[i] in matchedLines:              # Filter repeats
                continue
            elif indexer[i] == "":
                continue
            else:
                while '\n' in indexer[i]:               # Remove \n
                    indexer[i].replace('\n', '')
                matchedLines.append(indexer[i])         # Add line to list
    return matchedLines


def sentences(a, b):                                    # Return sentences in both a and b

    import re
    from nltk.tokenize import sent_tokenize

    matchedLines = []

    aList = sent_tokenize(a, language='english')        # Breaks string at sentence markers
    bList = sent_tokenize(b, language='english')

    for ay in range(0, len(aList)):                     # Remove \n
        while '\n' in aList[ay]:
            aList[ay] = re.sub(r'\n', '', aList[ay])
    for be in range(0, len(bList)):
        while '\n' in bList[be]:
            bList[be] = re.sub(r'\n', '', bList[be])

    newIndexer = ''

    if len(aList) < len(bList):                         # Decide what is compared to what
        cycleRange = len(aList)
        indexer = aList
        control = bList
    else:
        cycleRange = len(bList)
        indexer = bList
        control = aList

    for i in range(cycleRange):                         # Cycle through lists
        if indexer[i] in control:
            if indexer[i] in matchedLines:
                continue
            elif indexer[i] == "":
                continue
            else:
                matchedLines.append(indexer[i])
    return matchedLines


def substrings(a, b, n):                                # Return substrings of length n in both a and b

    import re

    aList = list(a.replace("\n", " "))                  # Remove \n and break string into letter array
    bList = list(b.replace("\n", " "))

    aSubList = list()
    bSubList = list()
    aTempWord = list()
    bTempWord = list()
    newIndexer = ''
    matchedLines = []

    for x in range(0, len(aList) - (n - 1)):            # Cycle through letter array and create
        for y in range(0, n):                           # strings that are n-length long
            aTempWord += aList[x + y]
        if aTempWord in aSubList:
            continue
        else:
            aSubList.append(''.join(aTempWord))
            aTempWord = []                              # Clear the tempWord container
    print(aSubList)

    for v in range(0, len(bList) - (n - 1)):            # Repeat for b file
        for w in range(0, n):
            bTempWord += bList[v + w]
        if bTempWord in bSubList:
            continue
        else:
            bSubList.append(''.join(bTempWord))
            bTempWord = []
    print(bSubList)

    if len(aSubList) < len(bSubList):                   # Decide what to compare to what
        cycleRange = len(aSubList)
        indexer = aSubList
        control = bSubList
    else:
        cycleRange = len(bSubList)
        indexer = bSubList
        control = aSubList

    for i in range(cycleRange):                         # Cycle through lists
        if indexer[i] in control:
            if indexer[i] in matchedLines:
                continue
            elif indexer[i] == "":
                continue
            else:
                matchedLines.append(indexer[i])         # Add like to list

    return matchedLines