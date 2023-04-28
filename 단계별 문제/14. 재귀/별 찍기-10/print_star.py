import sys

n = int(sys.stdin.readline())
star = ["***", "* *", "***"]
count = 0


def printStar(star):
    result = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            result.append(star[i % len(star)] + " " * len(star) + star[i % len(star)])
        else:
            result.append(star[i % len(star)] * 3)
    return result


while n > 3:
    n /= 3
    count += 1

for i in range(count):
    star = printStar(star)

for i in star:
    print(i)