import services.library_service
from routes.borrowing_routes import return_book
from services.library_service import search_books_in_catalog

def test_search_by_title_valid_input(mocker):
    test_catalog = [
        {'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    books_stub = mocker.patch('services.library_service.get_all_books', return_value= test_catalog)
    success = search_books_in_catalog("great", "title")

    if success:
        assert True
    else:
        assert False

def test_search_by_author_valid_input(mocker):
    test_catalog = [
        {'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    books_stub = mocker.patch('services.library_service.get_all_books', return_value= test_catalog)
    success = search_books_in_catalog("fitz", "author")

    if success:
        assert True
    else:
        assert False
def test_search_by_isbn_valid_input(mocker):
    test_catalog = [
        {'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    books_stub = mocker.patch('services.library_service.get_all_books', return_value= test_catalog)
    success = search_books_in_catalog("9780743273565", "isbn")

    if success:
        assert True
    else:
        assert False
def test_search_invalid_title(mocker):
    test_catalog = [
        {'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    books_stub = mocker.patch('services.library_service.get_all_books', return_value= test_catalog)
    success = search_books_in_catalog("100984", "title")

    if not success:
        assert True
    else:
        assert False

def test_search_invalid_author(mocker):
    test_catalog = [
        {'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    books_stub = mocker.patch('services.library_service.get_all_books', return_value= test_catalog)
    success = search_books_in_catalog("George Orwellington", "author")

    if not success:
        assert True
    else:
        assert False
def test_search_invalid_isbn(mocker):
    test_catalog = [
        {'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    books_stub = mocker.patch('services.library_service.get_all_books', return_value= test_catalog)
    success = search_books_in_catalog("50", "isbn")

    if not success:
        assert True
    else:
        assert False
