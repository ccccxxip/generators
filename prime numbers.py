def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            yield num

start_number = int(input("введите начальное число: "))
end_number = int(input("введите конечное число: "))

print(f"простые числа между {start_number} и {end_number}:")
for prime in prime_generator(start_number, end_number):
    print(prime)
