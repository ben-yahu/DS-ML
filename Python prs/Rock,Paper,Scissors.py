import sys
import random
import Basic

def choicepick():
    global string
    global name
    ent=f'Welcome to Rock, Paper, Scissors {name}.'
    playerchoice = input('\n'+string.center(20,'_')+'\n\n'+ent.center(20,' ')+'\n'+string.center(20,'_')+'\nPlease choose'+'\n\n1 for Rock\n2 for Paper\n3 for Scissors\n'+ string.center(20,'_')+'\n\n')
    print(string.center(20,'_'))
    choice = int(playerchoice)
    choiceite(choice)
    return choice


def yesorno(ans):
    global string
    global name
    if ans.lower() == 'y':
        main()
    elif ans.lower() == 'n':
        print(string.center(20,'_'))
        print('\n...Okay exiting...')
        print(string.center(20,'_'))
        sys.exit()
    else:
        print(f"\n!!!Please pick up a correct option {name}!!!")
        return 'r'


def choiceite(choice):
    global string
    if choice < 1 or choice > 3:
        print(f'\n!!!The option is invalid {name}!!!')
        print(string.center(20,'_'))
        ans = input(f'\nDo you want to continue {name}?\n'+string.center(20,'_')+'\n\nPress Y for yes\nPress N for no\n'+string.center(20,'_')+'\n\n')
        print(string.center(20,'_'))
        ret = yesorno(ans)
        if ret == 'r':
         choicepick()


def choiceran(choice):
    values = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    choice_1 = int(choice)
    pickval = str(values.get(choice_1))
    print(f'\n{name}, You picked {pickval}.')
    comp = int(random.choice([1, 2, 3]))
    comppick = str(values.get(comp))
    print(f'\nComputer picked {comppick}.')
    print(string.center(20,'_'))
    return comp


def iterate():
    global string
    global name
    i = 1
    for i in range(5):
        print(string.center(20,'_'))
        answer = input(f'\nWanna keep playing {name}?\n\nY for yes\nN for no\n'+string.center(20,'_')+'\n\n')
        print(string.center(20,'_'))
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            print(f"\n!!!Thanks for playing {name}!!!")
            return False
        else:
            print('\n!!!Wrong Input!!!')
        i += 1
        if i == 4:
            print('\n!!!Maximum tries reached!!!')
            print('\n!!!Exiting!!!')
            print(string.center(20,'_'))
            sys.exit()


def main():
    game_count=1
    player_win=0
    comp_win=0
    draw=0
    value = True
    while value:
        player = choicepick()
        comp = choiceran(player)
        
        def g_wins(*args):     
            nonlocal game_count
            nonlocal player_win
            nonlocal comp_win
            nonlocal draw
            if player == comp:
                print('\n😉 The game is a Draw!!!')
                draw+=1
            elif (player == 1 and comp == 2) or (player == 3 and comp == 1) or (player == 2 and comp == 3):
                print('\n😏 Computer Won!')
                comp_win+=1
            elif (player == 2 and comp == 1) or (player == 1 and comp == 3) or (player == 3 and comp == 2):
                print(f'\n😎 {name}, You Won!')
                player_win+=1
            print(string.center(20,'_'))
            print(f'\nGame Count:{game_count}')
            game_count+=1
            print(f'{name}\'s win count:{player_win}')
            print(f'Computer win count:{comp_win}')
            print(f'Draw count:{draw}')

        g_wins(player,comp)
        value = iterate()
    else:
        bye='Bye'
        print('\n'+bye.center(20,'-'))
        print(string.center(20,'_'))
        sys.exit()


if __name__ == "__main__":
    string='_'
    name='Player'
    name = Basic.args.name
    main()
