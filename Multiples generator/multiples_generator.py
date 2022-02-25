while True:

    a = input('enter value:')
    b = input('enter how many multiple:')
    b=int(b)
    a=int(a)
    print('find multiples of', a)
    print('this many times:', b)
    for i in range (1, b+1):
        i=int(i)
        print ('{0} x {1} = {2}'.format(a, i, a*i))
    print('Do you want to exit:')
    c=input('yes or no:')
    if c =='yes':
        break


