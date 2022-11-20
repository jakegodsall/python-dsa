def factorial(n):
    if n == 0:
        # Base case where input n=0
        return 1
    else:
        # Recursive case where input n>0
        return n * factorial(n-1)


test_inputs = [1, 2, 3, 5, 10]
for val in test_inputs:
    print(f"factorial({val}) = {factorial(val)}")
