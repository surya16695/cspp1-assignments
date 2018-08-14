''' The 6.00 Word Game '''
import random
# import string
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for loop_var in sequence:
        freq[loop_var] = freq.get(loop_var, 0) + 1
    return freq
# (end of helper code)
# -----------------------------------
#
# Problem #1: Scoring a word
#
def get_wordscore(word, n_inp):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    word_score = 0
    for char in word:
        word_score += SCRABBLE_LETTER_VALUES[char]
    if len(word) == n_inp:
        return word_score*len(word) + 50
    return word_score*len(word)
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.
    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for _ in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def deal_hand(n_inp):
    """
    Returns a random hand containing n_inp lowercase letters.
    At least n_inp/3 the letters in the hand should be VOWELS.
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n_inp: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n_inp // 3
    for _ in range(num_vowels):
        loop_var = VOWELS[random.randrange(0, len(VOWELS))]
        hand[loop_var] = hand.get(loop_var, 0) + 1
    for _ in range(num_vowels, n_inp):
        loop_var = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[loop_var] = hand.get(loop_var, 0) + 1
    return hand
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand_temp = hand.copy()
    for char in word:
        if char in hand_temp:
            hand_temp[char] -= 1
    return hand_temp
#
# Problem #3: Test word validity
#
def is_validword(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # count = 0
    # for char in word:
    #     if hand[char] > 0:
    #         count += 1
    #     else:
    #         return False
    # if count == len(word):
    #     if word in word_list:
    #         return True
    # return False
    if word not in word_list:
        return False
    word_dict = get_frequency_dict(word)
    for each_char in word_dict:
        if each_char not in hand:
            return False
        if word_dict[each_char] > hand[each_char]:
            return False
    return True
#
# Problem #4: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())
def play_hand(hand, word_list, n_inp):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0
    while calculate_handlen(hand):
        display_hand(hand)
        word = input("Enter a word: ")
        if word in '.':
            break
        else:
            if not is_validword(word, hand, word_list):
                print("Invalid Input")
            else:
                word_score = get_wordscore(word, n_inp)
                print("Your score for this turn is: ", word_score)
                hand = update_hand(hand, word)
                total_score += word_score
    print("Your total score is: ", total_score)
#
# Problem #5: Playing a game
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
    2) When done playing the hand, repeat from step 1
    """
    hand = None
    while True:
        if hand is not None:
            input_from_user = input("Enter 'n' or 'r' or 'e' to start playing: ")
        else:
            input_from_user = input("Enter 'n' or 'e' to start playing: ")
        if input_from_user == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif input_from_user == 'r' and hand is not None:
            play_hand(hand, word_list, HAND_SIZE)
        elif input_from_user == 'e':
            print("Game over!")
            return
        else:
            print("Enter a valid input")
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    WORD_LIST1 = load_words()
    play_game(WORD_LIST1)