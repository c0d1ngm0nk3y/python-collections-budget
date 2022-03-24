from . import Expense

# import matplotlib.pyplot as plt


def check_sets(x, y):
    print()
    print(len(x), len(y))
    if x.issubset(y):
        print("x is subset of y")
    if y.issubset(x):
        print("y is subset of x")
    for e1, e2 in zip(x, y):
        if e1.amount != e2.amount:
            print(e1.amount, e2.amount)


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if divided_for_loop != divided_set_comp:
        print("Sets are NOT equal by == test")

    [a, b, c] = divided_for_loop
    [d, e, f] = divided_set_comp

    check_sets(a, d)
    check_sets(b, e)
    check_sets(c, f)

    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")


if __name__ == "__main__":
    main()
