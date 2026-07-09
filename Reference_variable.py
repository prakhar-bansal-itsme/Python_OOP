class Customer:
    
    def __init__(self, name):
        self.name = name
    
def greet(customer):
    # print(id(customer))
    customer.name = "hello"
    print(customer.name)

cust = Customer("Prakhar")
# print(id(cust))

greet(cust)
print(cust.name)