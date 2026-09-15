#Program 1: Sum2Num
#Description: Take an input of 2 numbers, add them and print them.

print("\nCase 1: Type Casting the input variables within the input section")

first  = int(input("Enter first number: "))
second = int(input("Enter second number: "))
sum_case1 = first + second

print("\nCase 2: Type Casting the input variables in the calculation section")

a = input("Enter first number: ")
b = input("Enter second number: ")

sum_case2 = int(b) + int(b)

#Method 1: Type Cast variable 'sum' within print statement, when concatenating with another statement
print("The sum of both numbers, for case 1: " + str(sum_case1))
print("The sum of both numbers, for case 2: " + str(sum_case2) + "\n")
#Method 2: Normal printing of variable 'sum'
print(sum_case1)
print(sum_case2)