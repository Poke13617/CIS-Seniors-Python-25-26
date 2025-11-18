"""
Personal Finance Manager
Program: personalFinance.py
Author: Mason Curtis
Date: 11/18/2025

This program demonstrates proper python program structure using a main function and helper functions to coordinate program flow
"""


def display_header():
    """Just displays the header, nothing more"""
    print("\n\n\n")
    print("=" * 50)
    print("             PERSONAL FINANCE MANAGER") 
    print("             Plan Your College Budget!")
    print("=" * 50)
    print()   

def get_user_name():
    name = input("What is your name?")
    return name

def get_income():
    print("\nEnter your monthly income: $", end="")
    income_str = input()
    income = float(income_str)
    return income

def get_expenses():
    print("\n--- EXPENSE TRACKING ---")

    expenses = {}

    print("Enter your rent/housing cost: $", end="")
    expenses['Rent/Housing'] = float(input())

    print("Enter your food/grocery budget: $", end="")
    expenses['Food/Groceries'] = float(input())

    print("Enter your transportation costs: $", end="")
    expenses['Transportation'] = float(input())

    print("Enter your entertainment budget: $", end='')
    expenses['Entertainment'] = float(input())

    print("What is your savings goal: $", end="")
    expenses['Savings'] = float(input())

    print("Enter miscellaneous expenses: $", end="")
    expenses['Miscellaneous'] = float(input())

    total = sum(expenses.value())

    return expenses, total
    

def calculate_reamining(income, expenses):
    pass

def provide_feedback(remaining, income):
    pass

def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    pass




def main():

    """
    Notice how main() reads like a story:
    1. display header
    2. get username
    3. get income
    4. get expenses
    5. calculate remaining
    6. give feedback
    7. display a summary
    8. say goodbye
    """

    display_header()
    print("Welcome! Let's track your monthly finances.\n")

    name = get_user_name()

    income = get_income()

    # This function below brings in TWO variables (tuple unpacking)

    expense_categories, total_expenses = get_expenses()

    remaining = calculate_reamining(income, expenses)

    feedback = provide_feedback(remaining, income)

    display_summary(name, income, expense_categories, total_expenses, remaining, feedback)








if __name__ == "__main__":
    main()