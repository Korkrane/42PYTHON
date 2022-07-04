import string


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""

    if len(args) >= 2:
        print("ERROR")
        return
    elif len(args) == 0:
        print("Type the text you want to analyze")
        myString = input()
    else:
        myString = args[0]
    upperCount = 0
    lowerCount = 0
    spaceCount = 0
    puncCount = 0
    for i in myString:
        if i.islower():
            lowerCount += 1
        elif i.isupper():
            upperCount += 1
        elif i.isspace():
            spaceCount += 1
        elif i in string.punctuation:
            puncCount += 1

    print("The text contains " + str(len(myString)) + " characters:")
    print("- " + str(upperCount) + " upper letters")
    print("- " + str(lowerCount) + " lower letters")
    print("- " + str(puncCount) + " punctuation marks")
    print("- " + str(spaceCount) + " spaces")
