"""this file to strore information about players, such as player ID, age, ...
"""
class Player:
    def __init__(self):
        self.name = ""
        self.age = ""

    def create(self, player_no):
        self.name = input(f"Player{player_no} name: ")
        self.age = input(f"Player{player_no} age: ")


if __name__ == "__main__":
    
    player1 = Player()
    player1.create(1)
    print(f"Player 1 is {player1.name} of age {player1.age}.")
    
    player2 = Player()
    player2.create(2)
    print(f"Player 2 is {player2.name} of age {player2.age}.")
    
    player3 = Player()
    player3.create(3)
    print(f"Player 3 is {player3.name} of age {player3.age}.")
    
    player4 = Player()
    player4.create(4)
    print(f"Player 4 is {player4.name} of age {player4.age}.")
