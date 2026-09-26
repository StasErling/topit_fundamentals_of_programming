"""Программа по входным данным выводит информационную карточку вычислительного эксперимента"""

name = input("Введите имя исследователя: ")
experimentName = input("Введите название эксперимента: ")
amountOfRuns = int(input("Введите количество выполненных запусков: "))
lengthOfOneRun = float(input("Введите длительность одного запуска (в секундах): "))
real = float(input("Введите действительную часть комплексного коэффициента: "))
imag = float(input("Введите мнимую часть комплексного коэффициента: "))

totalTime_sec = lengthOfOneRun * amountOfRuns
totalTime_min = totalTime_sec / 60
complexNumber = complex(real, imag)
square = real**2 + imag**2
has_runs = bool(amountOfRuns)

print("========================================")
print("ЭКСПЕРИМЕНТ: ", experimentName)
print("Исследователь: ", name)
print("Запуски: ", amountOfRuns)
print(f"Общее время: {totalTime_sec:.2f} с ({totalTime_min:.2f} мин)")
print("Коэффициент: ", complexNumber)
print(f"Квадрат модуля: {square:.2f}")
print("Есть выполненные запуски: ", has_runs)
print("========================================")

print("-----------------ТИПЫ-------------------")
print("тип имени исследователя: ", type(name), "тип названия эксперимента: ",
       type(experimentName), "тип количества запусков: ", type(amountOfRuns), 
       "тип длительности одного запуска: ", type(lengthOfOneRun), "тип действительной части коэффициента: ", 
       type(real), "тип мнимой части коэффициента: ", type(imag))
