a="""In the beginning God created the heavens and the earth. And the earth was waste and void; and darkness was upon the face of the deep: and the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light."""
b="""In the beginning, God created the heavens and the earth. The earth was without form and void, and darkness was over the face of the deep. And the Spirit of God was hovering over the face of the waters. And God said, "Let there be light," and there was light."""

n = 5



import re

aList = list(a.replace("\n", " "))
bList = list(b.replace("\n", " "))

aSubList = list()
bSubList = list()
aTempWord = list()
bTempWord = list()
newIndexer = ''
matchedLines = []

for x in range(0, len(aList)-(n-1)):
    for y in range(0, n):
        aTempWord += aList[x+y]
    if aTempWord in aSubList:
        continue
    else:
        aSubList.append(''.join(aTempWord))
        aTempWord = []
print(aSubList)

for v in range(0, len(bList)-(n-1)):
    for w in range(0, n):
        bTempWord += bList[v+w]
    if bTempWord in bSubList:
        continue
    else:
        bSubList.append(''.join(bTempWord))
        bTempWord = []
print(bSubList)

if len(aSubList) < len(bSubList):
    cycleRange = len(aSubList)
    indexer = aSubList
    control = bSubList
else:
    cycleRange = len(bSubList)
    indexer = bSubList
    control = aSubList

for i in range(cycleRange):
    if indexer[i] in control:
        if indexer[i] in matchedLines:
            continue
        else:
            matchedLines.append(indexer[i])

print( matchedLines)