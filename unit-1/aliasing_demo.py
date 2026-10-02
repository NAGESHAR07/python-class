a = [1, 2, 3]
# This step can be called as aliasing (giving another name to a)
b = a
# This step just copied the items of a to c
c = a[:]

b.append(4)
c.append(99)
# changing one list also changed the other list because
# b and a refer to the same object in memory

print("a =", a)
print("b =", b)
print("c =", c)
print("b is a:", b is a, "| c is a:", c is a)
