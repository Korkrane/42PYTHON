import time
from random import randint
import os


# https://ankitbko.github.io/blog/2021/04/logging-in-python/#:~:text=A%20decorator%20is%20a%20function,can%20be%20subject%20of%20assignment.

def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        t = open("machine.log", "a")
        action = " ".join(map(str.capitalize, func.__name__.split('_'))).ljust(19, ' ')
        t.write(f"({os.environ['USER']})Running: {action}[ exec-time = {end:.3f}{'s' if end > 1 else 'ms'} ]\n")
        t.close()
        return result
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
