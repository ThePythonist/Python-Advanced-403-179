def is_prime(n):
    divs = [i for i in range(1, n + 1) if n % i == 0]
    return True if len(divs) == 2 else False


def average(*args):
    print(sum(args) / len(args))
