# for i in range(17):
#     print(f"{i:>2} in binary is {i:>08b} and {i:>92x} in hexadecimal")

# x = 0x20
# y = 0x0a
# print(x)
# print(y)
# print(x * y)
# print(0b101010)

initial_number = 37
number = 37
binary = 0
while number > 1:
    biggest_power = 0
    while 2 ** biggest_power <= number:
        biggest_power += 1
    biggest_power -= 1
    binary += 10 ** biggest_power
    number -= 2 ** biggest_power
else:
    binary += number

print("Number ", initial_number, " in binary is ", binary)


def conversion_for_bases_till_10(decimal_number, number_system=2):
    representation = 0
    number = decimal_number
    while number > number_system - 1:
        biggest_power = 0
        while number_system ** biggest_power <= number:
            biggest_power += 1
        biggest_power -= 1
        representation += 10 ** biggest_power * \
            (number // (number_system ** biggest_power))
        number = number % (number_system**biggest_power)
    else:
        representation += number
    print(
        f"Number {decimal_number} is represented as {representation} in \
        number system of base {number_system}")


conversion_for_bases_till_10(37, number_system=8)
conversion_for_bases_till_10(37)
conversion_for_bases_till_10(37, number_system=3)


# Video solution
def video_conversion(decimal_number, number_system=2):
    powers = []
    for power in range(15, -1, -1):
        powers.append(number_system**power)
    print(powers)

    x = decimal_number

    printing = False
    for power in powers:
        bit = x // power
        if bit != 0 or power == 1:
            printing = True
        if printing:
            print(bit, end=" ")
        x %= power
    print()


video_conversion(15)
video_conversion(16, number_system=8)
video_conversion(16, number_system=16)
