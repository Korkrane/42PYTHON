import sys

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

res = []

for params_i, params in enumerate(sys.argv[1::]):
    string = params.split()
    for word_i, word in enumerate(string):
        if word.isalnum():
            for letter in word:
                res.append(MORSE_CODE_DICT[letter.upper()] + " ")
        else:
            print("ERROR")
            exit()
        if params_i != len(sys.argv) - 2 or word_i != len(string) - 1:
            res.append("/ ")

for i in res:
    print(i, end="")
if len(sys.argv) > 1:
    print()
