def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    answer = ''
    middle = len(s) // 2
    if len(s) % 2 == 1:
        answer = s[middle]
    else:
        answer = s[middle -1: middle + 1]
    return answer