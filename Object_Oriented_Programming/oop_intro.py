class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 5.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 9.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 24.98)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
