class Category:
    """docstring for ClassName."""

    def __init__(self, category):
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
        """return the balance category

        Returns:
            float: _description_
        """
        return sum([total['amount'] for item in self.ledger])

    def check_funds(self, amount: int) -> bool:
        """check is funds is disponible

        Args:
            amount (int): _description_

        Returns:
            bool: _description_
        """
        if amount.isdigit():
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
            amount (int): _description_
            category_budget (object): _description_

        Returns:
            bool: _description_
        """
        if self.withdraw(amount, description=f"Transfert vers [Catégorie budgétaire de {category_budget.category}] "):
            category_budget.deposit(
                amount, description=f"Transfert vers [Catégorie budgétaire de {self.category}] ")
            return True
        return False

    def __str__(self):
        pass
