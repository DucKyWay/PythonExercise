time = int(input("Enter time: "))
balance = time

while balance > 0:
    if balance >= 84000: #day
        day = balance//84000
        day_left = balance/day
    elif balance >= 3600: #hour
        hour = balance // 3600
        hour_left = balance / hour
    elif balance >= 60: #min
        minute = balance // 60
        min_left = balance / minute

print(day_left, hour_left, min_left, sec_left)