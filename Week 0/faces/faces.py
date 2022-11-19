def convert():
    x = str(input("Input: "))

    h = ':)' in x
    s = ':(' in x

    if (h == True):
        first = x.replace(":)", "🙂")
        if (s == True):
            second = first.replace(":(", "🙁")
            print(second)
        else:
            print(first)
    elif (s == True):
        third = x.replace(":(", "🙁")
        print(third)


convert()