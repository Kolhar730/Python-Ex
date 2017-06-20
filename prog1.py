#Variation 1

"""a = input('Enter the number A: ')
b = input('Enter the number B: ')

sumTotal = int(a) + int(b)
diff = int(a) - int(b)
product = int(a) * int(b)

print('The sum of {0} and {1} is {2}'.format(a, b, sumTotal))
print('The difference of {0} and {1} is {2}'.format(a, b, diff))
print('The product of {0} and {1} is {2}'.format(a, b, product))"""

#Variation 2

a = input('Enter the number A: ')
b = input('Enter the number B: ')

print('The sum of {0} and {1} is {2}'.format(a, b, eval('a+b')))
print('The difference of {0} and {1} is {2}'.format(a, b, eval('a-b')))
print('The prduct of {0} and {1} is {2}'.format(a, b, eval('a*b')))

