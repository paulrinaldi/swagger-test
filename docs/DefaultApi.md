# testpaul2-pyth.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/PAULRINALDI_1/TestPaul2/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pins_get**](DefaultApi.md#pins_get) | **GET** /pins | List all pins
[**pins_pin_id_delete**](DefaultApi.md#pins_pin_id_delete) | **DELETE** /pins/{pinId} | Delete a pin configuration
[**pins_pin_id_get**](DefaultApi.md#pins_pin_id_get) | **GET** /pins/{pinId} | Get a single pin configuration
[**pins_pin_id_put**](DefaultApi.md#pins_pin_id_put) | **PUT** /pins/{pinId} | Update a pin configuration
[**pins_post**](DefaultApi.md#pins_post) | **POST** /pins | Create a new pin configuration

# **pins_get**
> list[Pin] pins_get()

List all pins

Retrieve a list of all pins with their current configurations.

### Example
```python
from __future__ import print_function
import time
import testpaul2-pyth
from testpaul2-pyth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi()

try:
    # List all pins
    api_response = api_instance.pins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Pin]**](Pin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_pin_id_delete**
> pins_pin_id_delete(pin_id)

Delete a pin configuration

Remove a pin configuration from the IoT device.

### Example
```python
from __future__ import print_function
import time
import testpaul2-pyth
from testpaul2-pyth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi()
pin_id = 56 # int | The ID of the pin to delete.

try:
    # Delete a pin configuration
    api_instance.pins_pin_id_delete(pin_id)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_pin_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_id** | **int**| The ID of the pin to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_pin_id_get**
> Pin pins_pin_id_get(pin_id)

Get a single pin configuration

Retrieve the configuration of a specific pin by its ID.

### Example
```python
from __future__ import print_function
import time
import testpaul2-pyth
from testpaul2-pyth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi()
pin_id = 56 # int | The ID of the pin to retrieve.

try:
    # Get a single pin configuration
    api_response = api_instance.pins_pin_id_get(pin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_pin_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_id** | **int**| The ID of the pin to retrieve. | 

### Return type

[**Pin**](Pin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_pin_id_put**
> Pin pins_pin_id_put(body, pin_id)

Update a pin configuration

Update the configuration of an existing pin.

### Example
```python
from __future__ import print_function
import time
import testpaul2-pyth
from testpaul2-pyth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi()
body = testpaul2-pyth.Pin() # Pin | 
pin_id = 56 # int | The ID of the pin to update.

try:
    # Update a pin configuration
    api_response = api_instance.pins_pin_id_put(body, pin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_pin_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pin**](Pin.md)|  | 
 **pin_id** | **int**| The ID of the pin to update. | 

### Return type

[**Pin**](Pin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_post**
> Pin pins_post(body)

Create a new pin configuration

Add a new pin configuration to the IoT device.

### Example
```python
from __future__ import print_function
import time
import testpaul2-pyth
from testpaul2-pyth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = testpaul2-pyth.DefaultApi()
body = testpaul2-pyth.Pin() # Pin | 

try:
    # Create a new pin configuration
    api_response = api_instance.pins_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pins_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pin**](Pin.md)|  | 

### Return type

[**Pin**](Pin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

