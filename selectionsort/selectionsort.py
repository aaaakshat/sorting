#!/usr/bin/env python3

def selectionsort_up(x):
    n = len(x)
    for i in range(n):
        mini = i
        for j in range(i, n):
            if (x[j] < x[mini]):
                mini = j
        t = x[i]
        x[i] = x[mini] 
        x[mini] = t
    return x
    
def selectionsort_down(x):
    n = len(x)
    for i in range(n-1, -1, -1):
        maxi = i
        for j in range(0, i):
            if (x[j] > x[maxi]):
                maxi = j
        t = x[i]
        x[i] = x[maxi] 
        x[maxi] = t
    return x

# Get inp
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))

x = selectionsort_down(x)

# Print array
out = ""
for i in x:
    out += str(i)
    out += " "

print(out)
