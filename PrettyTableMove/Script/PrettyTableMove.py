__version__ = "2023.05.06.01"
__author__ = "Muthukumar Subramanian"

'''
Python Pretty Table Move Utility, the pretty table will display based on the user 
specified position [left side or right side].
'''

from prettytable import PrettyTable
import shutil


class PrettyTableMove:
    def __init__(self, table_obj):
        self.table_obj = table_obj
        # Get the console window width
        self.console_width = shutil.get_terminal_size().columns
        # Set the max width for the table
        self.table_obj.max_width = self.console_width
        # Set table of current width
        self.table_obj._title_width = self.console_width - 4

    def move_table_lft_ryt_center(self, move_size=0):
        table_str = self.table_obj.get_string().split('\n')
        table_str_width = max(len(line) for line in table_str)
        if move_size <= 0:
            padding = ' ' * abs(move_size)
            table_str = [line + padding for line in table_str]
        elif move_size > 0:
            padding = ' ' * move_size
            table_str = [padding + line for line in table_str]
        else:
            padding = ' ' * ((self.console_width - table_str_width) // 2)
            table_str = [padding + line for line in table_str]

        # Print the table with user specified position
        print('\n'.join(table_str))


if __name__ == "__main__":
    # Create Table Object
    table = PrettyTable()
    # Set the title
    table.title = "My Table"

    # Set the column headers and rows
    table.field_names = ["Name", "Age", "Gender"]
    table.add_row(["Muthu", 28, "Male"])
    table.add_row(["Kumar", 32, "Male"])
    cls_obj = PrettyTableMove(table)

    # Scenario-1 - Move Center Position as "40"
    print("{:*^30}".format(" Scenario-1 Start "))
    cls_obj.move_table_lft_ryt_center(move_size=40)
    print("{:*^30}".format(" Scenario-1 End "))

    # Scenario-2 - Move Left to Right side
    print("{:*^30}".format(" Scenario-2 Start "))
    for i in range(0, 100, 20):
        print(f"Position: {i}")
        cls_obj.move_table_lft_ryt_center(move_size=i)
    print("{:*^30}".format(" Scenario-2 End "))

    # Scenario-3 - Move Right to Left side
    print("{:*^30}".format(" Scenario-3 Start "))
    for i in reversed(range(0, 100, 20)):
        print(f"Position: {i}")
        cls_obj.move_table_lft_ryt_center(move_size=i)
    print("{:*^30}".format(" Scenario-3 End "))
