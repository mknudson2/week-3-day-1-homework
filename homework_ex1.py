
"""
The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.
"""


# Create a class called cart that retains items and has methods to add, remove, and show


class Cart:
    
    def __init__(self):
        self.shopping_cart = {} #set the shopping cart within the class to be called for each instance of the class created.
        
    def customer_decision(self): #customer path, using a while loop to continue through the steps until the user chooses to exit, at which point it breaks
        while True: #begins the while loop that the user will continue in until exit is selected
            self.user_decision = input('\nWould you like to [a]dd an item, [r]emove an item, [s]ee your cart, or [e]xit?  \n').lower() #user prompt, with lower called to avoid issues with case
            if self.user_decision == 'a':
                self.add() # call the add method 
            elif self.user_decision == 'r':
                self.remove() # call the remove method
            elif self.user_decision == 's':
                self.show() # call the show method
            elif self.user_decision == 'e':
                print('Thank you for shopping with us! Please come again soon!\n') #print statement for when the user chooses to exit the loop
                print('~'*115) #separator to indicate the end of the program
                break #breaks the loop and the user exits the program
            else:
                print('Please enter a valid option: [a]dd, [r]emove, [s]ee, or [e]xit.\n') #user prompt if they do not enter a valid response

    
    def add(self):
        print("\nWhat would you like to add? ")     #prompt the user
        self.name = input('Item name: ').lower()    #assign user input to self.name, which will be used as dict key
        while True:       #error handling, specifically to avoid an error if the user does not enter a digit quant
            try:          #will try the quantity input (same as two lines up), breaking from try/except if successful
                self.quantity = int(input('\nHow many would you like to add?  ')) #assigning value to quantity
                break   #break if user input is successful
            except: ValueError #looks for the value error which would occur if not entered in digits
            print('Please enter a valid number in digits.') #prompt user to retry their input with digits
        self.shopping_cart[self.name] = {  #the key:value pair (self.name: self.quantity) are placed w/in the dict
            'quantity': self.quantity
        }    
        print(self.shopping_cart) #show the user their cart after adding item/quant

    
    def remove(self):
        self.remove_item = input('Which item would you like to remove? ')      #prompt user to id which key in the dict they are targeting for removal
        if self.remove_item in self.shopping_cart:      #conditional checking to see if the item is in the cart or not
            self.remove_quantity = int(input('\nHow many would you like to remove? '))  #after confirming that it is, prompt to declare quant to remove
            self.shopping_cart[self.remove_item]['quantity'] -= self.remove_quantity    #declaring the new quant value is the old minus the removed number.
            if int(self.shopping_cart[self.remove_item]['quantity']) <= 0:  #conditional checking if the new quant is at or below 0, which instigates item removal from dict
                self.shopping_cart.pop(self.remove_item)   #if it is <= 0, the item name/key will be removed from the shopping cart dict.
            print(f"{self.remove_quantity} {self.remove_item} has been removed from the cart. You now have {self.shopping_cart}.\n") #confirmation statement of what the cart now looks like.
        else:
            print('\nItem not found in the cart.\n')   #print statement responding to an invalid response (i.e., that item chosen to be removed does not exist in the dict)
        
        
    def show(self):
        print(f'\nYou have {self.shopping_cart} in your cart.\n') #Print statement showing user their cart as it stands
    
user = Cart()
user.customer_decision()
