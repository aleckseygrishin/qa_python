import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name, genre', [
        ['Гордость и предубеждение и зомби', 'Фантастика'],
        ['Что делать, если ваш кот хочет вас убить', 'Детективы']
    ])
    def test_set_book_genre_other_one_genres_genre_added(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name=name, genre=genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_not_set_genre_empty_array(self):
        name = 'Евгений Онегин'
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize("genre", ['Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_empty_books_len_zero(self, genre):
        collector = BooksCollector()
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    def test_get_books_with_specific_genre_three_books_and_genre_added_len_two(self):
        collector = BooksCollector()
        collector.add_new_book("Буратино")
        collector.add_new_book("Гуливер")
        collector.add_new_book("Сияние")
        collector.set_book_genre("Буратино", "Мультфильмы")
        collector.set_book_genre("Гуливер", "Мультфильмы")
        collector.set_book_genre("Сияние", "Ужасы")
        assert len(collector.get_books_with_specific_genre("Мультфильмы")) == 2

    @pytest.mark.parametrize('name, genre', [
        ["Сияние", "Ужасы"],
        ["Что делать, если ваш кот хочет вас убить", "Детективы"]
    ])
    def test_get_books_for_children_books_high_age_rating_empty_array(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name=name, genre=genre)
        assert len(collector.get_books_for_children()) == 0

    @pytest.mark.parametrize('name, genre', [
        ["Буратино", "Мультфильмы"],
        ["Гуливер", "Фантастика"]
    ])
    def test_get_books_for_children_books_low_age_rating_filled_array(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name=name, genre=genre)
        assert len(collector.get_books_for_children()) == 1

    @pytest.mark.parametrize('name', ['1234', '  2 3 ', 'Книга', '!№Books@$'])
    def test_add_book_in_favorites_added_one_books_book_in_list(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['1234', '  2 3 ', 'Книга', '!№Books@$'])
    def test_add_book_in_favorites_added_book_not_in_books_genre_dont_added_book(self, name):
        collector = BooksCollector()
        collector.add_book_in_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['1234', '  2 3 ', 'Книга', '!№Books@$'])
    def test_delete_book_from_favorites_delete_one_books_book_not_in_list(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()
