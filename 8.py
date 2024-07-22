import jdatetime


def show_jalali_age(birth):
    thisyear = jdatetime.datetime.now().year
    age = thisyear - birth
    print(age)


show_jalali_age(int(input("Enter your birth year : ")))
