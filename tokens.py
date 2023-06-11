"""this file to make tokens for players, such as dinosaur, hat, dog, ...
"""

class Token:
    def __init__(self, name):
        self.name = name
        self.image_loc = r"pic\token_" + name + r".png"
        
        self.money = 0
        self.position = (0, 0)


if __name__ == "__main__":
    play1_token = Token("tophat")
    play2_token = Token("boot")
    play3_token = Token("racecar")
    play4_token = Token("battleship")
    print (f"Player 4 is {play4_token.image_loc}")
