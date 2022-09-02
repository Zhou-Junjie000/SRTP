hour = 0
minute = 0
counter = 0
while hour != 24:
    counter += 1
    print('"%02d:%02d":%d,' % (hour, minute, counter))
    minute += 5
    if minute == 60:
        hour += 1
        minute = 0
