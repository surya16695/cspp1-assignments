'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
dec_k = ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'KD', 'JD', 'QD'
         'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'KH', 'JH', 'QH', 
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'KS', 'JS', 'QS', 
         'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'KC', 'JC', 'QC']
    # for i in range(len(hand)-1):
def get_val(x):
    if x[0] == 'A':
        return 14
    elif x[0] == 'K':
        return 13
    elif x[0] == 'Q':
        return 12
    elif x[0] == 'J':
        return 11
    elif x[0] == 'T':
        return 10
    return int(x[0])
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    hand_temp = sorted(hand, key=get_val)
    for i  in range (len(hand)-1):
        if (get_val(hand_temp[i])+1) != (get_val(hand_temp[i+1])):
            print("False")
            return False
    print("True")
    return True


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    for i in range(len(hand)-1):
        if str(hand[i][1]) == str(hand[i+1][1]):
            print("True")
            return True
        else:
            print("False")
            return False

    

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example King of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best han

    elif is_straight(hand):
        return 1
    elif is_flush(hand):
        return 2
    if is_straight(hand) and is_flush(hand):
        return 3

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
