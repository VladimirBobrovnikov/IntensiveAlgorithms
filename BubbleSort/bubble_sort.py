from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using bubble sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """
    flag_action = True
    for i in range(len(array) - 1):
        if not flag_action:
            break
        else:
            flag_action = False

        for j in range(len(array) - 1 - i):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag_action = True

    return array

# https://leetcode.com/problems/sort-colors/description/
