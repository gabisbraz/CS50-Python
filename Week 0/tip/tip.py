def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    rem1 = str(d)
    rem2 = float(rem1.removeprefix('$'))
    return rem2

def percent_to_float(p):
    rem3 = str(p)
    rem4 = float(rem3.removesuffix('%'))
    rem5 = rem4 / 100
    return rem5

main()