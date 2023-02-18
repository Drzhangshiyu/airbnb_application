import random
from random import randint

def print_instructions():
    print("Let's play pig!  Here are the rules:\n"
          "- You and the computer will take turns rolling a six-sided die as many times as you want, or until you roll a 6.\n"
          "- Each number you roll, except a 6, will be added to your score for that turn; but if you roll a 6, your score for that turn will be a 0, and your turn will end.\n"
          "- At the end of each turn, the score for that turn is added to your total score. The first player to reach or exceed 50 wins.\n"
          "- If you and the computer are tied with 50 or more, you'll each get another turn until the tie is broken.\n"
          "- The computer will go first!")

def computer_move(computer_score, human_score):
    #Defined how many times computer would roll
    com_play_numbers = random.randint(1,8) #computer random a nuimport random
from random import randint

def print_instructions():
    print("Let's play pig!  Here are the rules:\n"
          "- You and the computer will take turns rolling a six-sided die as many times as you want, or until you roll a 6.\n"
          "- Each number you roll, except a 6, will be added to your score for that turn; but if you roll a 6, your score for that turn will be a 0, and your turn will end.\n"
          "- At the end of each turn, the score for that turn is added to your total score. The first player to reach or exceed 50 wins.\n"
          "- If you and the computer are tied with 50 or more, you'll each get another turn until the tie is broken.\n"
          "- The computer will go first!")

def computer_move(computer_score, human_score):
    #Defined how many times computer would roll
    com_play_numbers = random.randint(1,8) #computer random a number from 1-8 and decided how many times wanna achieve.
    sum_com_rolling_score = 0    #initial sum of computer rolling score this run
    while com_play_numbers > 0: #com play chance
        com_play_numbers = com_play_numbers-1       #One rolled and reduce one chance to roll
        # computer called the roll function and return a number between 1-6
        com_roll_score = roll()
        print("The computer rolled a " + str(com_roll_score)) #show what computer rolled
        if com_roll_score != 6: #if not rolled a 6, sum up the computer rolling score and print the rolled number
            sum_com_rolling_score += com_roll_score
        else: # if rolled a 6, computer has 0 point this run and break the loop.
            sum_com_rolling_score = 0 #no score this run
            com_play_numbers = 0 #no chance to roll, break the loop and human's turn
    #end up computer rolling, added more score gained this run and return computer score
    computer_score += sum_com_rolling_score
    return computer_score

def human_move(computer_score, human_score):
    sum_human_rolling_score =0 #initial sum_human_rolling_score this run
    human_play_chance = 1 #human played at least once

    start_play = input("Ready to roll? (y/n)") #ask the player ready to play?
    if ask_yes_or_no(start_play) != False: #determine if the input is valid to start the game, if yes, start to play
        while human_play_chance > 0: #we have at least once to play
            human_play_chance -=1  # after one rolled, we reduced one chance to play
            human_roll_score = roll() #rolling...
            print("You rolled a {}.".format(human_roll_score))
            if human_roll_score != 6:
                sum_human_rolling_score += human_roll_score #sum up the score if not rolling a 6
                start_play = input("Do you want to roll again? (y/n)") #ask if wanna roll? if yes, human has one more chance to roll(human_play_chance added 1)
                if ask_yes_or_no(start_play) == True:
                    human_play_chance += 1
            else:
                sum_human_rolling_score = 0 # if rolled a six, no socre for this turn and no chance to play this turn
                human_play_chance = 0
        human_score += sum_human_rolling_score
    return human_score

def is_game_over(computer_score, human_score):
    #Returns True if either player has 50 or more, and the players are not tied,otherwise it returns False.
    if computer_score >= 50 or human_score >=50 and computer_score != human_score:
        return True
    else:
        return False

def roll():
    return random.randint(1,6) #Returns a random number in the range 1 to 6, inclusive.

def ask_yes_or_no(prompt):
    if prompt.startswith('Y') or prompt.startswith('y'): #if input string startswith y or Y, return T
        return True
    elif prompt.startswith('N') or prompt.startswith('n'): #if input string startswith n or N, return F
        return False
    else: #if Y/N or y/s not provided, re-ask the user to type the y/n
        prompt = input("Please enter (y/n) only!")
        return ask_yes_or_no(prompt)

def show_current_status(computer_score, human_score):

    score_difference = abs(computer_score-human_score) #calculated the difference betwwen computer_score and human_score

    if computer_score > human_score:
        print("The computer\'s score is {} and your score is {}. (You are {} points behind the computer.)".format(computer_score,human_score,score_difference))
    elif computer_score < human_score:
        print("The computer\'s score is {} and your score is {}. (You are {} points ahead of the computer.)".format(computer_score,human_score,score_difference))
    else: #tied
        print("The computer\'s score is {} and your score is {}. (You are tied with the computer.)".format(computer_score,human_score))

def show_final_results(computer_score, human_score):

    if computer_score > human_score: #calculated the difference betwwen computer_score and human_score
        print("You lost by {} points!".format(abs(computer_score - human_score)))
    elif computer_score < human_score:
        print("You won by {} points!".format(abs(computer_score - human_score)))

