def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a = len(s1)
    a1 = str(s1)
    b = len(s2)
    b1 = str(s2)
    c = len(s3)
    c1 = str(s3)
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        z = '[a1, b1, c1]'
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        z = '[]'
    
    return z

print(main('code', 'coder', 'python'))