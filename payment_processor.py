"""
Youll need to install requests by running this command on any terminal
pip install requests
"""
import json
import requests

def make_payment(api_key, email, amount, msisdn, reference):
    url = 'https://velelazesoftwares.co.ke/api/initiatestk'
    payload = {
        "api_key": api_key,
        "email": email,
        "amount": amount,
        "msisdn": msisdn,
        "reference": reference,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    
    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
  
  
  
def verify_payment(api_key, email, transaction_request_id):
    url = 'https://velelazesoftwares.co.ke/api/transactionstatus'
    payload = {
        "api_key": api_key,
        "email": email,
        "transaction_request_id": transaction_request_id,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    
    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
   