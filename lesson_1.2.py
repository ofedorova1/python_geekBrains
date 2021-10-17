# 1.2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Введите количество секунд:"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds - int(hours * 3600) - int(minutes * 60)
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if sec < 10:
    sec = "0" + str(sec)
print("{0}:{1}:{2}".format(hours, minutes, sec))