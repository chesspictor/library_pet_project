import class_book as cb

#ввод и проверка на корректность
def check_blank(message, numeric = False): 
    if numeric == False:
        try: 
            rez = input(message)
            rez = rez.strip()
            if not bool(rez):
                raise ValueError('пустая строка')         
        except ValueError as e:
            print(f'Предупреждение: {e}')
            rez = 'N/A'
    else:
        try:
            rez = int(input(message))
        except ValueError:
            print('Предупреждение: '
                  'пустое или НЕ числовое значение')
            rez = None
    return rez

#создание объекта новой книги
def terminal_new_book(id):
    title = check_blank('Название книги: ')
    author = check_blank('Автор: ')
    year = check_blank('Год издания: ', True)
    new_book = cb.Book(id, title, author, year)
    return new_book

#стартовая панель управления пользователя
def start_screen():
    s = '\n1 - Добавление книги\n'
    s += '2 - Удаление книги\n'
    s += '3 - Поиск книги\n'
    s += '4 - Отображение всех книг\n'
    s += '5 - Изменение статуса книги\n'
    s += '0 - Выход\n'
    s += 'Введите число: '
    flag = False
    while not flag:
        try:
            x = int(input(s))
            if x in range(0,6):
                flag = True
            else:
                print('От 0 до 5!')
        except ValueError:
            print('Нечисловое значение!')
    return x

#является ли строка подстрокой
def substring(s_min, s_max):
    s_min = s_min.lower()
    s_max = s_max.lower()
    if s_min in s_max:
        return True
    else:
        return False
