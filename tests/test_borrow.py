import pytest
from services.library_service import borrow_book_by_patron

# Test Patron ID input
def test_catalog_patron_id_valid_input(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value= 3)
    record_stub = mocker.patch('services.library_service.insert_borrow_record', return_value= True)
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= True)

    success, message = borrow_book_by_patron("123456", 5)

    assert success == True
    assert "successfully borrowed" in message.lower()

def test_catalog_patron_id_too_short(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value= 3)
    record_stub = mocker.patch('services.library_service.insert_borrow_record', return_value= True)
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= True)

    test_patron_id = "12345"
    success, message = borrow_book_by_patron(test_patron_id, 5)
    assert success == False
    assert "invalid patron id" in message.lower()

def test_catalog_patron_id_too_long(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value= 3)
    record_stub = mocker.patch('services.library_service.insert_borrow_record', return_value= True)
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= True)

    test_patron_id = "1234567"
    success, message = borrow_book_by_patron(test_patron_id, 5)
    assert success == False
    assert "invalid patron id" in message.lower()
# Test Borrow Limit
def test_catalog_borrow_limit(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_count_stub = mocker.patch('services.library_service.get_patron_borrow_count', return_value= 5)
    record_stub = mocker.patch('services.library_service.insert_borrow_record', return_value= True)
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= True)

    success, message = borrow_book_by_patron("123456", 5)
    assert success == False
    assert "borrowing limit" in message.lower()

