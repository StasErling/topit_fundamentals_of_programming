a = 1000
b = a
c = int("1000")

print("Типы:", type(a), type(b), type(c)) #а - int, b- int, c - int
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b) # true
print("a is b:", a is b) # true
print("a == c:", a == c) # true
print("a is c:", a is c) # false

c = None
print(c is None) #true

first = "python"
second = "py" + "thon"

print(first == second) #true
print(first is second) #true 