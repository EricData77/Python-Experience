
##### YIELD KEYWORD ####
# yield converts regular python functions to generators - Ex 1 , 2
# generator functions return generator objects that is iterable - Ex 3

### Ex 1 - GENERATOR FUNCTION
def simpleGeneratorFunction():
    """
    A generator function that yield 1 first, then 2 and 3
    :return: 1 , 2, 3
    """
    yield  1
    yield  2
    yield  3


print("Ex 1:")
print(type(simpleGeneratorFunction()))
for value in simpleGeneratorFunction():
    print(value)


### Ex 2 - GENERATOR OBJECTS
def simpleGeneratorFunction2():
    """
    A generator function that yield 1 first, then 2 and 3
    :return: 1 , 2, 3
    """
    yield  1
    yield  2
    yield  3


x = simpleGeneratorFunction2()  # x is a generator object
print(type(x))

print("Ex 2:")
print(x.__next__())  # Iterating over generator using __next__()
print(x.__next__())
print(x.__next__())


### Ex 3 - Fibonacci
def fib(limit):
    a, b = 0, 1
    while a < limit:
        # This generator function returns a list of "a" value
        yield a  # a will be the result of fib() function/generator
        a, b = b, a + b

x = fib(5)  # Create generator object

# Iterating through generator object
print("Ex 3:")
print("__next() method")
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print("looping method")
for i in fib(5):
    print(i)


# Ex 4
def printResult(string):
    for i in string:
        if i == "e":
            yield i

string = "GreekforGreeks"
ans = 0
print("The number of e in word is: ", end="")
string = string.strip()

for j in printResult(string):
    """
    printResult() generator is now the list "eeee"
    ans will return the length of "eeee" by using iterator j
    """
    # print(j)
    ans = ans + 1


print("Ex 4:")
print(ans)

#### RETURN KEYWORD ####
# Use fir the ending and call the result of statement

class Test():
    def __init__(self):
        self.string = "The Tran"
        self.x = "Eric Tran"

def fun():
    return Test()

# t variable is class Test data type
t = fun()
print("Return Ex")
print(t.string)
print(t.x)
