from services.payment_service import PaymentGateway
import time

test_gateway = PaymentGateway()
def test_process_payment_valid_input():
    success, txn_id, msg = test_gateway.process_payment(patron_id= '123456', amount= 1)

    assert success == True
    assert txn_id == f"txn_{'123456'}_{int(time.time())}"
    assert "processed successfully" in msg.lower()

def test_process_payment_invalid_id():
    success, txn_id, msg = test_gateway.process_payment(patron_id='1234567', amount=1)

    assert  success == False
    assert txn_id == ''
    assert "Invalid patron ID format".lower() in msg.lower()

def test_process_payment_amount_negative():
    success, txn_id, msg = test_gateway.process_payment(patron_id='123456', amount=-1)

    assert  success == False
    assert txn_id == ''
    assert "Invalid amount: must be greater than 0".lower() in msg.lower()

def test_process_payment_amount_zero():
    success, txn_id, msg = test_gateway.process_payment(patron_id='123456', amount=0)

    assert  success == False
    assert txn_id == ''
    assert "Invalid amount: must be greater than 0".lower() in msg.lower()

def test_process_payment_amount_above_max():
    success, txn_id, msg = test_gateway.process_payment(patron_id='123456', amount=1001)

    assert  success == False
    assert txn_id == ''
    assert "Payment declined: amount exceeds limit".lower() in msg.lower()