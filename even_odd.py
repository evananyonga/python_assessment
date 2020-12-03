# An even or odd function

def even_odd(num):
    num = int(input("Please enter number "))
    if num % 2 == 0:
        print(num/2)
    else:
        print(num * 2)
num1 = -40
even_odd(num1)