user_select = int(input('Enter a number: '))
if user_select == 1:
    print (":Понеделтник")
elif user_select == 2:
    print(':Вторник')
elif user_select == 3:
    print(':Среда')
elif user_select == 4:
    print(':Четверг')
elif user_select == 5:
    print(':Пятница')
elif user_select == 6:
    print(':Суббота')
elif user_select == 7:
    print(':Воскресенье')
else :
    print(':Некоректное значение ')
#ex2
n1 = int(input("Введите 1 число: "))
n2= int(input("Введите 2 число :"))
if n1==n2:
    print("Числа равны")
elif n2<n1:
    print(f'{n1},{n2}')
elif n1<n2:
    print(f'{n2},{n1}')
else :
    print(':Ошибка')

