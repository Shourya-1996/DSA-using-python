def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'power is not integer'
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)


print(power(2.2, 4))
