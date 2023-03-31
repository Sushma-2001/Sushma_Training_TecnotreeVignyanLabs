# A simple calculator program in Python

# Function to add two numbers
def add(a, b):
   return a + b

# Function to subtract two numbers
def subtract(a, b):
   return a - b

# Function to multiply two numbers
def multiply(a, b):
   return a * b

# Function to divide two numbers
def divide(a, b):
   return a / b

# Function of modulus of two numbers
def mod(a, b):
   return a % b

# Main function
def main():
   print("Welcome to the Calculator!")
   print("Select an operation to perform:")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   print("5. Modulus")

   # Get user input for the operation
   while True:
       choice = input("Enter choice (1/2/3/4/5): ")
       if choice in ['1', '2', '3', '4' ,'5']:
           break
       print("Invalid input")


   n1 = int(input("Enter first number: "))
   n2 = int(input("Enter second number: "))

   if choice == '1':
      print(n1,"+",n2,"=", add(n1,n2))

   elif choice == '2':
      print(n1,"-",n2,"=", subtract(n1,n2))

   elif choice == '3':
      print(n1,"*",n2,"=", multiply(n1,n2))

   elif choice == '4':
      if n2 == 0:
          print("Error: division by zero")
      else:
          result = divide(n1, n2)
          print(n1,"/",n2,"=", divide(n1,n2))

   elif choice == '5':
      print(n1,"%",n2,"=", mod(n1,n2))
          
   else:
      print("Invalid input")
       
# Call the main function
main()
