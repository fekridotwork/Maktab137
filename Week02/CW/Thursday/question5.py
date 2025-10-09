def convert_time(sec):
    hour = sec // 3600
    sec = sec % 3600
    minute = sec // 60
    remain_sec = sec % 60
    return f"{hour}:{minute}:{remain_sec}"

sec = int(input("Please enter the time in second : "))
print(convert_time(sec))