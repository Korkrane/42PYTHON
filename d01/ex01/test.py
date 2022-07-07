from game import Stark, GotCharacter

unknown = GotCharacter()
print(unknown.__dict__)

luigi = GotCharacter("Name", True)
print(luigi.__dict__)
print(luigi.__doc__)
print(vars(luigi))

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)

ned = Stark("Ned")
print(ned.__dict__)
