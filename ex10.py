t = int(input("Введите количество секунд с момента старта:"))
print(f"Время с момента старта: {t} секунд.")

hours = t // 3600
minutes = t%3600 // 60
seconds = t%3600 % 60

print(f"Форматированное время: {hours} ч {minutes} мин {seconds} сек.")