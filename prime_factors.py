def prime_factors(n):
    while n % 2 == 0:
        yield 2
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            yield i
            n //= i

    if n > 2:
        yield n

number = int(input("введите число: "))
print(f"простые множители числа {number}:")
for factor in prime_factors(number):
    print(factor)
