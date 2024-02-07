def square_numbers(n):
    for i in range(1, n + 1):
        n = i * i
        print(n)
        return n


# Create a generator object
generator = square_numbers(5)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# Iterate over the generator
# for num in generator:
#     print(num)
