from math import ceil


class Pagination:
    def __init__(self, items, page_size):
        self.page_size = page_size  # Кол-во символов в строке
        self.items_list = [i for i in items]  # Лист со значениями из items
        self.pages_number = ceil((len(self.items_list) / page_size))  # Кол-во страниц
        self.pages = []  # Кортеж из страниц, содержащих значения, по количесву из page_size
        self.current_page_number = 0  # Текущий номер страницы
        x = 0  # Переменная счетчик
        for i in range(self.pages_number):  # Цикл для создания кортежа pages
            self.pages.append(self.items_list[x:x + self.page_size])
            x += page_size

    def get_vizible_items(self):  # Возвращает список элементов текущей страницы
        return self.pages[self.current_page_number]

    def prev_page(self):  # Переход на предыдущую страницу
        self.current_page_number -= 1
        if self.current_page_number < 0:
            self.current_page_number += 1
            return self

    def next_page(self):  # Переход на следующую страницу
        self.current_page_number += 1
        if self.current_page_number >= self.pages_number:
            self.current_page_number -= 1
            return self

    def first_page(self):  # Переход на первую страницу
        self.current_page_number = 0
        return self

    def last_page(self):  # Переход на последнюю страницу
        self.current_page_number = self.pages_number - 1
        return self

    def go_to_page(self, number):  # Принимает номер страницы, на которую необходимо совершить преход
        if number > self.pages_number:
            self.current_page_number = self.pages_number
            return self
        elif number < 1:
            self.current_page_number = 0
            return self
        else:
            self.current_page_number = number - 1
            return self

    def get_current_page(self):  # Возвращает номер текущей страницы
        return self.current_page_number

    def get_page_size(self):  # Возвращает размер текущей страницы
        return len(self.pages[self.current_page_number])

    def get_items(self):  # Возвращает список строк
        return self.pages


alphabet_list = list('abcdefghijklmnopqrstuvwxyz')

Test = Pagination(alphabet_list, 4)
print(Test.get_items())
print(Test.get_vizible_items())
Test.next_page()
print(Test.get_vizible_items())
Test.last_page()
print(Test.get_vizible_items())
Test1 = Test.next_page().next_page().last_page().go_to_page(3)
print(Test.get_vizible_items())
