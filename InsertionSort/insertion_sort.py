from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using insertion sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """
    for i in range(1, len(array)):
        now = array[i]
        j = i - 1
        while j >= 0 and now < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = now

    return array


# https://leetcode.com/problems/sort-colors/
