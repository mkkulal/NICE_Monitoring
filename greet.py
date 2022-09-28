def greeting(name):
    print("Hi " + name + "!")

greeting("Mithun")

def square(x):
    return x * x

result = square(5)
print(result)

def sumOfSquares(x, y):
    square1 = x * x
    square2 = y * y
    return square1 + square2

result = sumOfSquares(2, 5)
print(result)

def is_it_raining():
    raining = input("Is it raining? ")
    return raining

mnday_status = is_it_raining()
print(mnday_status)
