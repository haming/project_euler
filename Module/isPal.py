def isPal(s):
    """return True if is palindromes"""
    if len(s)<=1:
        return True
    return s[0]==s[-1] and isPal(s[1:-1])