#ex1
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
#ex3
num1 = int(input("Введите 1 число:"))
num2 = int(input("Введите 2 число "))
print("1. + ")
print("3. - ")
print('3. * ')
print('4. / ')
choice=int(input(":Выберите опперацию "))
if choice == 1:
    result = (num1 + num2)
    print(result)
elif choice == 2:
    result = (num1 - num2)
    print(result)
elif choice == 3:
    result = (num1 * num2)
    print(result)
elif choice == 4:
    result = ( num1 / num2)
else:
    print(':Некоректный ввод'
