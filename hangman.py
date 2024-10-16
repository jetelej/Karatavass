import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Spēlējam bioloģijas karātavas!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Lūdzu mini burtu vai vārdu!: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Tu jau šo burtu minēji", guess)
            elif guess not in word:
                print(guess, "nav vārdā.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Malacis,", guess, "ir vārdā!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Tu jau minēji šo vārdu", guess)
            elif guess != word:
                print(guess, "nav īstais vārds.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Nepareizs minējums.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Malacis, tu uzminēji vārdu! Tu uzvari!")
    else:
        print("Piedod, tev beidzās mēģinājumi. Vārds bija " + word + ". Varbūt nākamreiz!")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Spēlēsi vēlreiz? (J/Nē) ").upper() == "J":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()