def power_of_two_recursive(n):
    if n == 0:
        # Base condition
        return 1
    else:
        # Recursive solution
        power = power_of_two_recursive(n - 1)
        return power * 2


def power_of_two_iterative(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


print(power_of_two_recursive(3))
print(power_of_two_iterative(3))
