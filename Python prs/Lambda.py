class sweets:
    def __init__(self, company, type1, cost):
        self.company = company
        self.type1 = type1
        self.cost = cost

    def company_name(self):
        print(f'\nThe company is:{self.company}')

    def type_name(self):
        print(f'\nThe type is:{self.type1}')

    def cost_count(self):
        print(f'\nThe cost is:{self.cost}')
        return self.cost


class chocolate(sweets):
    def __init__(self, company, type1, cost, color):
        super().__init__(company, type1, cost)
        self.color = color

    def color_type(self):
        print(f'\nThe color is:{self.color} chocolate')


class candy(sweets):
    def __init__(self, company, type1, cost, shape):
        super().__init__(company, type1, cost)
        self.shape = shape

    def shape_type(self):
        print(f'\nThe shape of the candy is:{self.shape}')


class lollipop(sweets):
    def __init__(self, company, type1, cost, flavour):
        super().__init__(company, type1, cost)
        self.flavour = flavour

    def flavour_name(self):
        print(f'\nThe flavour of the candy is:{self.flavour}')

def main():
    Companies = ['Cadbury', 'Toblerone', 'Alpenliebe']
    Types = ['Dairy Milk', 'White', 'Bubble']
    Cost = ['100', '200','140']
    count=1
    value=True
    while value:
     v = 0
     for v in range(4):
        first = chocolate(Companies[v], Types[v], Cost[v], 'Dark')
        v += 1
        second = candy(Companies[v], Types[v], Cost[v], 'Triangle')
        v += 1
        third = lollipop(Companies[v], Types[v], Cost[v], 'Strawberry')
        v += 1
        break
     def answer(name):
         k=0
         nonlocal ans
         if ans.lower()=='y':
            print('\nGreat Choice!\n\nPacking the product...\nDone.')
            cost_paid=name.cost_count()
            inp=input(f'\nPlease pay:\n')
            if inp==cost_paid:
                print('\nTransaction Successful!')
                return 'repeat'
            else:
                print('\nSorry! you have not paid the required amount.\nPlease try again.')
                k+=1
                if k==2:
                    print('\nYou can\'t proceed.')
                    return 'repeat'
         elif ans.lower()=='n':
                return 'repeat'
         else:
            return 'repeat'
     option=int(input('\nWhat do you want?\n1.Chocolate\n2.Candy\n3.Lollipop\n'))
     if option==1:
      name_1=first
      print('\nThe Available product is: \n')
      name_1.company_name()
      name_1.type_name()
      name_1.cost_count()
      name_1.color_type()
      ans=input('\nDo you want to buy it?\nY for yes\nN for no\n')
      value=answer(first)
      if value=='repeat':
        again=1
        for again in range(3):
            answ=input('\nDo you want anything else\nY for yes\nN for no\n')
            if answ.lower()=='y':
                value=True
                break
            elif answ.lower()=='n':
                value=False
                break
            else:
                print('\nWrong Option!')
                again+=1
                                                                
        else:
            print('\nMaximum Tries exceeded')
            print('\nPlease Leave.')
            value=False
            return value
    
     elif option==2:
        name_2=second
        print('\nThe Available product is: \n')
        name_2.company_name()
        name_2.type_name()
        name_2.cost_count()
        name_2.shape_type()
        ans=input('\nDo you want to buy it?\nY for yes\nN for no\n')
        value=answer(second)
        if value=='repeat':
            again=1
            for again in range(3):
                answ=input('\nDo you want anything else\nY for yes\nN for no\n')
                if answ.lower()=='y':
                    value=True
                    break
                elif answ.lower()=='n':
                    value=False
                    break
                else:
                    print('\nWrong Option!')
                    again+=1
                                                                
        else:
            print('\nMaximum Tries exceeded')
            print('\nPlease Leave.')
            value=False
            return value
     elif option==3:
        name_3=third
        print('\nThe Available product is: \n')
        name_3.company_name()
        name_3.type_name()
        name_3.cost_count()
        name_3.flavour_name()
        ans=input('\nDo you want to buy it?\nY for yes\nN for no\n')
        value=answer(third)
        if value=='repeat':
            again=1
            for again in range(3):
                answ=input('\nDo you want anything else\nY for yes\nN for no\n')
                if answ.lower()=='y':
                    value=True
                    break
                elif answ.lower()=='n':
                    value=False
                    break
                else:
                    print('\nWrong Option!')
                    again+=1
                                                                    
        else:
            print('\nMaximum Tries exceeded')
            print('\nPlease Leave.')
            value=False
            return value
     else:
        print('\nWrong option please choose again!')
        if count==3:
            print('\nTries exceeded'+'\nAborting...')
            value=False
            return value
        count+=1
    else:
     print('\nThankyou for visiting\nHave a great day!\n')

if __name__ == '__main__':
    main()
