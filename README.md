# PESAFLUX-API-Python

## Introduction

**PESAFLUX-API-Python** is a Python library that provides a wrapper around the **PESAFLUX API**. This library allows you to easily interact with the PESAFLUX system using a simple set of Python functions, making it easier to integrate PESAFLUX functionalities into your Python-based projects.

## Documentation

For full details on the available API endpoints, parameters, and usage examples, please refer to the official PESAFLUX API documentation:

[PESAFLUX API Documentation](https://velelazesoftwares.co.ke/api/documentation/index.html)

## Installation

You can install the PESAFLUX-API-Python library by manually downloading the code.

1. Download the source code from this repository.
2. Include the `PesaFluxApi.py` file in your project.
3. Import and use the required classes as needed.

## Usage

To get started, include the `PesaFluxApi.py` file and initialize the API client.

### Example

```python
# Import the PESAFLUX-API-Python library
from PesaFluxApi import PesaFluxApi

# Initialize the API client with your PESAFLUX credentials
api = PesaFluxApi('your-username', 'your-api-key')

# Fetch account details
response = api.get_account_details()

if response['status'] == 'success':
    print('Account Name:', response['data']['account_name'])
else:
    print('Error:', response['message'])
