#!/usr/bin/env python3

def print_arr(x):
    out = ""
    for i in x:
        out += str(i)
        out += " "
    print(out)

def insertionsort(x):
    n = len(x)
    print("Insertion sort:")
    for i in range(1, n):
        print_arr(x)
        curr = x[i]
        j = i-1
        run = False
        while j > -1 and curr < x[j]:
            run = True
            j -= 1
        j += 1

        if (run):
            del x[i] 
            x.insert(j, curr)
    return x

# Get inp
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))

x = insertionsort(x)

# Print array
print("Sorted Arr:")
print_arr(x)
