def multiplier(x, y):
    if y == 1:
        return x
    else:
        return x + multiplier(x, y - 1)


print(multiplier(8, 7))
