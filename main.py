import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        pass

    def increment_score(self):
        self.score += 1
    
    def reset_score(self):
        self.score = 0
    pass

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def make_choice(self, choices):
        while True:
            choice = input("Enter your choice (rock/paper/scissor/lizard/spock): ")
            if choice in choices:
                return choice
            
            print("Invalid choice")
    pass

class Computer(Player):
    def __init__(self, name = "Computer"):
        super().__init__(name)
    
    def make_choice(self, choices):
        return random.choice(choices)
    pass

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor", "lizard", "spock"]
        self.rules = {
            "rock": ["scissor", "lizard"],
            "scissor": ["paper", "lizard"],
            "paper": ["rock", "spock"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissor"]
        }
        self.human_player = None
        self.computer_player = Computer()
        self.win_score = 3
        self.round = 1
    
    def display_welcome_message(self):
        print("""
            Welcome to RPS game with Lizard and Spock. Win 3 times to be a champion.
        """)
    
    def create_human_player(self):
        player_name = input("Please input your name: ")
        self.human_player = Human(player_name)
    
    def play_round(self):
        print(f"Round {self.round}")
        
        computer_choice = self.computer_player.make_choice(self.choices)
        human_choice = self.human_player.make_choice(self.choices)

        print(f"Computer choice: {computer_choice}")
        print(f"Human choice: {human_choice}")

        if human_choice in self.rules[computer_choice]:
            self.computer_player.increment_score()
            print("Computer wins")
        elif computer_choice in self.rules[human_choice]:
            self.human_player.increment_score()
            print("Human wins")
        else:
            print("Tie!!")
        
        print(f"Computer score: {self.computer_player.score}")
        print(f"Human score: {self.human_player.score}")

        self.round += 1
    
    def check_winner(self):
        if self.computer_player.score == self.win_score:
            print("Sorry, you lose")
            return True
        elif self.human_player.score == self.win_score:
            print("Congratulations, you are the champion")
            return True
        else:
            return False

    def play_again(self):
        ans = input("Play again? (Y/N): ")
        return ans == "Y" or ans == "y"
    
    def reset_game(self):
        self.computer_player.reset_score()
        self.human_player.reset_score()
        self.round = 1
        pass

    def start_game(self):
        self.display_welcome_message()
        self.create_human_player()

        while True:
            self.play_round()
            if self.check_winner():
                if self.play_again():
                    self.reset_game()
                else:
                    print("Good Bye!")
                    return
            pass
        pass
    pass

game = Game()
game.start_game()