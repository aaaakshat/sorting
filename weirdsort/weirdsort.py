#!/usr/bin/env python3

def print_arr(x):
    out = ""
    for i in x:
        out += str(i)
        out += " "
    print(out)

def weirdsort_up(x):
    n = len(x)
    print("Bubblesort up:")
    for i in range(n):
        print_arr(x)
        for j in range(i+1, n):
            if (x[j] < x[i]):
                t = x[j]
                x[j] = x[i] 
                x[i] = t
    return x

def weirdsort_down(x):
    n = len(x)
    print("Bubblesort down:")
    for i in range(n-1, -1, -1):
        print_arr(x)
        for j in range(0, i):
            if (x[j] > x[i]):
                t = x[j]
                x[j] = x[i] 
                x[i] = t
    return x

# Get inp
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))

x = weirdsort_down(x)

# Print array
print("Sorted Arr:")
print_arr(x)
