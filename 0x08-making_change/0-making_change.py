#!/usr/bin/python3

'''Given a collection of coins with varying values,

    determine the minimal number of coins required to achieve

    a specified total amount.

'''

import sys

def makeChange(coins, total):

    '''

    Return: minimal number of coins required to reach total

    If total is less than or equal to 0, return 0

    If the total cannot be achieved with the available coins, return -1

    '''

    if total <= 0:

        return 0

    table = [sys.maxsize for _ in range(total + 1)]

    table[0] = 0

    m = len(coins)

    for i in range(1, total + 1):

        for j in range(m):

            if coins[j] <= i:

                subres = table[i - coins[j]]

                if subres != sys.maxsize and subres + 1 < table[i]:

                    table[i] = subres + 1

    if table[total] == sys.maxsize:

        return -1

    return table[total]

