#odd even
number1=int(input("Please Enter a number to check if it is od or even: "))
if(number1%2==0):
    print(number1, " is even")
else:
    print(number1, " is odd")


#greatest
max=0
for i in range(0,3):
    number2=int(input("Please enter number "))
    if max<=number2:
        max=number2
print("The greatest of three numbers is ",max)

#multiple of 7
number3=int(input("Please enter a new number for checking multiple of 7: "))
if(number3%7==0):
    print("The number ",number3," is multiple of 7.")
else:
    print("The number ",number3," is not a multiple of 7.")