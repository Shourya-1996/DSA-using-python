def sumofDigits(n):
    assert n >= 0 and int(n) == n, 'number must be positive integer number'
    if n == 0:
        return 0
    else:
        return sumofDigits(int(n//10)) + int(n % 10)


print(sumofDigits(521))
