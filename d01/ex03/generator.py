import random


# shuffle randomly the word list
# https://stackoverflow.com/questions/17489477/shuffle-a-python-list-without-using-the-built-in-function
def shuffle(text):
    for i in range(len(text) - 1, 0, -1):
        other = random.randint(0, i)
        if other == i:
            continue
        text[i], text[other] = text[other], text[i]


# function prototype
def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings. \
        option precise if a action is performed to the substrings before \
        it is yielded.
    """
    availableOptions = ['shuffle', 'unique', 'ordered', None]
    if type(text) != str or option not in availableOptions:
        print("ERROR")
        return
    newText = text.split(sep)
    if option == 'ordered':
        newText.sort()
    elif option == 'unique':
        # A Set is an unordered collection data type that is iterable,
        # mutable and has no duplicate elements.
        newText = set(newText)
    elif option == 'shuffle':
        shuffle(newText)
    for word in newText:
        yield word


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)
print()

for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print()

for word in generator(text, sep=" ", option="ordered"):
    print(word)
print()

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
print()

text = 1.0
for word in generator(text, sep="."):
    print(word)
