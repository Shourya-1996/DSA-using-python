def decimalTobinary(n):
    assert int(n) == n, 'number must be integer'
    if n == 0:
        return 0
    else:
        return n % 2 + 10*decimalTobinary(int(n/2))


print(decimalTobinary(13))
