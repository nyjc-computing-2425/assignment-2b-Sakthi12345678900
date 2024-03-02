num = input('Enter a number (decimal only): ')
# type your code here
decimal_point = num.find('.')
num1 = (num[decimal_point:])
num2 = num1.replace('.','').strip()
dp = len(num2)
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
