#!/usr/bin/env python3

def print_arr(x):
    out = ""
    for i in x:
        out += str(i)
        out += " "
    print(out)

# Doesn't work for some reason
def bubblesort_up(x):
    n = len(x)
    print("Bubblesort up:")
    sorted = True 
    for i in range(n):
        sorted = True 
        print_arr(x)
        for j in range(n):
            if (x[j] > x[j+1]):
                t = x[j]
                x[j] = x[j+1] 
                x[j+1] = t
                sorted = False
        if(sorted):
            break
    return x

def bubblesort_down(x):
    n = len(x)
    print("Bubblesort down:")
    sorted = True
    for i in range(n-1, -1, -1):
        sorted = True 
        print_arr(x)
        for j in range(n-1, 0, -1):
            if (x[j] < x[j-1]):
                t = x[j]
                x[j] = x[j-1] 
                x[j-1] = t
                sorted = False
        if(sorted):
            break
    return x

# Get inp
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))

x = bubblesort_down(x)

# Print array
print("Sorted Arr:")
print_arr(x)
