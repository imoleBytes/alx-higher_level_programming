#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """this class inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.print_sorted()
    li2.print_sorted()
