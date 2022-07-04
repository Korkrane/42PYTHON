import sys

for i, arg in enumerate(sys.argv[:0:-1]):
    finalString = ""
    for letter in arg[::-1]:
        if letter.isupper():
            finalString += letter.lower()
        elif letter.islower():
            finalString += letter.upper()
        else:
            finalString += letter
    if i != len(sys.argv) - 2:
        print(finalString, end=" ")
    else:
        print(finalString, end="")

if len(sys.argv) > 1:
    print()
