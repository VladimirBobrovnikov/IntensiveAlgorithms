from typing import List


def prime_numbers(n: int) -> List[int]:
    """
    Return all prime numbers from 1 to n (including)

    Args:
        n (int): number

    Returns:
        List[int]: prime numbers
    """
    if n <= 2:
        return [2]

    for_compare = {i for i in range(2, n + 1)}
    for_del = set()
    for index in range(2, int(n**(0.5)) + 1):
        for elem in for_compare.difference(for_del):
            if elem > index and elem % index == 0:
                for_del.add(elem)
    return [elem for elem in for_compare.difference(for_del)]


# https://leetcode.com/problems/count-primes/
