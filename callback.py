import json

# Read the raw JSON data from the incoming request
stk_callback_response = input()  

# Log the response to a file
log_file = "response.json"
with open(log_file, "a") as log:
    log.write(stk_callback_response + "\n")

# Decode the response to extract individual fields
data = json.loads(stk_callback_response)

# Extract the relevant information
checkout_request_id = data['Body']['stkCallback']['CheckoutRequestID']
merchant_request_id = data['Body']['stkCallback']['MerchantRequestID']
result_code = data['Body']['stkCallback']['ResultCode']
amount = data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
transaction_id = data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
phone_number = data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']



