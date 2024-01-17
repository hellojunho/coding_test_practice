import sys

n = int(sys.stdin.readline())**3

hipen = []
for i in range(n):
    hipen.append('-')

def slicing(hipen):
    if len(hipen) == 1:
        return hipen
    else:
        mid = len(hipen)//2
        left = hipen[:mid]
        right = hipen[mid:]
        