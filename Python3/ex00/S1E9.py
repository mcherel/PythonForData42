from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def is_alive(self):
        """Method to tell whether the character is alive"""
        pass

class Stark(Character):
    """Your docstring for Class"""

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for the Stark class.
        :param first_name: The first name of the character
        :param is_alive; Whether the charactr is alive
        """
        self.first_name = first_name
        self.is_alive = is_alive


    def is_alive(self):
        "Method to check if the character is alive"
        return self.is_alive


    def die(self):
        """method to mark character as dead"""
        self.is_alive = False

def main():
    try:
        hodor = Character("hodor")
    except TypeError as e:
        print(f"TypeError: {e}")

        
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

if __name__ == "__main__":
    main()

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
