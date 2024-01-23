#Question 1:
# Question no.01
def factorial(num):
      factorial = 1
      for i in range(1, num + 1):
          factorial *= i
      return factorial

  
num = int(input("Enter a number: "))

 
result = factorial(num)
print(f"The factorial of {num} is: {result}")

#--------------------------------------------------------
#Question no.02
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 * num2

print(f"The multiplication result of is: {result}")

#---------------------------------------------------------

#Question no.03
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))


if denominator != 0:
    
    quotient = numerator / denominator

    
    print(f"The quotient of dividing {numerator} by {denominator} is: {quotient}")
else:
    print("Error: Division by zero is undefined.")


