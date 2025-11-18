from services.library_service import calculate_late_fee_for_book
from datetime import datetime, timedelta

# borrow_date, due_date
def test_late_fee_zero_days(mocker):
    now = datetime.now()
    borrow_date = now - timedelta(days=0)
    due_date = borrow_date + timedelta(days=14)
    test_borrowed_books = [
        {'book_id': 1, 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565", 'due_date': due_date},
        {'book_id': 2, 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123", 'due_date': due_date},
        {'book_id': 3, 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321", 'due_date': due_date}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value= test_borrowed_books)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] <= 0
    assert fee_details['fee_amount'] == 0

def test_late_fee_seven_days(mocker):
    now = datetime.now()
    borrow_date = now - timedelta(days=7)
    due_date = borrow_date + timedelta(days=14)
    test_borrowed_books = [
        {'book_id': 1, 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565",
         'due_date': due_date},
        {'book_id': 2, 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123", 'due_date': due_date},
        {'book_id': 3, 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321",
         'due_date': due_date}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value=test_borrowed_books)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] <= 0
    assert fee_details['fee_amount'] == 0
def test_late_fee_fourteen_days(mocker):
    now = datetime.now()
    borrow_date = now - timedelta(days=14)
    due_date = borrow_date + timedelta(days=14)
    test_borrowed_books = [
        {'book_id': 1, 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565", 'due_date': due_date},
        {'book_id': 2, 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123", 'due_date': due_date},
        {'book_id': 3, 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321", 'due_date': due_date}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value= test_borrowed_books)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 0
    assert fee_details['fee_amount'] == 0

def test_late_fee_twentyone_days(mocker):
    now = datetime.now()
    borrow_date = now - timedelta(days=21)
    due_date = borrow_date + timedelta(days=14)
    test_borrowed_books = [
        {'book_id': 1, 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565",
         'due_date': due_date},
        {'book_id': 2, 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123", 'due_date': due_date},
        {'book_id': 3, 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321",
         'due_date': due_date}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value=test_borrowed_books)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 7
    assert fee_details['fee_amount'] == 3.5

def test_late_fee_twentyeight_days(mocker):
    now = datetime.now()
    borrow_date = now - timedelta(days=28)
    due_date = borrow_date + timedelta(days=14)
    test_borrowed_books = [
        {'book_id': 1, 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565",
         'due_date': due_date},
        {'book_id': 2, 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123", 'due_date': due_date},
        {'book_id': 3, 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321",
         'due_date': due_date}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value=test_borrowed_books)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 14
    assert fee_details['fee_amount'] == 10.5

def test_late_fee_thirtyfive_days(mocker):
    now = datetime.now()
    borrow_date = now - timedelta(days=35)
    due_date = borrow_date + timedelta(days=14)
    test_borrowed_books = [
        {'book_id': 1, 'title': "Great Gatsby", 'author': "Scott Fitzgerald", 'isbn': "9780743273565",
         'due_date': due_date},
        {'book_id': 2, 'title': "1984", 'author': "George Orwell", 'isbn': "1234567890123", 'due_date': due_date},
        {'book_id': 3, 'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'isbn': "3210987654321",
         'due_date': due_date}
    ]
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books',
                                     return_value=test_borrowed_books)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 21
    assert fee_details['fee_amount'] == 15

