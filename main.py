class Soda():
    def __init__(self, taste=None):
        self.taste = taste
    def taste_init(self):
        if self.taste:
            print(f'You have {self.taste} flavored soda')
        else:
            print('You have default soda')
soda = Soda()
soda.taste_init()