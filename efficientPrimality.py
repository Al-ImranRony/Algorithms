import sys
import math
from math import sqrt

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# 1. Check if given num is prime or not by most efficient method in worst case scenario.
# def CheckPrime(n, cnt):
#     if n == 2:
#         cnt += 1
#         print("Prime", "-> Iterration needed:", cnt)
#         return
#     if (n == 1) or (n % 2 == 0):
#         cnt += 1
#         print("Not prime", "-> Iterration needed:", cnt)
#         return

#     sr = int(math.sqrt(n))
#     for i in range(3, sr + 1, 2):
#         cnt += 1
#         if n % i == 0:
#             print("Not prime", "-> Iterration needed:", cnt)
#     print("Prime", "-> Iterration needed:", cnt)

# for _ in range(int(input())):
#     n = int(input())
#     cnt = 0
#     CheckPrime(n, cnt)


# 3. Generate primes between 2 given numbers by bruteForce - Need 0.8sec & 22M  
for _ in range(int(input())):
    m, n = map(int, input().split())
    primes = {}
    for i in range(2, int(sqrt(n)+1)):
        for j in range(max(m//i, 2), (n//i)+1):
            primes[i * j] = 1                   #Dictionary of non-prime numbers

    for i in range(max(m, 2), n+1):
        if i not in primes:                     #Produce primes by checking non-primes
            print(i) 


# 3. Generate primes between 2 given numbers by efficient logic - Exceeds time limit & 12M 
# def GeneratePrime(a, b):
#     l = []
#     for i in range(a, b+1):
#         if (i == 1):
#             continue
#         elif (i == 2):
#             l.append(2)
#         elif (i == 3):
#             l.append(3)
#         elif (i%2 == 0 or i%3 == 0):
#             continue
#         else:
#             for j in range(5, int(sqrt(i))+1, 6):
#                 if (i%j == 0 or i%(j+2) == 0):
#                     break
#             l.append(i)                
#     return l              

# for _ in range(int(input())):
#     m, n = map(int, input().split())

#     primes = GeneratePrime(m, n)
#     for prime in primes:
#         print(prime)
#     print() 

