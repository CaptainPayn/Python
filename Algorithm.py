while True:
    try:
        num = float(input('Enter a number(non-zero positive): '))
        if num < 1:
            print('Number must be a positive number')
        else:
            print(num)
    except ValueError:
        print('Input must be a number')

