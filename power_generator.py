def power_generator(base, exponent):
    for i in range(exponent + 1):
        yield base ** i

base_number = int(input("введите основание (число): "))
max_exponent = int(input("введите показатель степени: "))

print(f"степени числа {base_number} от 0 до {max_exponent}:")
for power in power_generator(base_number, max_exponent):
    print(power)
