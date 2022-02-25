
while True:
    try:
        a = (input('Enter min number: '))
        x = (input('Enter max number: '))
        z = (input('Enter even or odd: '))

    except ValueError:
        print('you hav entered an invalid number')
    a = int(a)
    x = int(x)
    try:
        if z == 'even':
            print(f'Printing even numbers from {a} to {x}')
            for b in range(a-1, x+1):
                if b % 2 == 0:
                    print('Number is even', b)
        elif z =='odd':
            print(f'Printing odd numbers from {a} to {x}')
            for b in range(a-1, x+1):
                if b % 2 != 0:
                    print('Number is odd', b)
        else:
            print(f"The value {z} is not a valid option")

    except ValueError:
            print("you have entered an invalid option")

    print('Do you want to exit:')
    c=input('yes or no:')
    if c =='yes':
        break



