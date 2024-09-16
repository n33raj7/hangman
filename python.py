import random

class Hangman:
    def __init__(self):
        print("Welcome to 'Hangman', are you ready to die?")
        print("(1) Yes, for I am already dead.")
        print("(2) No, get me outta here!")
        user_choice_1 = input("-> ")

        if user_choice_1 == '1':
            print("Loading nooses, murderers, rapists, thieves, lunatics...")
            self.start_game()
        elif user_choice_1 == '2':
            print("Bye bye now...")
            exit()
        else:
            print("I'm sorry, I'm hard of hearing, could you repeat that?")
            self.__init__()

    def load_words(self):
        with open('words.txt', 'r') as file:
            words = [line.strip() for line in file]
        return words

    def start_game(self):
        print("A crowd begins to gather, they can't wait to see some real")
        print("justice. There's just one thing, you aren't a real criminal.")
        print("No, no. You're the wrong time, wrong place type. You may think")
        print("you're dead, but it's not like that at all. Yes, yes. You've")
        print("got a chance to live. All you've gotta do is guess the right")
        print("words and you can live to see another day. But don't get so")
        print("happy yet. If you make 6 wrong guesses, YOU'RE TOAST! VAMANOS!")
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = set()
        words = self.load_words()
        the_word = random.choice(words).lower()
        progress = ["?"] * len(the_word)
        
        while guesses < 6:
            guess = input("Guess a letter -> ").lower()

            if guess in letters_used:
                print("You've already guessed that letter. Try again!")
                continue

            if guess in the_word:
                print("As it turns out, your guess was RIGHT!")
                letters_used.add(guess)
                progress = self.progress_updater(guess, the_word, progress)
                self.hangman_graphic(guesses)
                print("Progress: " + "".join(progress))
                print("Letters used: " + ", ".join(letters_used))
            else:
                print("Things aren't looking so good, that guess was WRONG!")
                print("Oh man, that crowd is getting happy, I thought you")
                print("wanted to make them mad?")
                letters_used.add(guess)
                guesses += 1
                self.hangman_graphic(guesses)
                print("Progress: " + "".join(progress))
                print("Letters used: " + ", ".join(letters_used))

            if "?" not in progress:
                print("Congratulations, you've guessed the word!")
                break
        else:
            print("The noose tightens around your neck, and you feel the")
            print("sudden urge to urinate.")
            print("GAME OVER!")
            self.__init__()

    def hangman_graphic(self, guesses):
        hangman_states = [
            "________      \n|      |      \n|             \n|             \n|             \n|             ",
            "________      \n|      |      \n|      0      \n|             \n|             \n|             ",
            "________      \n|      |      \n|      0      \n|     /       \n|             \n|             ",
            "________      \n|      |      \n|      0      \n|     /|      \n|             \n|             ",
            "________      \n|      |      \n|      0      \n|     /|\\     \n|             \n|             ",
            "________      \n|      |      \n|      0      \n|     /|\\     \n|     /       \n|             ",
            "________      \n|      |      \n|      0      \n|     /|\\     \n|     / \\     \n|             \nThe noose tightens around your neck, and you feel the\nsudden urge to urinate.\nGAME OVER!"
        ]
        print(hangman_states[guesses])

    def progress_updater(self, guess, the_word, progress):
        for i, letter in enumerate(the_word):
            if letter == guess:
                progress[i] = guess
        return progress

game = Hangman()
