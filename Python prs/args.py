import argparse
import RPS
import Guessnumber
import sys


def hello(name, lang):
    greeting = {
        'English': 'Hello',
        'Malayalam': 'Namaskaram',
        'Hindi': 'Namaste',
        'Tamil': 'Vanakkam'
    }
    usage = f'\n\n{greeting[lang]} {name}\n\n.'
    print(usage)
    value=True
    unt=0
    while value:
        title='Welcome to Arcade'
        ans=int(input(title.center(20,' ')+'\n\nSelect the game:\n1.Rock,Paper,Scissors\n2.Guess the number\n3.Quit\n'))
        for unt in range(3):
            if ans==1:
                RPS.main(name)
                break
            elif ans==2:
                Guessnumber.main()
                break
            elif ans==3:
                sys.exit()
            else:
                print('\nIncorrect option picked\nPlease Re-Enter\n')
                unt+=1
                break
        else:
            print('\nMaximum tries exceeded'+'\nQuitting...')
            sys.exit()



# if __name__=='__main__':
parser = argparse.ArgumentParser(description="Arcade Game")
parser.add_argument("-n", "--name", required=True, help='The name of the person to greet')
parser.add_argument('-l', '--lang',required=True, choices=['English', 'Malayalam', 'Hindi', 'Tamil'], help='The language of the greeting')
args = parser.parse_args()

hello(args.name, args.lang)
