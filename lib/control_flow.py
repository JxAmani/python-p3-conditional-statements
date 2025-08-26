#!/usr/bin/env python3
def admin_login(username, password):
    # Check if username is "admin" (any case) AND password is correct
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    # Check ranges of temperature
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    # Multiples of both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    try:
        # Use dictionary mapping instead of a long if/elif chain
        operations = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": num1 / num2
        }
        return operations[operation]
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except KeyError:
        print("Invalid operation!")
        return None
