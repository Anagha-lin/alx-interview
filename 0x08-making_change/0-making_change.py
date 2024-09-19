#!/usr/bin/python3

'''Given an assortment of coins with distinct values,

    determine the minimum number of coins necessary to achieve

    a specified total sum.

'''

import sys

def makeChange(coins, total):

    '''

    Return: minimum number of coins necessary to reach the total.

    If the total is 0 or less, return 0.

    If the total cannot be matched with any combination of coins, return -1.

    '''

    if total <= 0:

        return 0

    dp = [sys.maxsize for _ in range(total + 1)]

    dp[0] = 0

    num_coins = len(coins)

    for amount in range(1, total + 1):

        for coin in range(num_coins):

            if coins[coin] <= amount:

                sub_result = dp[amount - coins[coin]]

                if sub_result != sys.maxsize and sub_result + 1 < dp[amount]:

                    dp[amount] = sub_result + 1

    if dp[total] == sys.maxsize:

        return -1

    return dp[total]

