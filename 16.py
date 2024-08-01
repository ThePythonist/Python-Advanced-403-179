def myhash(number):
    if len(str(number)) == 1:
        return number
    else:
        digits = [int(i) for i in str(number)]
        return myhash(sum(digits))


print(myhash(435345))
