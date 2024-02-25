def hello(name,lang):
    greeting={
        'English':'Hello',
        'Malayalam':'Namaskaram',
        'Hindi':'Namaste',
        'Tamil':'Vanakkam'
    }
    usage=f'\n\n{greeting[lang]}.'
    print(usage)

# if __name__=='__main__':
import argparse

parser = argparse.ArgumentParser(
    description="Says hello."
)
parser.add_argument(
    "-n", "--name",required=True, help='The name of the person to greet'
)
parser.add_argument(
    '-l', '--lang',required=True,choices=['English','Malayalam','Hindi','Tamil'],help='The language of the greeting'
)

args = parser.parse_args()
hello(args.name,args.lang)
