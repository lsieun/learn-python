#!/usr/bin/env python3
# Last modified: 2018-08-24 01:06:59

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print('\t',f)
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True  

num_list = range(10)
some_list = [
    num + 5
    for num in num_list
    if is_prime(num)
]

print(some_list)
