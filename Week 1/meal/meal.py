def convert(time):
    hours, minutes = time.split(":")

    if (int(hours) == 7):
        if(int(minutes) <= 59):
            print("breakfast time")

    elif (int(hours) == 8):
            print("breakfast time")

    elif (int(hours) == 12):
        if(int(minutes) <= 59):
            print("lunch time")

    elif (int(hours) == 13):
            print("lunch time")

    elif (int(hours) == 18):
        if(int(minutes) <= 59):
            print("dinner time")

    elif (int(hours) == 19):
            print("dinner time")

time = str(input("What time is it? "))
convert(time)




#breakfast time, lunch time, or dinner time