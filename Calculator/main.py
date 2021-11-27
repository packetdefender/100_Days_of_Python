import art
import os
def cls(): return os.system('clear')


print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("Please enter a number: "))
    for symbol in operations:
        print(symbol)

    calc_on = True
    while calc_on:
        operation_symbol = input(
            "Pick an operation: ")
        num2 = float(input("Please enter another number: "))
        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        calc_more = input(
            f"Type 'Y' to continue calculating with {answer}, or type 'N' to exit: ").upper()
        if calc_more == "Y":
            num1 = answer
        else:
            cls()
            calc_on = False
            calculator()


calculator()
