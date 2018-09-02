a="""In the beginning, God created the heavens and the earth. The earth was without form and void, and darkness was over the face of the deep. And the Spirit of God was hovering over the face of the waters. And God said, "Let there be light," and there was light."""
b="""In the beginning, God created the heavens and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light."""

import re
from nltk.tokenize import sent_tokenize

aList = sent_tokenize(a, language='english')   #re.split('[\.|\?|\!]',a)
bList = sent_tokenize(b, language='english')   #re.split('[\.|\?|\!]',b)

matchedLines = []

for ay in range(0, len(aList)):
    while '\n' in aList[ay]:
        aList[ay] = re.sub(r'\n','', aList[ay])
for be in range(0, len(bList)):
    while '\n' in bList[be]:
        bList[be] = re.sub(r'\n','', bList[be])

newIndexer = ''

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
            matchedLines.append(indexer[i])
print( matchedLines)