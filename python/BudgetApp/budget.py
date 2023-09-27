# -*- coding: utf-8 -*-


class Category:
    """_summary_
    """

    def __init__(self, category: str):
        """_summary_

        Args:
            category (str): _description_
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

    def withdraw(self,  amount: int, description: str = "") -> bool:
        """method for withdraw from the category

        Args:
            amount (int): _description_
            description (str, optional): _description_. Defaults to "".

        Returns:
            bool: _description_
        """

        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": description})
            return True
        return False

    def transfert(self, amount: int, category_budget: object) -> bool:
        """
        method for transfert money for another category

        Args:
            amount (int): _description_ the amount to transfert
            category_budget (object): _description_ object category who will be add the money

        Returns:
            bool: _description_
        """
        if self.withdraw(amount, description=f"Transfert vers [Catégorie budgétaire de {category_budget.category}] "):
            category_budget.deposit(
                amount, description=f"Transfert vers [Catégorie budgétaire de {self.category}] ")
            return True
        return False

    def __str__(self):
        """_summary_ representation the object in str format
        """
        title = f'{self.category.center(30, "*")} \n'
        row_ledger = [list(value.values()) for value in self.ledger]
        line = ''
        for item in row_ledger:
            row =  f'{item[1].ljust(23)} {str(item[0])[0:7]}\n'
            line = line + row
        return f'{title} {line} '



food = Category(category="Food")
food.deposit(1000, "initial deposit")
food.withdraw(10, "groceries")
food.withdraw(15, "restaurant and more foo")

print(food)
