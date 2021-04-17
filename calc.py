def sum(num1, num2):
	return num1 + num2
	
def sub(num1, num2):
	return num1 - num2

def div(num1, num2):
	return num1/num2

def mult(num1, num2):	
	return num1 * num2

print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")

select = int(input("Select operation: "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    sub(number_1, number_2))
  
elif select == 3:
    print(number_1, "/", number_2, "=",
                    div(number_1, number_2))
  
elif select == 4:
    print(number_1, "*", number_2, "=",
                    mult(number_1, number_2))
else:
    print("Invalid input")
