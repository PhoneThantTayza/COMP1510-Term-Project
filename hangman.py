import json
import random

DIFFICULTY = ["easy", "medium", "hard"]

def get_words_from_json(file_path):
    """Load word records from a JSON file.

    :param file_path: Path to the JSON file containing word records.
    :return: The loaded word records, or an empty list if the file is missing.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = json.load(file)
        return words
    except FileNotFoundError:
        print("File not found!")
        return[]

def words_by_difficulty(difficulty, word_list):
    """Filter word records by difficulty.

    :param difficulty: The difficulty level to match.
    :param word_list: A list of dictionaries containing word and difficulty fields.
    :return: A list of word strings matching the difficulty.
    """
    filtered_words = [word["word"] for word in word_list if word["difficulty"] == difficulty]
    return filtered_words

def choose_difficulty():
    """Ask the player for a difficulty until a valid choice is entered.

    :return: The selected difficulty as a lowercase string.
    """
    while True:
        try:
            difficulty = input("Choose difficulty level: (Easy, Medium, Hard)").lower().strip()
            if difficulty not in DIFFICULTY:
                raise ValueError("Invalid difficulty level")
            return difficulty
        except ValueError:
            print("Invalid Difficulty level. Please enter Easy Medium or Hard")

def create_blanks(word):
    """Create a blank for each letter in the word.

    :param word: The word the player will guess.
    :return: A list containing one " -" string for each letter.
    """
    guess_word = []
    for i in range(len(word)):
        guess_word.append(" -")
    return guess_word

def display_word(guess_word):
    """Print the revealed letters and remaining blanks.

    :param guess_word: A list of revealed letters and blank strings.
    :return: None.
    """
    string = ""
    # put in the string from the list
    for letter in guess_word:
        string += letter

    print(string)

def reveal_letter(word, guess_word, user):
    """Reveal the first unrevealed occurrence of the guessed letter.

    :param word: The word the player is trying to guess.
    :param guess_word: The list of letters and blanks to update in place.
    :param user: The letter guessed by the player.
    :return: None.
    """
    for i in range(len(word)):
        if user == word[i] and guess_word[i] == " -":
            guess_word[i] = user
            break

def choose_word(file_path, difficulty):
    """Select a random word matching the chosen difficulty.

    :param file_path: Path to the JSON file containing word records.
    :param difficulty: The difficulty level to match.
    :return: A randomly selected word string.
    """
    words = get_words_from_json(file_path)
    filtered_words = words_by_difficulty(difficulty, words)
    return random.choice(filtered_words)

def get_guess():
    """Ask for a guess until the player enters one alphabetical letter.

    :return: The valid guessed letter as a lowercase string.
    """
    while True:
        user = input("Guess the letter: ").lower().strip()
        if len(user) == 1 and user.isalpha():
            return user
        print("Please enter one alphabetical letter.")

def play(player_name):
    """Run one Hangman game and return the remaining wrong guesses as the score.

    :param player_name: The arcade player's name.
    :return: The remaining guesses on a win, or zero on a loss.
    """
    difficulty = choose_difficulty()
    random_word = choose_word("data/word-list.json", difficulty)
    score = 6
    guess_word = create_blanks(random_word)

    while " -" in guess_word and score > 0:

        display_word(guess_word)

        user = get_guess()

        if user not in random_word:
            score -= 1
            if score == 0:
                print(f"You lost\nThe word is {random_word}")
            else:
                print(f"You have {score} guesses left.")
        else:
            reveal_letter(random_word, guess_word, user)

        if " -" not in guess_word:
            print("Congratulations! You win!")

    return score
