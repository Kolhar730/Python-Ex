a = input('Enter the number 1: ')
b = input('Enter the number 2: ')

div1 = int(a) // int(b)
div2 = float(a) / float(b)

print('The integer quotient of {0} and {1} is {2}'.format(a, b, div1))
print('The floating quotient of {0} and {1} is {2}'.format(a, b, div2))