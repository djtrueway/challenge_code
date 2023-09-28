class Category:

    def __init__(self, category: str):
        """_summary_

        Args:
          category (str): _description_ the name of category
        """
        self.category = category
        self.ledger = []

    def deposit(self, amount: int, description: str = "") -> None:
        """method for add money to the category

        Args:
            amount (int): _description_
            description (str, optional): _description_. Defaults to "".
        """
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self) -> float:
        """return the balance of the category

        Returns:
            float: _description_
        """
        return sum([item['amount'] for item in self.ledger])

    def check_funds(self, amount: int) -> bool:
        """check is funds is disponible

        Args:
            amount (int): _description_

        Returns:
            bool: _description_
        """
        return self.get_balance() >= amount

    def withdraw(self, amount: int, description: str = "") -> bool:
        """method for withdraw from the category

        Args:
            amount (int): _description_
            description (str, optional): _description_. Defaults to "".

        Returns:
            bool: _description_
        """

        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount: int, category_budget: object) -> bool:
        """
        method for transfert money for another category

        Args:
            amount (int): _description_ the amount to transfert
            category_budget (object): _description_ object category who will be add the money

        Returns:
            bool: _description_
        """
        if self.withdraw(amount,
                         description=f"Transfer to {category_budget.category}"):
            category_budget.deposit(amount,
                                    description=f"Transfer from {self.category}")
            return True
        return False

    def __str__(self):
        """_summary_ representation the object in str format
        """
        title = f'{self.category.center(30, "*")}\n'
        row_ledger = [list(value.values()) for value in self.ledger]
        line = ''
        for item in row_ledger:
            row = f'{item[1].ljust(23)[:23]} {"{:.2f}".format(float(item[0]))[:7]}\n'
            line += row
        return f'{title}{line}Total: {self.get_balance()}'


def create_spend_chart(categories: str) -> str:
    """_summary_ . function return a string that is a bar chart. 

    Args:
        categories (str): _description_ list of categories as an argument  
    Returns:
        str: _description_ return a string that is a bar chart.
    """
    
    chart = "Percentage spent by category\n"
    spendings = [
        sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        for category in categories
    ]
    total_spent = sum(spendings)
    percentages = [(spending / total_spent) * 100 for spending in spendings]

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            chart += "o" if percentage >= i else " "
            chart += "  "
        chart += "\n"

    chart += "    ----------\n"

    # Find the longest category name
    max_len = max(len(category.category) for category in categories)

    # Create vertical bars with category names
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"  # Add a newline after each vertical bar, except the last one

    return chart
