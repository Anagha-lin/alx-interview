#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """ Returns a list of primes up to max_n using the Sieve of Eratosthenes. """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return [i for i in range(max_n + 1) if is_prime[i]]

def isWinner(x, nums):
    """ Determines the overall winner of the Prime Game. """
    if x == 0:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = len(primes)
    
    # Count wins
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # Count primes up to n
        count_primes = sum(1 for p in primes if p <= n)
        if count_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

