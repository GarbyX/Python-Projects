
print('Simple Calculator')
while True:
        b = float(input('First Number: '))
        c = input('Choose Operator: ')
        d = float(input('Second Number: '))
        if c == '+':
            print(b + d)
        elif c == '-':
            print(b - d)
        elif c == '*':
            print(b * d)
        elif c == '/':
            print(b / d)
        elif c == '%':
            print(b % d)
        elif c == '//':
            print(b // d)
        q = input('do you want to continue?: ')
        if q == 'y':
            continue
        else:
            break
