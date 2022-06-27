import sys

finalString = ""
inputArgs = sys.argv

for i in inputArgs[:0:-1]:
    finalString = ""
    for letter in i[::-1]:
        if letter.isupper() == True:
            finalString += letter.lower()
        elif letter.islower() == True:
            finalString += letter.upper()
        else:
            finalString += letter
    print(finalString, end=" ")
print()