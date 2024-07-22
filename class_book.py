from datetime import date 

class Book:
    def __init__(self, id, title = None,
                 author = None, year = None,
                 status = 'в наличии'):
        self.id = id
        self.title = (
            title if title is not None
            else 'N/A'
        )
        self.author = (
            author if author is not None
            else 'N/A'
        )
        self.year = (
            year if year is not None
            else date.today().year
        )
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    def to_terminal(self):
        return (
            f'id: {self.id}\n'
            f'title: {self.title}\n'
            f'author: {self.author}\n'
            f'year: {self.year}\n'
            f'status: {self.status}'
        )

    def to_terminal_brief(self):
        return (
            f'{self.id}\t'
            f'{self.title}\t'
            f'{self.author}\t'
            f'{self.year}\t'
            f'{self.status}'
        )

    def __del__(self):
        print(f'Книга id{self.id} удалена')

    def switch_status(self):
        if self.status == 'в наличии':
            self.status = 'выдана'
        else:
            self.status = 'в наличии'
        print(f'Статус книги с id{self.id} изменен')
