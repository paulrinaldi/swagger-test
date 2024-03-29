# testpaul2-pyth
This API allows for managing the pin configurations of an IoT device.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import testpaul2-pyth 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import testpaul2-pyth
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import testpaul2-pyth
from testpaul2-pyth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi(testpaul2-pyth.ApiClient(configuration))

try:
    # List all pins
    api_response = api_instance.pins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_get: %s\n" % e)

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi(testpaul2-pyth.ApiClient(configuration))
pin_id = 56 # int | The ID of the pin to delete.

try:
    # Delete a pin configuration
    api_instance.pins_pin_id_delete(pin_id)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_pin_id_delete: %s\n" % e)

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi(testpaul2-pyth.ApiClient(configuration))
pin_id = 56 # int | The ID of the pin to retrieve.

try:
    # Get a single pin configuration
    api_response = api_instance.pins_pin_id_get(pin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_pin_id_get: %s\n" % e)

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi(testpaul2-pyth.ApiClient(configuration))
body = testpaul2-pyth.Pin() # Pin | 
pin_id = 56 # int | The ID of the pin to update.

try:
    # Update a pin configuration
    api_response = api_instance.pins_pin_id_put(body, pin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_pin_id_put: %s\n" % e)

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi(testpaul2-pyth.ApiClient(configuration))
body = testpaul2-pyth.Pin() # Pin | 

try:
    # Create a new pin configuration
    api_response = api_instance.pins_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/PAULRINALDI_1/TestPaul2/1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**pins_get**](docs/DefaultApi.md#pins_get) | **GET** /pins | List all pins
*DefaultApi* | [**pins_pin_id_delete**](docs/DefaultApi.md#pins_pin_id_delete) | **DELETE** /pins/{pinId} | Delete a pin configuration
*DefaultApi* | [**pins_pin_id_get**](docs/DefaultApi.md#pins_pin_id_get) | **GET** /pins/{pinId} | Get a single pin configuration
*DefaultApi* | [**pins_pin_id_put**](docs/DefaultApi.md#pins_pin_id_put) | **PUT** /pins/{pinId} | Update a pin configuration
*DefaultApi* | [**pins_post**](docs/DefaultApi.md#pins_post) | **POST** /pins | Create a new pin configuration

## Documentation For Models

 - [Pin](docs/Pin.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


