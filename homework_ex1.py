
"""
The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.
"""


# Create a class called cart that retains items and has methods to add, remove, and show

# shopping_cart = {}

class Cart:
    
    def __init__(self):
        self.shopping_cart = {}
        
    def customer_decision(self):
        while True:
            self.user_decision = input('\nWould you like to [a]dd an item, [r]emove an item, [s]ee your cart, or [e]xit?  \n').lower()
            if self.user_decision == 'a':
                self.add()
            elif self.user_decision == 'r':
                self.remove()
            elif self.user_decision == 's':
                self.show()
            elif self.user_decision == 'e':
                break
            else:
                print('Please enter a valid option: [a]dd, [r]emove, [s]ee, or [e]xit.')

    
    
    def add(self):
        print("What would you like to add? ")
        self.name = input('Item name: ').lower()
        self.quantity = int(input('How many would you like to add?  '))
        self.shopping_cart[self.name] = {
            'quantity': {self.quantity}
        }    
        print(self.shopping_cart)

                

    def remove(self):
        self.remove_item = input('Which item would you like to remove?  ')
        self.shopping_cart.pop(self.remove_item)

        
        
    def show(self):
        print(self.shopping_cart)
    
user = Cart()
user.customer_decision()
