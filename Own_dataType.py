class Fraction:

    def __init__(self, n, d):   # n = numerator, d = denominator
        self.num = n
        self.den = d
    
    # whenever we try to print the object of our class using a print function
    # the print function searches for __str__ which is a magic method
    # that calls itself automatically when a certain requirement is met
    def __str__(self):
        # return "Hello"
        return "{}/{}".format(self.num, self.den)
    
    # We can't directly add two objects. To do so we have to define 
    # how the object will be added using the __add__ magic method
    def __add__(self,other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)
    
lala = Fraction(5, 6)
kaka = Fraction(7, 8)
print(lala)
print(lala + kaka)