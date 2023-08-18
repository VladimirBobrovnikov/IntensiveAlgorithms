from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using selection sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """
    for i in range(len(array) - 1):
        minimum = array[i]
        index_minimum = None
        for j in range(i, len(array)):
            if array[j] < minimum:
                minimum = array[j]
                index_minimum = j

        if index_minimum:
            array[i], array[index_minimum] = array[index_minimum], array[i]
    return array

# https://leetcode.com/problems/sort-colors/
