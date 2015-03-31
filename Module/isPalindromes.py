def isPal(s):
    if len(s)<=1:
        return True
    return s[0]==s[-1] and isPal(s[1:-1])