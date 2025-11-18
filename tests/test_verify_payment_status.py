from services.payment_service import PaymentGateway
import time

test_gateway = PaymentGateway()

def test_verify_payment_status_valid_input():
    txn_id = 'txn_123'
    result = test_gateway.verify_payment_status(txn_id)

    assert result['status'] == "completed"
    assert result['transaction_id'] == txn_id
    assert result['amount'] == 10.50
    assert result['timestamp'] == time.time()

def test_verify_payment_status_invalid_txn_id():
    txn_id = 'txn123'
    result = test_gateway.verify_payment_status(txn_id)

    assert result['status'] == "not_found"
    assert result['message'] == "Transaction not found"
