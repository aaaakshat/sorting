#!/usr/bin/env python3

def printArr(a):
    for i in a:
        print(i)

n = input()
a = []
for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    for j in range(i, len(a)):

