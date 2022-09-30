from audioop import reverse


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -  1)
a = factorial(3)
print(a)

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last
print(sum_digits(12))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n -1)+fib(n-2)

a = "mithun"
b =  reverse(a)
print(b)