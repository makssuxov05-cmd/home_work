class Book:
    material = 'бумага'
    text = True

    def __init__(self, name_book, author, page_count, isbn):
        self.name_book = name_book
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = False

    def print_info(self):
        info = f"Название: {self.name_book}, Автор: {self.author}, страниц: {self.page_count}, материал: {Book.material}"
        if self.reserved:
            info += ", зарезервирована"
        print(info)



class SchoolBook(Book):
    def __init__(self, name_book, author, page_count, isbn,subject, grade, ): #taska
        super().__init__( name_book, author, page_count, isbn)
        self.subject = subject
        self.grade = grade
        # self.taska = taska ## незнаю как лучше сделать типо в коде указывать True and False или в переменной кароче незнаю сделаю так же как и сделала (так проще кажется и имб правильно)

    def print_info(self):
        info =  f"Название: {self.name_book}, Автор: {self.author}, страниц: {self.page_count}, придмет: {self.subject}, класс: {self.grade}"
        if self.reserved:
            info += ", зарезервирована"
        print(info)



book1 = Book("Приключения Тома Сойера", "Марк Твен", 320, "978-5-04-116345-3")
book2 = Book("Наедине с собой. Размышления", "Марк Аврелий", 416, "978-5-17-103372-5")
book3 = Book("Самурай без меча", "Китами Масао", 256, "978-5-04-116346-0")
book4 = Book("Краткая история человечества", "Юваль Ной Харари", 520, "978-5-17-091712-5")
book5 = Book("Ревизор", "Николай Гоголь", 288, "978-5-04-116347-7")
school_book1 = SchoolBook("Алгебра", "Иванов", 200, "978-5-09-000001-1", "Математика", 9)
school_book2 = SchoolBook("История России", "Петров", 350, "978-5-09-000002-2", "История", 10)


book3.reserved = True
book1.reserved = True
school_book2.reserved = True




all_books = [book1, book2, book3, book4,book5, school_book2, school_book1]

for books in all_books:
    books.print_info()


