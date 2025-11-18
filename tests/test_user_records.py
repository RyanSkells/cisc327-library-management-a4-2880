import services.library_service
from routes.borrowing_routes import return_book
from services.library_service import get_patron_status_report

def test_user_records_valid_input(mocker):
    test_borrowed_books = [
        {'book_id' : "1", 'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'book_id' : "2", 'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'book_id' : "3", 'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value= test_borrowed_books)
    get_borrow_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value=3)
    test_records = [
        {'id': "1", 'patron_id': "123456", 'book_id': "3"},
        {'id': "2", 'patron_id': "123456", 'book_id': "2"},
        {'id': "3", 'patron_id': "123456", 'book_id': "1"},
    ]

    get_records_stub = mocker.patch('services.library_service.get_patron_borrow_records', return_value= test_records)
    calc_late_fee_stub = mocker.patch('services.library_service.calculate_late_fee_for_book',
                                      return_value = {'fee_amount' : 0})

    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("123456")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == True

def test_user_records_patron_id_not_exist(mocker):
    test_borrowed_books = [
        {'book_id' : "1", 'title' : "Great Gatsby", 'author' : "Scott Fitzgerald", 'isbn' : "9780743273565"},
        {'book_id' : "2", 'title' : "1984", 'author' : "George Orwell", 'isbn' : "1234567890123"},
        {'book_id' : "3", 'title' : "To Kill a Mockingbird", 'author' : "Harper Lee", 'isbn' : "3210987654321"}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value= [])
    get_borrow_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value=0)
    test_records = [
        {'id': "1", 'patron_id': "123456", 'book_id': "3"},
        {'id': "2", 'patron_id': "123456", 'book_id': "2"},
        {'id': "3", 'patron_id': "123456", 'book_id': "1"},
    ]

    get_records_stub = mocker.patch('services.library_service.get_patron_borrow_records', return_value= [])
    calc_late_fee_stub = mocker.patch('services.library_service.calculate_late_fee_for_book',
                                      return_value = {'fee_amount' : 0})
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("654321")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == False

def test_user_records_patron_id_too_short(mocker):
    test_borrowed_books = [
        {'book_id': "1", 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565"},
        {'book_id': "2", 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123"},
        {'book_id': "3", 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321"}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value=[])
    get_borrow_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value=0)
    test_records = [
        {'id': "1", 'patron_id': "123456", 'book_id': "3"},
        {'id': "2", 'patron_id': "123456", 'book_id': "2"},
        {'id': "3", 'patron_id': "123456", 'book_id': "1"},
    ]

    get_records_stub = mocker.patch('services.library_service.get_patron_borrow_records', return_value=[])
    calc_late_fee_stub = mocker.patch('services.library_service.calculate_late_fee_for_book',
                                      return_value={'fee_amount': 0})
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("12345")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == False

def test_user_records_patron_id_too_long(mocker):
    test_borrowed_books = [
        {'book_id': "1", 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565"},
        {'book_id': "2", 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123"},
        {'book_id': "3", 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321"}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value=[])
    get_borrow_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value=0)
    test_records = [
        {'id': "1", 'patron_id': "123456", 'book_id': "3"},
        {'id': "2", 'patron_id': "123456", 'book_id': "2"},
        {'id': "3", 'patron_id': "123456", 'book_id': "1"},
    ]

    get_records_stub = mocker.patch('services.library_service.get_patron_borrow_records', return_value=[])
    calc_late_fee_stub = mocker.patch('services.library_service.calculate_late_fee_for_book',
                                      return_value={'fee_amount': 0})
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("1234567")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == False