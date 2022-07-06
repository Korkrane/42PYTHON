class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


#  When you add the __init__() function, the child class will no longer
#  inherit the parent's __init__() function.
#  super() make the child class inherit all the methods and properties
# from its parent:
class Stark(GotCharacter):
    """A class representing the Stark family. \
        Or when bad things happen to good people.
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

    def __str__(self):
        return str(self)


arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)
