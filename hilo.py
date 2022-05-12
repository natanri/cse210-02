import random

POINTS = 300
class pick_a_card:
    """
    this class will show us the random number for the first card
    """
    
    def __init__(self):
        self.value = 0
        self.points = POINTS
        
    """
    This method will pull the first card
    
    """
    def display_card(self):
        self.value = random.randint(1, 13)
        print(f"The card is: {self.value}")
        
    """
    This will display the text and ask for letter if the next number is lower or higher
    """
    def input_letter(self):
        (input("Higher or lower? [h/l] "))
        
        
    """
    Then display the next number
    """
    def display_next_card(self):
        self.value = random.randint(1, 13)
        print(f"Next card was: {self.value}")
    
class Game(pick_a_card):
    """
    This method suppose to get the value and added or subtract depend on the letter, we are still working on this method.
    """
    
    def __init__(self, value, points):
        super().__init__(value, points)
        
    def score(self):
        if self.display_next_card > self.display_card:
            self.points = self.points + 100
        else:
            return self.points - 75
            
            
        
   
a = pick_a_card()
a.display_card()
a.input_letter()
a.display_next_card()
b = Game()
b.score()
    
    
    

