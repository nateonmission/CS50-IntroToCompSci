a="""In the beginning, God created the heavens and the earth.
The earth was without form and void, and darkness was over the face of the deep.
And the Spirit of God was hovering over the face of the waters.
And God said, "Let there be light," and there was light."""
b="""In the beginning, God created the heavens and the earth.
And the earth was without form, and void; and darkness was upon the face of the deep.
And the Spirit of God moved upon the face of the waters.
And God said, Let there be light: and there was light."""
matchedLines = []



aList = a.split('\n')
bList = b.split('\n')
print(aList)
print(bList)

if len(aList) < len(bList):
    cycleRange = len(aList)
    indexer = aList
    control = bList
else:
    cycleRange = len(bList)
    indexer = bList
    control = aList

for i in range(cycleRange):
    if indexer[i] in control:
        if indexer[i] in matchedLines:
            continue
        else:
            while '\n' in indexer[i]:
                indexer[i].replace('\n','')
            matchedLines.append(indexer[i])
print( matchedLines)