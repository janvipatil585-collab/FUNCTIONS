# check weather number is even or odd using functions

def check_even_odd(n):
    if(num%2==0):
        print('number is even')
    else:
        print('number is odd')
        num=int(input('enter a number:'))
        check_even_odd(num)

