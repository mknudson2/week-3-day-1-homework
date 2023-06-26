class UpperString:
    
    def get_input(self):
        self.user_input = input('What is your favorite word? ')
    
    def print_input(self):
        print(f'{self.user_input}'.upper())
        
word = UpperString()
word.get_input()
word.print_input()