import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 2:
        assert sys.argv[1].isdigit(), "argument is not integer"
        num = int(sys.argv[1])
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as e:
    print("AssertionError:", e)
