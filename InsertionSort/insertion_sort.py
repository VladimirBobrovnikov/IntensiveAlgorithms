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
        for j in range(i - 1, -1, -1):
            if array[j] > now:
                array[j + 1] = array[j]
            else:
                array[j + 1] = now
                break
    return array


# https://leetcode.com/problems/sort-colors/
