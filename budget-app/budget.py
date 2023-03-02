class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    # Creates the receipt-like output.
    def __repr__(self):
        calculation = (30 - len(self.category)) // 2
        if (calculation * 2) + len(self.category) == 30:
            header_asterisk = calculation *  "*"
        else:
            header_asterisk = (calculation * "*") + "*"
        header = header_asterisk + str(self.category) + (calculation * "*") + "\n"
        
        items = ""
        for entry in self.ledger:
            formatted_description = entry['description'][:23]
            formatted_amount = "{:.2f}".format(entry['amount'])
            spacing = (30 - (len(str(formatted_amount)) + len(formatted_description))) * " "
            line = f"{formatted_description}{spacing}{formatted_amount}"
            items += line + "\n"
        
        total = f"Total: {self.get_balance()}"
        return header + items + total
    
    def deposit(self, amount, description=False):
        if description:
            description = description
        else:
            description = ""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=False):
        if not description:
            description = ""

        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total_balance = 0
        for categories in self.ledger:
            total_balance += categories["amount"]
        return total_balance

    def transfer(self, amount, other_category):
        if self.get_balance() < other_category.get_balance():
            return False
        
        else:
            self.ledger.append({"amount": -amount, "description": f"Transfer to {other_category.category}"})
            other_category.deposit(amount, f"Transfer from {str(self.category)}")
            return True
        

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
        
    # Optional; used for the create_spend_chart function.
    def get_expense(self):
        expenses_list = []
        for item in self.ledger:
            if item['amount'] < 0:
                expenses_list.append(item['amount'])

        total_expenses = 0
        for expenses in expenses_list:
            total_expenses += abs(expenses)
        return total_expenses


# Creates the spend chart.
def create_spend_chart(categories):
    # Gets the total expenses.
    categories_total_expenses = []
    for category in categories:
        categories_total_expenses.append(category.get_expense())
    total_expense = 0
    for expense in categories_total_expenses:
        total_expense += expense
    
    # Gets the percentage by each category.
    percentage_by_category = []
    for category in categories:
        percentage = (category.get_expense() / total_expense) * 100
        round_num = round(percentage / 10) * 10
        percentage_by_category.append(round_num)
            
    
    header = "Percentage spent by category"
    # Creates the base chart.
    base_chart_by_line = []
    for line in range(10):
        if line == 0:
            base_chart_by_line.append(f"  {line * 0}|")    
        else:
            base_chart_by_line.append(f" {line * 10}|")
    base_chart_by_line.append("100|")
    base_chart_by_line.reverse()
    
    # Plotts the chart.
    count = 100
    plotted_chart = []
    for line in base_chart_by_line:
        first_column = "o" if percentage_by_category[0] >= count else " "
        second_column = "o" if percentage_by_category[1] >= count else " "
        third_column = "o" if percentage_by_category[2] >= count else " "
        count -= 10
        plotted_chart.append(f"{line} {first_column}  {second_column}  {third_column}  ")

    bottom_line = "    " + "-" * 10

    # Prints the vertical names under the chart.
    names = ""
    word1 = str(categories[0])
    word2 = str(categories[1]) if len(categories) > 1 else ""
    word3 = str(categories[2]) if len(categories) > 2 else ""
    
    max_len = max(len(word1), len(word2), len(word3))

    for position in range(max_len):
        column1 = word1[position] if position < len(str(word1)) else " "
        column2 = word2[position] if position < len(str(word2)) else " "
        column3 = word3[position] if position < len(str(word3)) else " "
        names += f"    {column1:<2} {column2:<2} {column3:<2} \n"

    return header + '\n' + '\n'.join(plotted_chart) + '\n' + bottom_line + '\n' + names

