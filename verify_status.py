import json
#import secure config and payment_processor functions here
from secure_config import api_key, email
from payment_processor import verify_payment

transaction_request_id = "paste transaction_request_id here"

# Process payment verification

result = verify_payment(api_key, email, transaction_request_id)

#check if the transaction code exists and is not empty
if result.get('TransactionCode') != '':
      
      transactionStatus = result['TransactionStatus']
      receipt = result['TransactionReceipt']
      amount = result['TransactionAmount']
      phone = result['Msisdn']
      transaction_description = result['ResultDesc'] 
      Mpesa_receipt = result ['TransactionReceipt']

      #to show the full response
      print(result)
else:
      print("Something went wrong!!")
  

