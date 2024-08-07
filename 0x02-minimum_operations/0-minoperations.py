#!/usr/bin/python3
import math

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            while n % factor == 0:
                operations += factor
                n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    print("Min # of operations to reach {} chars: {}".format(n, minOperations(n)))

