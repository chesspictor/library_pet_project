import class_book as cb
import functions as f
import json
import os

f_path = 'library.json'
if os.path.exists(f_path):
    with open(f_path, 'r') as file:
        data = json.load(file)
else:
    with open(f_path, 'w') as file:
        json.dump({}, file)
        data = []
    print('Файл library.json не существовал')
if not isinstance(data, list):
    if data is not None:
        if data:
            data = [data]
        else:
            data = []
    else:
        data = []
data_class = []
for i in data:
    book = cb.Book(i['id'], i['title'],
                   i['author'], i['year'],
                   i['status'])
    data_class.append(book)
start = True
if data_class:
    id_max = data_class[-1].id
else:
    id_max = 0
while start != 0:
    start = f.start_screen()
    if start == 1:
        id_max += 1
        book = f.terminal_new_book(id_max)
        data_class.append(book)
    if start == 2:
        s = 'id удаляемой книги: '
        search = f.check_blank(s, True)
        flag = False
        for book in data_class[:]:
            if book.id == search:
                data_class.remove(book)
                flag = True
        if flag == False:
            print(f'Книги с id{search} не существует')
    if start == 3:
        start_3 = True
        while start_3 != 0:
            s = '\n1 - Поиск по названию\n'
            s += '2 - Поиск по автору\n'
            s += '3 - Поиск по году\n'
            s += '0 - Выход\n'
            s += 'Введите число: '
            flag = False
            found = False
            while not flag:
                try:
                    start_3 = int(input(s))
                    if start_3 in range(0,4):
                        flag = True
                        if start_3 == 1:
                            message = 'Название: '
                            search = f.check_blank(message)
                            for book in data_class:
                                #if book.title == search:
                                if f.substring(search, book.title):
                                    print(book.to_terminal())
                                    found = True
                        if start_3 == 2:
                            message = 'Автор: '
                            search = f.check_blank(message)
                            for book in data_class:
                                #if book.author == search:
                                if f.substring(search, book.author):
                                    print(book.to_terminal())
                                    found = True
                        if start_3 == 3:
                            message = 'Год: '
                            search = f.check_blank(message,
                                                   True)
                            for book in data_class:
                                if book.year == search:
                                    print(book.to_terminal())
                                    found = True
                        if start_3 == 0:
                            found = True
                        if found == False:
                            print('Книг не найдено')
                    else:
                        print('От 0 до 3!')
                except ValueError:
                    print('Нечисловое значение!')
    if start == 4:
        for book in data_class:
            print(book.to_terminal_brief())
    if start == 5:
        s = 'id книги: '
        search = f.check_blank(s, True)
        flag = False
        for book in data_class:
            if book.id == search:
                book.switch_status()
                flag = True
        if flag == False:
            print(f'Книги с id{search} не существует')
with open(f_path, 'w') as file:
    json.dump([book.to_dict() for book in data_class],
              file, indent = 4)
