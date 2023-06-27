
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
                print('Thank you for shopping with us! Please come again soon!\n')
                print('~'*115)
                break
            else:
                print('Please enter a valid option: [a]dd, [r]emove, [s]ee, or [e]xit.\n')

    
    def add(self):
        print("\nWhat would you like to add? ")
        self.name = input('Item name: ').lower()
        self.quantity = int(input('\nHow many would you like to add?  '))
        self.shopping_cart[self.name] = {
            'quantity': self.quantity
        }    
        print(self.shopping_cart)

    
    def remove(self):
        self.remove_item = input('Which item would you like to remove? ')
        if self.remove_item in self.shopping_cart:
            self.remove_quantity = int(input('\nHow many would you like to remove? '))
            self.shopping_cart[self.remove_item]['quantity'] -= self.remove_quantity
            if int(self.shopping_cart[self.remove_item]['quantity']) <= 0:
                # del self.shopping_cart[self.remove_item]
                self.shopping_cart.pop(self.remove_item)
            print(f"{self.remove_quantity} {self.remove_item} has been removed from the cart. You now have {self.shopping_cart}.\n")
        else:
            print('\nItem not found in the cart.\n')
        
        
    def show(self):
        print(f'\nYou have {self.shopping_cart} in your cart.\n')
    
user = Cart()
user.customer_decision()
