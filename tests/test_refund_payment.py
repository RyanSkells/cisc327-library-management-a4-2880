from services.payment_service import PaymentGateway

test_gateway = PaymentGateway()
def test_refund_payment_valid_input():
    success, msg = test_gateway.refund_payment(transaction_id='txn_123', amount= 5)

    assert success == True
    assert "processed successfully" in msg.lower()

def test_refund_payment_invalid_txn_id():
    success, msg = test_gateway.refund_payment(transaction_id='txn123', amount= 5)

    assert success == False
    assert "Invalid transaction ID".lower() in msg.lower()

def test_refund_payment_amount_negative():
    success, msg = test_gateway.refund_payment(transaction_id='txn_123', amount= -1)

    assert success == False
    assert "Invalid refund amount".lower() in msg.lower()

def test_refund_payment_amount_zero():
    success, msg = test_gateway.refund_payment(transaction_id='txn_123', amount= 0)

    assert success == False
    assert "Invalid refund amount".lower() in msg.lower()