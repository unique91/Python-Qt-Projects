
num1 = int(input('Input 1st number: '))
num2 = int(input('Input 2st number: '))
operator = input('Input an operator (+, -, *, /): ')

res = 0
if operator == '+':
    res = num1 + num2
elif operator == '-':
    res = num1 - num2
elif operator == '*':
    res = num1 * num2
elif operator == '/':
    res = num1 / num2
else:
    print(f"{operator} is not a valid operator!")

print('(%d %s %d) = %d' % (num1, operator, num2, res))
