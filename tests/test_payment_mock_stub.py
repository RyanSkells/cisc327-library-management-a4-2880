import services.library_service
from services.library_service import pay_late_fees, refund_late_fee_payment
from services.payment_service import PaymentGateway
from unittest.mock import Mock

#-------------------------------------TESTS FOR pay_late_fees()---------------------------------------------------------
def test_pay_late_fees_valid_payment(mocker):
    #stub the fee calculation
    return_dict = {'fee_amount': 3.5, 'days_overdue': 7, 'status': True}
    fee_mock = mocker.patch('services.library_service.calculate_late_fee_for_book', return_value= return_dict)

    #stub the book fetch
    return_book = {'book_id' : 1, 'title' : "abcde", 'author' : "Geoff"}
    book_mock = mocker.patch('services.library_service.get_book_by_id', return_value= return_book)

    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (True, "txn_123", "Success")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    #use book_id 1, patron_id 123456, and mocked gateway
    success, msg, txn_id = pay_late_fees(patron_id="123456", book_id=1, payment_gateway=mock_gateway)

    #check that the stubs & mocks were called
    fee_mock.assert_called_once()
    book_mock.assert_called_once()
    mock_gateway.process_payment.assert_called_once_with(patron_id='123456', amount=3.5,
                                                         description="Late fees for 'abcde'")

    #check results
    assert success == True
    assert "success" in msg.lower()
    assert txn_id == 'txn_123'

def test_pay_late_fees_declined_payment(mocker):
    #stub the fee calculation
    return_dict = {'fee_amount': 1001, 'days_overdue': 7, 'status': True}
    fee_mock = mocker.patch('services.library_service.calculate_late_fee_for_book', return_value= return_dict)

    #stub the book fetch
    return_book = {'book_id' : 1, 'title' : "abcde", 'author' : "Geoff"}
    book_mock = mocker.patch('services.library_service.get_book_by_id', return_value= return_book)

    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (False, "txn_123", "Declined")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    #use book_id 1, patron_id 123456, and mocked gateway
    success, msg, txn_id = pay_late_fees(patron_id="123456", book_id=1, payment_gateway=mock_gateway)

    #check that the stubs & mocks were called
    fee_mock.assert_called()
    book_mock.assert_called()
    mock_gateway.process_payment.assert_called_once_with(patron_id='123456', amount=1001,
                                                         description="Late fees for 'abcde'")

    #check results
    assert success == False
    assert "declined" in msg.lower()
    assert txn_id == None

def test_pay_late_fees_invalid_patron_id(mocker):
    #stub the fee calculation
    return_dict = {'fee_amount': 3.5, 'days_overdue': 7, 'status': True}
    fee_mock = mocker.patch('services.library_service.calculate_late_fee_for_book', return_value= return_dict)

    #stub the book fetch
    return_book = {'book_id' : 1, 'title' : "abcde", 'author' : "Geoff"}
    book_mock = mocker.patch('services.library_service.get_book_by_id', return_value= return_book)

    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (False, "txn_123", "Declined")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    #use book_id 1, patron_id 1234567 (Invalid), and mocked gateway
    success, msg, txn_id = pay_late_fees(patron_id="1234567", book_id=1, payment_gateway=mock_gateway)

    #check that the stubs & mocks were NOT called
    fee_mock.assert_not_called()
    book_mock.assert_not_called()
    mock_gateway.process_payment.assert_not_called()

def test_pay_late_fees_no_fees(mocker):
    #stub the fee calculation
    return_dict = {'fee_amount': 0, 'days_overdue': 0, 'status': True}
    fee_mock = mocker.patch('services.library_service.calculate_late_fee_for_book', return_value= return_dict)

    #stub the book fetch
    return_book = {'book_id' : 1, 'title' : "abcde", 'author' : "Geoff"}
    book_mock = mocker.patch('services.library_service.get_book_by_id', return_value= return_book)

    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (False, "txn_123", "Invalid amount")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    #use book_id 1, patron_id 1234567 (Invalid), and mocked gateway
    success, msg, txn_id = pay_late_fees(patron_id="123456", book_id=1, payment_gateway=mock_gateway)

    #check that only the fee_calculation stub was called
    fee_mock.assert_called_once()
    book_mock.assert_not_called()
    mock_gateway.process_payment.assert_not_called()

def test_pay_late_fees_network_error(mocker):
    #stub the fee calculation
    return_dict = {'fee_amount': 3.5, 'days_overdue': 7, 'status': True}
    fee_mock = mocker.patch('services.library_service.calculate_late_fee_for_book', return_value= return_dict)

    #stub the book fetch
    return_book = {'book_id' : 1, 'title' : "abcde", 'author' : "Geoff"}
    book_mock = mocker.patch('services.library_service.get_book_by_id', return_value= return_book)

    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (False, "txn_123", "Payment processing error")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    success, msg, txn_id = pay_late_fees(patron_id="123456", book_id=1, payment_gateway=mock_gateway)

    #check that only the fee_calculation stub was called
    fee_mock.assert_called()
    book_mock.assert_called()
    mock_gateway.process_payment.assert_called_once_with(patron_id='123456', amount=3.5, description="Late fees for 'abcde'")

    assert "processing error" in msg.lower()

#---------------------------------------END OF TESTS FOR pay_late_fees()------------------------------------------------

#--------------------------------------TESTS FOR refund_late_fee_payment()----------------------------------------------
def test_refund_late_fee_payment_valid_refund(mocker):
    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.refund_payment.return_value = (True, "Refund processed successfully")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    success, msg = refund_late_fee_payment(transaction_id="txn_123", amount=1, payment_gateway=mock_gateway)

    #check mock calls
    mock_gateway.refund_payment.assert_called_once()

    assert success == True
    assert "success" in msg.lower()

def test_refund_late_fee_payment_invalid_txn_id(mocker):
    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.refund_payment.return_value = (False, "Invalid transaction ID")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    success, msg = refund_late_fee_payment(transaction_id="txn123", amount=1, payment_gateway=mock_gateway)

    #check mock calls
    mock_gateway.refund_payment.assert_not_called()

    assert success == False
    assert "invalid transaction id" in msg.lower()

def test_refund_late_fee_payment_refund_negative(mocker):
    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.refund_payment.return_value = (False, "Invalid refund amount")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    success, msg = refund_late_fee_payment(transaction_id="txn_123", amount=-1, payment_gateway=mock_gateway)

    #check mock calls
    mock_gateway.refund_payment.assert_not_called()

    assert success == False
    assert "refund amount must be greater than 0" in msg.lower()

def test_refund_late_fee_payment_refund_zero(mocker):
    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    mock_gateway.refund_payment.return_value = (False, "Invalid refund amount")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    success, msg = refund_late_fee_payment(transaction_id="txn_123", amount=0, payment_gateway=mock_gateway)

    #check mock calls
    mock_gateway.refund_payment.assert_not_called()

    assert success == False
    assert "refund amount must be greater than 0" in msg.lower()

def test_refund_late_fee_payment_refund_exceeds_max(mocker):
    #create mock class of payment gateway class
    mock_gateway = Mock(spec=PaymentGateway)
    #notably, payment gateway doesn't have any protection against the refund amount being too high
    mock_gateway.refund_payment.return_value = (True, "Refund processed successfully")

    mocker.patch('services.library_service.PaymentGateway', return_value=mock_gateway)
    success, msg = refund_late_fee_payment(transaction_id="txn_123", amount=16, payment_gateway=mock_gateway)

    #check mock calls
    mock_gateway.refund_payment.assert_not_called()

    assert success == False
    assert "refund amount exceeds maximum late fee" in msg.lower()