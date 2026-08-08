expenses = []
def add_expense():
    expense_name = input('Enter the expense name : ')
    expense_amount = int(input('Enter the amount of expense : '))
    expenses.append([expense_name, expense_amount])

def display_expenses():
    if not expenses:
        print('NO expense found!')
    else:
        for expense_name , expense_amount in expenses:
            print(f'{expense_name} : {expense_amount}')

def calculate_total():
    total = 0
    for expense_name, expense_amount in expenses:
        total += expense_amount
    return total

while True:
    print('\n-----> Expense Tracker <-----\n')
    print('1.Add Expense')
    print('2.Display Expense')
    print('3.Calculate Expense')
    print('4.Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        add_expense()
    elif choice == 2:
        display_expenses()
    elif choice == 3:
        print(f'Total expense : {calculate_total()}')
    elif choice == 4:
        print('Thanks for using expense tracker!')
        break
    else:
        print('Enter a valid choice!')