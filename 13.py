def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


n = int(input("Enter any number : "))

# if n >= 1 :
#     print(factorial(n))
# elif n == 0 :
#     print("Factorial of zero is one")
# else :
#     print("Factorial doesn't exist")

try:
    print(factorial(n))
except RecursionError:
    print("Number must be greater than 0")
