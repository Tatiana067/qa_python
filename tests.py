from main import BooksCollector


import pytest


class TestBooksCollector:

    def test_init_books_genre_is_empty_dictionary(self):
        collector = BooksCollector()

        assert collector.books_genre == {}

    def test_init_favorites_is_empty_list(self):
        collector = BooksCollector()

        assert collector.favorites == []

    def test_init_genre_contains_available_genres(self):
        collector = BooksCollector()
        available_genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

        assert collector.genre == available_genres

    def test_init_genre_age_rating_contains_restricted_genres(self):
        collector = BooksCollector()
        restricted_genres = ['Ужасы', 'Детективы']

        assert collector.genre_age_rating == restricted_genres

    @pytest.mark.parametrize('name', ['','a','a*40','a*41'])
    def test_add_new_book_name_book_title_contains_from_1_to_40_characters(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        
        if 0 < len(name) < 41:
            assert name in collector.get_books_genre()
        else:
            assert name not in collector.get_books_genre()

    def test_add_new_book_can_be_added_only_once(self):
        collector = BooksCollector()
        name = 'Кто украл лопату у кота'
        collector.add_new_book(name)
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_determines_the_genre_of_the_book(self):
        collector = BooksCollector()
        name = 'Кто украл лопату у кота'

        collector.add_new_book(name)
        collector.set_book_genre(name, 'Детективы')

        assert collector.get_book_genre(name) == 'Детективы'

    def test_get_book_genre_determine_the_genre_based_on_the_books_title(self):
        collector = BooksCollector()
        name = 'Кто украл лопату у кота'
        book_genre = 'Детективы'

        collector.add_new_book(name)
        collector.set_book_genre(name, book_genre)

        assert collector.get_book_genre(name) == book_genre

    def test_get_books_with_specific_genre_successful_conclusion(self):
        collector = BooksCollector()
        name = 'Кот из Ада: Мурчание на улице Вязов'
        collector.add_new_book(name)

        collector.set_book_genre(name, 'Ужасы')
        result = collector.get_books_with_specific_genre('Ужасы')

        assert result == [name]

    def test_get_books_genre_successful_conclision(self):
        collector = BooksCollector()
        name = 'Как я завёл человека, и что из этого вышло'

        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        result = collector.get_books_genre()

        assert result == {name: 'Комедии'}

    def test_get_books_for_children_age_rating(self):
        collector = BooksCollector()

        collector.books_genre['Дневник кота, которого случайно отправили на Марс'] = 'Фантастика'
        result = collector.get_books_for_children()

        assert result == ['Дневник кота, которого случайно отправили на Марс']

    def test_add_book_in_favorites_successful_addition(self):
        collector = BooksCollector()
        collector.books_genre['Кто украл лопату у кота'] = 'Детективы'

        collector.add_book_in_favorites('Кто украл лопату у кота')

        assert collector.favorites == ['Кто украл лопату у кота']

    def test_delete_book_from_favorites_successful_deletion(self):
        collector = BooksCollector()
        collector.favorites = ['Кто украл лопату у кота', 'Дневник кота, которого случайно отправили на Марс']

        collector.delete_book_from_favorites('Кто украл лопату у кота')

        assert collector.favorites == ['Дневник кота, которого случайно отправили на Марс']

    def test_get_list_of_favorites_books_successful_list(self):
        collector = BooksCollector()

        collector.favorites = ['Дневник кота, которого случайно отправили на Марс']

        result = collector.get_list_of_favorites_books()
        assert result == ['Дневник кота, которого случайно отправили на Марс']
            