def main():

    print_instructions()

    game_running = True
    while game_running ==True: #game running automatically

        #to start the game
        input('Ready to play? (press any key) ')

        #set initial scores
        human_score = 0
        computer_score = 0
        game_over = False #the game is not over, we play the game

        while game_over == False: #unknown winner, so let's play the game

            #computer goes first
            computer_score = computer_move(computer_score, human_score) #computer play and return the computer_score
            show_current_status(computer_score, human_score) #show current status

            #human's turn
            human_score = human_move(computer_score, human_score) #human play and return human_score
            show_current_status(computer_score, human_score)

            # check if game is over, if over return True
            game_over = is_game_over(computer_score, human_score) #return true once the game is over and exit the while loop

        # show final results
        show_final_results(computer_score, human_score)
        # ask if wanna play again? if not, game_running = False and not re-enter the game_running loop
        if ask_yes_or_no(input("Want to play again?")) == False:
            game_running = False

    print("Bye!")#Say good bye!
if __name__ == '__main__':
    main()mber from 1-8 and decided how many times wanna achieve.
    sum_com_rolling_score = 0    #initial sum of computer rolling score this run
    while com_play_numbers > 0: #com play chance
        com_play_numbers = com_play_numbers-1       #One rolled and reduce one chance to roll
        # computer called the roll function and return a number between 1-6
        com_roll_score = roll()
        print("The computer rolled a " + str(com_roll_score)) #show what computer rolled
        if com_roll_score != 6: #if not rolled a 6, sum up the computer rolling score and print the rolled number
            sum_com_rolling_score += com_roll_score
        else: # if rolled a 6, computer has 0 point this run and break the loop.
            sum_com_rolling_score = 0 #no score this run
            com_play_numbers = 0 #no chance to roll, break the loop and human's turn
    #end up computer rolling, added more score gained this run and return computer score
    computer_score += sum_com_rolling_score
    return computer_score

def human_move(computer_score, human_score):
    sum_human_rolling_score =0 #initial sum_human_rolling_score this run
    human_play_chance = 1 #human played at least once

    start_play = input("Ready to roll? (y/n)") #ask the player ready to play?
    if ask_yes_or_no(start_play) == True: #determine if the input is valid to start the game, if yes, start to play
        while human_play_chance > 0: #we have at least once to play
            human_play_chance -=1  # after one rolled, we reduced one chance to play
            human_roll_score = roll() #rolling...
            print("You rolled a {}.".format(human_roll_score))
            if human_roll_score != 6:
                sum_human_rolling_score += human_roll_score #sum up the score if not rolling a 6
                start_play = input("Do you want to roll again? (y/n)") #ask if wanna roll? if yes, human has one more chance to roll(human_play_chance added 1)
                if ask_yes_or_no(start_play) == True:
                    human_play_chance += 1
            else:
                sum_human_rolling_score = 0 # if rolled a six, no socre for this turn and no chance to play this turn
                human_play_chance = 0
        human_score += sum_human_rolling_score
    return human_score

def is_game_over(computer_score, human_score):
    #Returns True if either player has 50 or more, and the players are not tied,otherwise it returns False.
    if computer_score >= 50 or human_score >=50 and computer_score != human_score:
        return True
    else:
        return False

def roll():
    return random.randint(1,6) #Returns a random number in the range 1 to 6, inclusive.

def ask_yes_or_no(prompt):
    if prompt.startswith('Y') or prompt.startswith('y'): #if input string startswith y or Y, return T
        return True
    elif prompt.startswith('N') or prompt.startswith('n'): #if input string startswith n or N, return F
        return False
    else: #if Y/N or y/s not provided, re-ask the user to type the y/n
        prompt = input("Please enter (y/n) only!")
        return ask_yes_or_no(prompt)

def show_current_status(computer_score, human_score):

    score_difference = abs(computer_score-human_score) #calculated the difference betwwen computer_score and human_score

    if computer_score > human_score:
        print("The computer\'s score is {} and your score is {}. (You are {} points behind the computer.)".format(computer_score,human_score,score_difference))
    elif computer_score < human_score:
        print("The computer\'s score is {} and your score is {}. (You are {} points ahead of the computer.)".format(computer_score,human_score,score_difference))
    else: #tied
        print("The computer\'s score is {} and your score is {}. (You are tied with the computer.)".format(computer_score,human_score))

def show_final_results(computer_score, human_score):

    if computer_score > human_score: #calculated the difference betwwen computer_score and human_score
        print("You lost by {} points!".format(abs(computer_score - human_score)))
    elif computer_score < human_score:
        print("You won by {} points!".format(abs(computer_score - human_score)))

def main():

    print_instructions()

    game_running = True
    while game_running ==True: #game running automatically

        #to start the game
        input('Ready to play? (press any key) ')

        #set initial scores
        human_score = 0
        computer_score = 0
        game_over = False #the game is not over, we play the game

        while game_over == False: #unknown winner, so let's play the game

            #computer goes first
            computer_score = computer_move(computer_score, human_score) #computer play and return the computer_score
            show_current_status(computer_score, human_score) #show current status

            #human's turn
            human_score = human_move(computer_score, human_score) #human play and return human_score
            show_current_status(computer_score, human_score)

            # check if game is over, if over return True
            game_over = is_game_over(computer_score, human_score) #return true once the game is over and exit the while loop

        # show final results
        show_final_results(computer_score, human_score)
        # ask if wanna play again? if not, game_running = False and not re-enter the game_running loop
        if ask_yes_or_no(input("Want to play again?")) == False:
            game_running = False

    print("Bye!")#Say good bye!
if __name__ == '__main__':
    main()