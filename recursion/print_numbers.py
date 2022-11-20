def print_numbers(n):
    if n < 1:
        print("n is less than 1")
    else:
        print_numbers(n-1)
        print(n)

# Expect the output of print_numbers(4) to be
# n is less than 1
# 1
# 2
# 3
# 4


print(print_numbers(4))
