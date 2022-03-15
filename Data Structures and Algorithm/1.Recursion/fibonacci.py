def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Please enter a positive integer >= 0'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# print the nth term of fibonacci series
print(fibonacci(2))
