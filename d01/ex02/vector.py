class Vector:
    def __init__(self, arg):
        if isinstance(arg, list):  # list ctor
            self.values = arg
            if isinstance(arg[0], list) and len(arg) > 1:  # column
                self.shape = (len(arg), 1)
                for iList in arg:
                    for i in iList:
                        if not isinstance(i, float):
                            raise ValueError("Must be floats only")
            else:  # row
                self.shape = (1, len(arg[0]))
                for i in arg[0]:
                    if not isinstance(i, float):
                        raise ValueError("Must be floats only")

        if isinstance(arg, int):  # size ctor
            if arg <= 0:
                raise ValueError("size init must be greater than 0")
            self.shape = ((len(range(arg))), 1)
            self.values = []
            for i in range(arg):
                self.values.append([float(i)])

        if isinstance(arg, tuple):  # range ctor
            if len(arg) > 2:
                raise ValueError("Range constructor len > 2")
            if not isinstance(arg[0], int) or not isinstance(arg[1], int):
                raise ValueError("range with not int value")
            if arg[1] < arg[0]:
                raise ValueError("impossible range")
            self.shape = (arg[1] - arg[0], 1)
            self.values = []
            for i in range(arg[0], arg[1]):
                self.values.append([float(i)])

    def dot(self, other):
        if not isinstance(other, Vector):
            raise ValueError("dot operations with vector and something else impossible")
        if self.shape != other.shape:
            raise ValueError("dot operations with different vector shapes")
        ret = 0
        if(self.shape[0] == 1):
            print("row ", end="")
            for i in range(self.shape[1]):
                 if type(self.values[0][i]) == float:
                    ret += self.values[0][i] * other.values[0][i]
        else:
            print("col ", end="")
            for i in range(self.shape[1]):
                if type(self.values[i]) == float:
                    ret += self.values[i] * other.values[i]
                else:
                    for j in range(self.shape[0]):
                        ret += self.values[j][i] * other.values[j][i]
        return ret

    def T(self):  # swap vector's shape
        new = []
        if self.shape[0] == 1:
            print("row ", end="")
            #print("a", self.values[0], len(self.values[0]))

            for i in range(self.shape[1]):
                #print(self.values[0][i])
                new.append([self.values[0][i]])
            return Vector(new)
        else:
            print("col ", end="")
            for i in range(self.shape[0]):
                # print(self.values[i][0])
                new.append(self.values[i][0])

            tlist = []
            tlist.append(new)
            # print(tlist)
            return Vector(tlist)
        return

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Can't add Vector with another type than Vector")
        if self.shape != other.shape:
            raise ValueError("Vectors doesn't have identical shapes")
        new = []
        if self.shape[0] == 1:
            print("row ", end="")
            for i in range(self.shape[1]):
                new.append(self.values[0][i] + other.values[0][i])
            tlist = []
            tlist.append(new)
            return Vector(tlist)

        else:
            print("col ", end="")
            for i in range(self.shape[0]):
                new.append([self.values[i][0] + other.values[i][0]])
        return Vector(new)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Can't sub Vector with another type than Vector")
        if self.shape != other.shape:
            raise ValueError("Vectors doesn't have identical shapes")
        new = []
        if self.shape[0] == 1:
            print("row ", end="")
            for i in range(self.shape[1]):
                new.append(self.values[0][i] - other.values[0][i])
            tlist = []
            tlist.append(new)
            return Vector(tlist)

        else:
            print("col ", end="")
            for i in range(self.shape[0]):
                new.append([self.values[i][0] - other.values[i][0]])
        return Vector(new)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        new = []
        if self.shape[0] == 1:
            print("row ", end="")
            for i in range(self.shape[1]):
                new.append(self.values[0][i] * other)
            tlist = []
            tlist.append(new)
            return Vector(tlist)

        else:
            print("col ", end="")
            for i in range(self.shape[0]):
                new.append([self.values[i][0] * other])
        return Vector(new)

    def __rmul__(self, other):
        print("rmul")
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            new = []
            if self.shape[0] == 1:
                print("row ", end="")
                for i in range(self.shape[1]):
                    new.append(self.values[0][i] / other)
                tlist = []
                tlist.append(new)
                return Vector(tlist)
            else:
                print("col ", end="")
                for i in range(self.shape[0]):
                    new.append([self.values[i][0] / other])
            return Vector(new)
        except ZeroDivisionError:
            print("ZeroDivisionError: division by zero.")

    def __rtruediv__(self, other):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)
