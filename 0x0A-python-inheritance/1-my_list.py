"""
The module contain the
Mylist class which is a
sub class of list
"""


class MyList(list):
    """
    The class initialises
    it parent class and
    contain method to
    print the list.
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
