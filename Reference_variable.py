class Customer:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
def greet(customer):
    if customer.gender == "male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "sir")

cust = Customer("Prakhar", "male")
greet(cust)
