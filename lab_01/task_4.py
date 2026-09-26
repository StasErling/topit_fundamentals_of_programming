student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print("1 и -1 символы имени:", student[0], student[-1])
print("срез с именем:", student[:4])
print("срез с фамилией:", student[5:])
print("нижний регистр:", student.lower())
print("верхний регистр:", student.upper())
print("инициалы:", student[0] + "." + student[5] + ".")
print("обратный курс:", course[::-1])
print("способ1: ", "%s - %s: %d/%d (%.1f%%)" % (student, course, completed, total, completed*100/total))
print("способ2: ", "{} - {}: {}/{} ({}%)".format(student, course, completed, total, completed*100/total))
print("способ3: ", f"{student} - {course}: {completed}/{total} ({completed*100/total}%)")

symbol = "Я"
print("символ: ",symbol)
print("позиция: ",ord(symbol))
print("восстановленный символ: ",chr(ord(symbol)))
print("utf-8 символа: ",symbol.encode("utf-8"))
print("длина utf-8 символа: ",len(symbol.encode("utf-8")))

#student[0] = "С"