# stupid Calc v.1

what = input ( "Что делаем? (+,-): " )

a = float( input("Первое число: ") )
b = float( input("Второе число2: ") )

if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("чумба, ты совсем ёбнутый?ты не дописал калькулятор")
