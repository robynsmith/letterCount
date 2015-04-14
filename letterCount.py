import sys
import fileinput
import collections

count = collections.defaultdict(int)
allInput = ""

for line in raw_input():
        allInput +=str(line)

allInput

Input = allInput.lower()

for i in Input:
        count[i] += 1

for i in count:
        print i, "....", count[i]
