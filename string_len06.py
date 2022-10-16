def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    a = len(s1)
    b = len(s2)
    if a > b:
        d = s2
    else:
        d = s1
    return d

print(main('house', 'church'))