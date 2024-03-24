# qa_python
# Тесты
test_add_new_book_add_two_books - добавление 2х книг
test_set_book_genre_other_one_genres_genre_added - Жанр книги добавлен
test_get_book_genre_not_set_genre_empty_array - Книга без жанра
test_get_books_with_specific_genre_empty_books_len_zero - Пустой ответ при отсутствии жанра у книг
test_get_books_with_specific_genre_three_books_and_genre_added_len_two - Колличество записей в books_with_specific_genre (книг с указанным жанром = 2)
test_get_books_for_children_books_high_age_rating_empty_array - проверка отсутствия книг для детей, все жанры с высоким возрастным ограничением
test_get_books_for_children_books_low_age_rating_filled_array - проверка наличия книг для детей, низкие возрастные ограничения
test_add_book_in_favorites_added_one_books_book_in_list - проверка добавления книг в favorites
test_add_book_in_favorites_added_book_not_in_books_genre_dont_added_book - проверка, что книга не добавлена в favorites, из-за отсутствия её в books_genre
test_delete_book_from_favorites_delete_one_books_book_not_in_list - проверка удаления книги