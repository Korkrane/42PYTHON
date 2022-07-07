from generator import generator

txt="This is a simple string for a basic test. Very simple."
for elem in generator(txt, sep=' '):
    print(elem)

for elem in generator(txt, sep='.'):
    print(elem)

for elem in generator(txt, sep='i'):
    print(elem)

for elem in generator(txt, sep='si'):
    print(elem)
