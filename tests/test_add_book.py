import pytest

import services.library_service
from services.library_service import add_book_to_catalog

# Positive test case
def test_add_book_valid_input(mocker):
    #stub the database insert operation
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(True, "Successfully added"))

    success, message = add_book_to_catalog("Test Valid Book", "Test Author", "1234567890123", 1)

    assert success == True
    assert "successfully added" in message.lower()

# Test Title input
def test_add_book_title_too_long(mocker):
    # stub the database insert operation
    add_stub = mocker.patch('services.library_service.insert_book',
                            return_value=(False, "Title must be less than 200 characters"))
    test_title = "1234567890" * 21 # 210 characters long
    success, message = add_book_to_catalog(test_title, "Test Author", "1234567890123", 1)

    assert success == False
    assert "200 characters" in message.lower()

def test_add_book_title_too_short(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "Title is required"))
    test_title = "" # 0 characters long
    success, message = add_book_to_catalog(test_title, "Test Author", "1234567890123", 1)

    assert success == False
    assert "title is required" in message.lower()

# Test Author input
def test_add_book_author_too_long(mocker):
    add_stub = mocker.patch('services.library_service.insert_book',
                            return_value=(False, "Author must be less than 100 characters"))
    test_author = "1234567890" * 11 # 110 characters long
    success, message = add_book_to_catalog("Test Title", test_author, "1234567890123", 1)

    assert success == False
    assert "100 characters" in message.lower()
def test_add_book_author_too_short(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "Author is required"))
    test_author = ""  # 0 characters long
    success, message = add_book_to_catalog("Test Title", test_author, "1234567890123", 1)

    assert success == False
    assert "author is required" in message.lower()

# Test ISBN input
def test_add_book_isbn_too_short(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "ISBN must be exactly 13 digits"))
    test_isbn = "1234567890" # 10 characters long
    success, message = add_book_to_catalog("Test Title", "Test Author", test_isbn, 1)

    assert success == False
    assert "13 digits" in message.lower()
def test_add_book_isbn_too_long(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "ISBN must be exactly 13 digits"))
    test_isbn = "12345678901234" # 14 characters long
    success, message = add_book_to_catalog("Test Title", "Test Author", test_isbn, 1)

    assert success == False
    assert "13 digits" in message.lower()

def test_add_book_isbn_not_a_number(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "ISBN must be a number"))
    test_isbn = "abcdefghijklm" # 13 characters long, with alphanumeric characters
    success, message = add_book_to_catalog("Test Title", "Test Author", test_isbn, 1)

    assert success == False
    assert "must be a number" in message.lower()

# Test Total copies input
def test_add_book_total_copies_negative_number(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "Total copies must be a positive integer"))
    test_copies = -5
    success, message = add_book_to_catalog("Test Title", "Test Author", "1234567890123", test_copies)

    assert success == False
    assert "must be a positive integer" in message.lower()

def test_add_book_total_copies_not_a_number(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "Total copies must be a positive integer"))
    test_copies = "a"
    success, message = add_book_to_catalog("Test Title", "Test Author", "1234567890123", test_copies)

    assert success == False
    assert "must be a positive integer" in message.lower()

def test_add_book_total_copies_not_present(mocker):
    add_stub = mocker.patch('services.library_service.insert_book', return_value=(False, "Total copies must be a positive integer"))
    test_copies = ""
    success, message = add_book_to_catalog("Test Title", "Test Author", "1234567890123", test_copies)

    assert success == False
    assert "must be a positive integer" in message.lower()