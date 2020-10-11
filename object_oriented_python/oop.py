a = 12
b = 4
print(a*b)
print(a.__add__(b))


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 4
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.99)
print(hamilton.make)
print(hamilton.price)

print(f"Models: {kenwood.make} = {kenwood.price}, \
{hamilton.make} = {hamilton.price}")

# Same as above
print("Models: {0.make} = {0.price}, \
{1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
hamilton.switch_off()
print(hamilton.on)

kenwood.power = 1.5  # We can add it dynamically
print(kenwood.power)  # but it is not part of class
# print(hamilton.power) Will give an error


print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
