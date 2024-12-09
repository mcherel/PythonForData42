from abc import ABC, abstractmethod


class Character(ABC):


    """Your docstring for Class"""
    @abstractmethod
    def is_alive(self):
        """Method to tell wether the character is alive"""
        pass

class Stark(Character):


    """Your docstring for Class"""
    def is_alive(self):
        return True


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
"""4
Training Piscine Python for datascience - 3 Oriented Object Programming
Expected output: (docstrings can be different)
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>"""

if __name__ == "___main__":
    main()