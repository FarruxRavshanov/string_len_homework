def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a = ''
    middle = len(s) // 2
    if len(s) % 2 == 1:
        a = [middle]
    else:
        a = s[middle -1: middle + 1]
    return a