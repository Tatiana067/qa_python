from main import BooksCollector


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

        assert collector.get_genres == available_genres

    def test_init_genre_age_rating_contains_restricted_genres(self):
        collector = BooksCollector()
        restricted_genres = ['Ужасы', 'Детективы']

        assert collector.get_genre_age_rating == restricted_genres

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
        collector.name = 'Кто украл лопату у кота'
        collector.add_new_book('Кто украл лопату у кота')

        assert len(collector.get_books_rating()) == 1

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


        
    