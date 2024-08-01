def adder(x, y):
    if y == 1:  # shart payan
        return x + 1
    else:  # shart edame
        return 1 + adder(x, y - 1)


print(adder(2, 4))
