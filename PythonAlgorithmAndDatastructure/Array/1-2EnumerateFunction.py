# Enumerate function converts the tuple into enumerate objects

# Ex 1
x = ("apple", "banana", "mango")
y = enumerate(x)

print("Ex1: ", list(y))
# Return: [(0, 'apple'), (1, 'banana'), (2, 'mango')]

# Ex 2
l1 = ["eat", "sleep", "run"]
s1 = "erictran"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Ex 2:")
print(list(obj1))
for e in enumerate(l1):
    print(e)
## Change the start index from 0 to 2
print(list(enumerate(s1, 2)))

# Ex 3

