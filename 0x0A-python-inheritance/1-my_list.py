#!/usr/bin/python3

"""

1-my_list.py

MyList(list)

"""





class MyList(list):

    """

    A class that inherits from list

    """

    def print_sorted(self):

        """

        Prints the list in ascended sort

        """

        print("{}".format(sorted(self)))
