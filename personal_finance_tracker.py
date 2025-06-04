import json
import argparse


def save_data(filename='finance_data.json'):
    with open(filename, 'w') as f:
        json.dump(finance_data, f, indent=4)

def load_data(filename='finance_data.json'):
    global finance_data
    try:
        with open(filename, 'r') as f:
            finance_data = json.load(f)
    except FileNotFoundError:
        finance_data={
            'income':[],
            'expense':[]
        }




finance_data = {
    'income': [],
    'expense': []
}

def add_income(amount, category, date, note=""):
    transaction = {
        'amount': amount,
        'category': category,
        'date': date,
        'note': note
    }
    finance_data['income'].append(transaction)


def add_expense(amount, category, date, note=""):
    transaction = {
        'amount': amount,
        'category': category,
        'date': date,
        'note': note
    }
    finance_data['expense'].append(transaction)

def show_transaction(transaction_type):
    for i in finance_data[transaction_type]:
        print(f"{i['date']} - {i['category']}: ${i['amount']} | {i.get('note', '')}") 


def show_summary():
    total_income = sum(t['amount'] for t in finance_data['income'])
    total_expenses = sum(t['amount'] for t in finance_data['expense'])
    balance = total_income - total_expenses

    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Net Balance: ${balance}")

def main():
    load_data()

    parser = argparse.ArgumentParser(description="Personal Finance Tracker")

    parser.add_argument('--add-income', nargs=3, metavar=('amount', 'category', 'date'))
    parser.add_argument('--add-expense', nargs=3, metavar=('amount', 'category', 'date'))    
    parser.add_argument('--show-summary', action='store_true')    
    parser.add_argument('--show-history', choices=['income', 'expense'])

    args = parser.parse_args()
    data_changed = False

    if args.add_income:
        amount = float(args.add_income[0])
        category = args.add_income[1]
        date = args.add_income[2]
        add_income(amount, category, date)
        data_changed = True

    if args.add_expense:
        amount = float(args.add_expense[0])
        category = args.add_expense[1]
        date = args.add_expense[2]
        add_expense(amount, category, date)
        data_changed = True

    if args.show_summary:
        show_summary()

    if args.show_history:
        show_transaction(args.show_history)

    if data_changed:
        save_data()

if __name__ == "__main__":
    main()        