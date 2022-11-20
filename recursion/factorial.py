def factorial_recursive(n):
    if n == 0:
        # Base case where input n=0
        return 1
    else:
        # Recursive case where input n>0
        return n * factorial_recursive(n-1)


def factorial_iterative(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial = factorial * i
        i = i + 1
    return factorial


test_inputs = [1, 2, 3, 4, 5, 10]
for val in test_inputs:
    print(f"factorial({val}) = {factorial_recursive(val)}")


for val in test_inputs:
    print(f"factorial({val}) = {factorial_iterative(val)}")
