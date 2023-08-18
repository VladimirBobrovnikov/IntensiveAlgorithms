from collections import deque

brackets_mapping = {
    '{': '}',
    '[': ']',
    '(': ')',
}

def are_brackets_correct(string: str) -> bool:
    """
    Accepts a string consisting only of opening and closing parentheses as input,
    and checks whether this string is correct.
    An empty string (absence of parentheses) is considered correct.

    Args:
        string (str): string to check

    Returns:
        bool: are parentheses correct
    """
    stack = deque()
    for elem in string:
        if brackets_mapping.get(elem):
            stack.append(elem)
        else:
            if not len(stack):
                return False
            compare = stack.pop()
            if elem != brackets_mapping.get(compare):
                return False
    if len(stack):
        return False

    return True


# https://leetcode.com/problems/valid-parentheses/
