'''
Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score for a single word. The function get_word_score should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
'''

def get_word_score(word, n):
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
    # TO DO ... <-- Remove this comment when you code this function
    """
    Unit test for getWordScore
    """
    failure = False
    # dictionary of words and scores
    words = {("", 7): 0, ("it", 7): 4, ("was", 7): 18, ("scored", 7): 54, ("waybill", 7): 155, ("outgnaw", 7): 127, ("fork", 7): 44, ("fork", 4): 94}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print ("FAILURE: test_getWordScore()")
            print ("\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
        failure = True
    if not failure:
        print ("SUCCESS: test_getWordScore()")
    


def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print (get_word_score(data[0], int(data[1])))

if __name__ == "__main__":
    main()
