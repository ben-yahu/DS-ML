import math
first = 'Ben'
last = 'Bernard'

# constructor
pizza = str('pepperoni')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

fullname = first + ' ' + last
print(fullname)

decade = str(2001)
print(decade)
print(type(decade))

statement = 'The first born into the millenial '+decade+"'s."
print(statement)

multiline = f'''
Hey, how are you,{first} {last}?
I was just learning some concepts. 
'''
print(multiline)

sentence = 'I\'m good thank you,\nKeep up the work Mr.'
print(sentence)

print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('was', 'am'))
print(multiline)

print(len(multiline))
multiline += '       '
multiline = '        '+multiline
print(len(multiline))
print(multiline)

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("\n")

title = 'menu'.upper()
print(title.center(20, '='))
print("Coffee".ljust(16, '.')+'$1'.rjust(4))
print("Muffin".ljust(16, '.')+'$4'.rjust(4))
print("CheeseCake".ljust(16, '.')+'$5'.rjust(4))
print("Tea".ljust(16, '.')+'$1'.rjust(4))
print('\n')

print(first[0:])
print(first.startswith('B'))
print(first.endswith('N'))
print(last.startswith('B'))
print(last.endswith('N'))

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

price = 1000
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

comp_value = 3+4j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

gpa = 38.28
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

zipcode = "452001"
zip_val = int(zipcode)
print(type(zip_val))
print(zip_val)
