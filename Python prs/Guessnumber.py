import random
import sys


def guess(ply):
    print(f'\nYou picked {ply}')
    comp_choice = int(random.choice('123'))
    print(f'\nComputer picked {comp_choice}')
    compare(ply,comp_choice)

def compare(ply,comp_choice):
    if ply==comp_choice:
        print('\nYay! You guessed it right.')
    else:
        print('\nOops you guessed it wrong!')


def choice():
    title = '\nGuess the Number'
    print(title.center(20, ' '))
    playerchoice = input('\nEnter any number from 1 to 3\n')
    choice = int(playerchoice)
    return choice


def playagain():
    global count
    ans = input('\nDo you want to play again?'+'\nY for yes \nN for no\n')
    if ans.lower() == 'y':
        return True
    elif ans.lower() == 'n':
        return False
    else:
        print('\nWrong input'+'\nPlease try again')
        for count in range(3):
            count+=1
            continue
        else:
            print('\nMaximum tries exceeded'+'\nExiting')
            sys.exit()

def main():
    count = 0
    val = True
    while val:
        player = choice()
        if player not in [1, 2, 3]:
            for count in range(3):
                print('\nWrong option!'+'\nPlease try again')
                count += 1
                break
            else:
                print('\nMaximum tries exceeded'+'\nExiting')
                sys.exit()
        else:        
            guess(player)
            val=playagain()
   
if __name__ == '__main__':
    main()
