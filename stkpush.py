import json
#import secure config and payment_processor functions here
from secure_config import api_key, email
from payment_processor import make_payment

mpesa_number = input("Enter Mpesa Number: ")
amount = input("Enter Amount: ")
account_number = input("Enter Account Number: ")

# Process payment 
if mpesa_number and amount and account_number:
    result = make_payment(api_key, email, amount, mpesa_number, account_number)
    
    # Check the response and handle the result
    if result.get('success') == '200':
        result_code = result['success']
        message = result['message']
        transaction_request_id = result['transaction_request_id']

        # Output the transaction request ID
        print(f"transaction_request_id = {transaction_request_id}")
    else:
        print("Transaction Failed. Please retry")
