from . import Expense
import collections
import matplotlib.pyplot as plot


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")
    spending_categories = []
    for expense in expenses.list:
        spending_categories.append(expense.category)

    counter = collections.Counter(spending_categories)
    print(f"{len(spending_categories)} categories")
    top5 = counter.most_common(5)
    print(top5)
    categories, count = zip(*top5)
    print("")
    print(categories)
    print(count)
    figure, axes = plot.subplots()
    axes.bar(categories, count)
    axes.set_title("# of Purchases by Category")
    plot.show()


if __name__ == "__main__":
    main()
