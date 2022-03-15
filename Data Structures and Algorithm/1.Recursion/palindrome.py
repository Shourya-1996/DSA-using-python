def isPalindrome(strng):
    l = len(strng)
    if l in [0, 1]:
        return True
    if strng[0] != strng[l-1]:
        return False
    return isPalindrome(strng[1:-1])


print(isPalindrome('abcaacba'))
