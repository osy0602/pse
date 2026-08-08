import random
import string
class WordGame:
    def __init__(self):
        self.secret = self.get_random_word()
        self.blanks = ["_" for _ in self.secret]
        self.lives = 6
        self.used = set()

    def get_random_word(self):
        words = [
                "python", "variable", "function", "iterator", "notebook",
                "pipeline", "dataset", "computer", "research", "analytics"
        ]
        return random.choice(words)
    
    def prompt_for_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in self.used:
                print(" → You already tried that letter.")
                continue
            return guess

    def reveal_letters(self, letter):
        found_any = False
        for i, ch in enumerate(self.secret):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

    def all_blanks_filled(self):
        return "_" not in self.blanks
    
    def play_game(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret)} letters.")
        print(" ".join(self.blanks))

        while True:
            guess = self.prompt_for_letter()
            self.used.add(guess)

            if self.reveal_letters(guess):
                print("Well done, Nice job! You found a letter.")
                print(" ".join(self.blanks))
                if self.all_blanks_filled():
                    print("Congratulations! You've guessed the word!")
                    print(f"Word: {self.secret}")
                    print("GAME OVER")
                    break
            else:
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))
                if self.lives <= 0:
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {self.secret}")
                    print("GAME OVER")
                    break

if __name__ == "__main__":
    game = WordGame()
    game.play_game()