from vector import Vector

# size ctor
print("TEST: Vector(4)")
print(Vector(4).shape)
print(Vector(4).values)
print()

print("TEST: Vector(-1)")
try:
    print(Vector(-1).values)
except ValueError as err:
    print(err)
print()

# range ctor
print("TEST: Vector((10, 16))")
print(Vector((10, 16)).shape)
print(Vector((10, 16)).values)
print()

print("TEST: Vector((16, 10))")
try:
    print(Vector((16, 10)).values)
except ValueError as err:
    print(err)
print()

print("TEST: Vector((16, 'echo'))")
try:
    print(Vector((16, "echo")).values)
except ValueError as err:
    print(err)
print()

print("TEST: Vector((16, 20, 40))")
try:
    print(Vector((16, 20, 40)).values)
except ValueError as err:
    print(err)
print()

print("TEST: Vector([['0.0'], [1.0], [2.0], [3.0]])")
try:
    v1 = Vector([['0.0'], [1.0], [2.0], [3.0]])
except ValueError as err:
    print(err)
print()

print("TEST:  Vector(['lol', [1.0], [2.0], [3.0]])")
try:
    v1 = Vector(["lol", [1.0], [2.0], [3.0]])
except ValueError as err:
    print(err)
print()

#default ctor is used below for each test
#sub
print("TEST: sub 2 col vector")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[5.0], [4.0], [3.0], [3.0]])
print(v2 - v1)
print()

print("TEST: sub 2 row vector")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[5.0, 4.0, 3.0, 3.0]])
print(v2 - v1)
print()

print("TEST: sub 2 different vector shape")
try:
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = Vector([[5.0], [4.0], [3.0], [3.0]])
    print(v2 - v1)
except ValueError as err:
    print(err)
print()

print("TEST: sub a vector to 45")
try:
    v1 = 45 - v1
    print(v1)
except ValueError as err:
    print(err)
print()

#add
print("TEST: add 2 col vector")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[5.0], [4.0], [3.0], [2.0]])
print(v1 + v2)
print()

print("TEST: add 2 row vector")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[5.0, 4.0, 3.0, 2.0]])
print(v1 + v2)
print()

print("TEST: add 2 different vector shapes")
try:
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = Vector([[5.0], [4.0], [3.0], [3.0]])
    print(v2 + v1)
except ValueError as err:
    print(err)
print()

print("TEST: add a vector to 45")
try:
    v1 = 45 + v1
    print(v1)
except ValueError as err:
    print(err)
print()

#mul
print("TEST: multiply a row vector")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1 * 5)
print(5 * v1)
print()

print("TEST: multiply a row vector")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1 * 5)
print(5 * v1)
print()

#div
print("TEST: div by 2 a col vector then by 0")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1 / 2.0)
v1 / 0.0
print()

print("TEST: div by 2 a row vector then by 0")
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2 / 2.0)
v2 / 0.0
print()

print("TEST: div 2 by a vector")
try:
    2.0 / v1
except NotImplementedError as err:
    print("NotImplementedError:", err)
print()

#dot
print("TEST: dot method with col vectors")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
print()

print("TEST: dot method with row vectors")
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
print()

print("TEST: dot method with differnent vector shapes")
try:
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0], [4.0]])
    print(v3.dot(v4))
except ValueError as err:
    print(err)
print()

print("TEST: dot method with something else than a vector")
try:
    v3 = Vector([[1.0, 3.0]])
    print(v3.dot(42))
except ValueError as err:
    print(err)
print()

#shape
print("TEST: T method with col vector")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape) #(4,1)
print(v1.T()) # [[0.0, 1.0, 2.0, 3.0]]
print(v1.T().shape) # (1,4)
print()

print("TEST: T method with row vector")
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape) # (1,4)
print(v2.T()) # [[0.0], [1.0], [2.0], [3.0]]
print(v2.T().shape) # (4,1)
print()