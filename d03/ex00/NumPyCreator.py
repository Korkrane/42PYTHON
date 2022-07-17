import numpy

# https://numpy.org/doc/stable/user/basics.creation.html


class NumPyCreator:
    def from_list(self, lst):
        if isinstance(lst, list):
            # check if each list as same len
            if isinstance(lst[0], list):
                tlen = len(lst[0])
                for t in lst:
                    if len(t) != tlen:
                        return None
                return numpy.array(lst)
        else:
            return None

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple):
            # check if each tuple as same len
            if isinstance(tpl[0], tuple):
                tlen = len(tpl[0])
                for t in tpl:
                    if len(t) != tlen:
                        return None
                return numpy.array(tpl)
            return numpy.array(tpl)
        else:
            return None

    # https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
    def from_iterable(self, itr):
        if hasattr(itr, '__iter__'):
            return numpy.fromiter(itr, int)
        else:
            return None

    # https://numpy.org/doc/stable/reference/routines.array-creation.html
    def from_shape(self, shape, value=0):
        if isinstance(shape, tuple):
            for i in shape:
                if i < 0:
                    return None
            return numpy.zeros(shape)
        else:
            return None

    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    def random(self, shape):
        if isinstance(shape, tuple):
            return numpy.random.rand(shape[0], shape[1])
        else:
            return None

    # https://numpy.org/doc/stable/reference/generated/numpy.identity.html
    def identity(self, n):
        if isinstance(n, int) and n >= 0:
            return numpy.identity(n)
        else:
            return None

if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[],[]]))
    print(npc.from_list([[1,2,3],[6,3,4],[8,5,6]]))
    print(npc.from_tuple(("a","b","c")))
    print(npc.from_iterable(range(5)))
    print(npc.from_shape((0, 0)))
    print(npc.from_shape((3, 5)))
    print(npc.random((3, 5)))
    print(npc.identity(4))
    print(npc.from_list("toto"))
    print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
    print(npc.from_tuple(3.2))
    print(npc.from_tuple(((1,5,8),(7,5))))
    print(npc.from_shape((-1, -1)))
    print(npc.identity(-1))