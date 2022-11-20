def fibonacci(n):
    assert n >= 0 and int(n) == n, "input must be a positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(5))
