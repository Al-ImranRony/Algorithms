import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")


def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def findLCM(a, b):
    lcm = (a * b) // GCD(a, b)
    return lcm


print(findLCM(7, 14))
