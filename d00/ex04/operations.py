import sys

def usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
    exit()

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
    elif len(args) >= 3:
        print("InputError: too many arguments\n")
        usage()

    try:
        val1 = int(args[0])
        val2 = int(args[1])
        print("Sum:\t\t", val1 + val2)
        print("Difference:\t", val1 - val2)
        print("Product:\t", val1 * val2)

        if(val2 != 0):
            print("Quotient:\t", val1 / val2)
            print("Remainder:\t", val1 % val2)
        else:
            print("Quotient:\t", "ERROR (div by zero)")
            print("Remainder:\t", "ERROR (modulo by zero)")
    except ValueError:
        print("InputError: only numbers\n")
        usage()

if __name__ == "__main__":
    main()