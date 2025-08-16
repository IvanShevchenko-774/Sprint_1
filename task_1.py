time_string = "1h 45m,360s,25m,30m 120s,2h 60s"

total_minutes = 0

for value in time_string.split(","):
    for number in value.split():
        if "h" in number:  
            total_minutes += int(number.replace("h", "")) * 60
        elif "m" in number:  # минуты
            total_minutes += int(number.replace("m", ""))
        elif "s" in number:  # секунды
            total_minutes += int(number.replace("s", "")) // 60

print(f'Всего {total_minutes} минут')
