# Find out the connected pair


import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


for _ in range(int(input())):
    p, q = map(int, input().split())

    if 