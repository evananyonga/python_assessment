# A function that adds 2 to a number

def addTwo(*nums):
    num = int(input("Please enter number "))
    for num in nums:
        print(num + 2)

num1 = 2
num2 = -10
addTwo(num1)
addTwo(num2)