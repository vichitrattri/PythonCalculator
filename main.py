# Clear Function
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print("Welcome to Command Line Calculator!\nSample Inputs: 2+2 ↩ | 4*2 ↩ | 6-2 ↩ | 9/3 ↩")

operations = ["+", "-", "/", "*"]
user_input = input("\nWrite your query 👇 \n")

def find_operator():
  for operator in operations:
    z = (user_input.find(operator))
    if z > 0:
      return operator

operator = find_operator()

user_input_list = user_input.split(f"{operator}")
number1 = int(user_input_list[0])
number2 = int(user_input_list[1])

#Defining All Operators
def add(number1, number2):
  answer =  number1 + number2
  print(answer)
def subtract(number1, number2):
  answer =  number1 - number2
  print(answer)
def multiply(number1, number2):
  answer =  number1 * number2
  print(answer)
def divide(number1, number2):
  answer =  number1 + number2
  print(answer)

#Singular
def singular():
  if operator == "+":
    add(number1, number2)
  elif operator == "-":
    subtract(number1, number2)
  elif operator == "*":
    multiply(number1, number2)
  elif operator == "/":
    divide(number1, number2)

on = True

while on:
  singular()
  resume = input("Press Enter to continue; 0 to Clear ")
  if not resume ==  "0":
    user_input_list = []
    user_input = input("Write your query 👇 \n")
    operator = find_operator()
    user_input_list = user_input.split(f"{operator}")
    number1 = int(user_input_list[0])
    number2 = int(user_input_list[1])
  else:
    clear()


