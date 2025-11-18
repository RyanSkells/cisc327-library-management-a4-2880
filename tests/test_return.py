from services.library_service import return_book_by_patron

def test_return_valid_input(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5, 'record_id' : 4, 'is_overdue' : False}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books', return_value= [test_book, test_book])
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= True)
    update_record_stub = mocker.patch('services.library_service.update_borrow_record_return_date', return_value= True)

    success, message = return_book_by_patron("123456", 5)
    assert success == True

def test_return_no_books_checked_out(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5, 'record_id' : 4, 'is_overdue' : False}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books', return_value= None)
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= False)
    update_record_stub = mocker.patch('services.library_service.update_borrow_record_return_date', return_value= True)
    success, message = return_book_by_patron("123456", 3)
    assert success == False

def test_return_invalid_patron_id(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5, 'record_id' : 4, 'is_overdue' : False}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= test_book)
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books', return_value= [test_book, test_book])
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= True)
    update_record_stub = mocker.patch('services.library_service.update_borrow_record_return_date', return_value= True)
    test_patron_id = "1234567"
    success, message = return_book_by_patron(test_patron_id, 3)
    assert success == False

def test_return_invalid_book_id(mocker):
    test_book = {'title' : "Test Book", 'book_id' : 5, 'available_copies' : 5, 'record_id' : 4, 'is_overdue' : False}
    get_book_stub = mocker.patch('services.library_service.get_book_by_id', return_value= None)
    get_borrowed_stub = mocker.patch('services.library_service.get_patron_borrowed_books', return_value= None)
    availability_stub = mocker.patch('services.library_service.update_book_availability', return_value= False)
    update_record_stub = mocker.patch('services.library_service.update_borrow_record_return_date', return_value= True)

    test_book_id = 4
    success, message = return_book_by_patron("123456", test_book_id)
    assert success == False