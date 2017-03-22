# kaemo_client.PaymentModulesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_modules**](#get_payment_modules) | **GET** /payment-modules | 
[**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 


## **get_payment_modules**
> PaymentModules get_payment_modules(page=page, per_page=per_page)



Get payment modules list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.PaymentModulesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_payment_modules(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_payment_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PaymentModules**](#PaymentModules)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_url**
> PaymentUrl get_payment_url(cart_id, payment_name)



Get payment url

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.PaymentModulesApi()
cart_id = 789 # int | Id of the cart to fetch
payment_name = 'payment_name_example' # str | Payment module name

try: 
    api_response = api_instance.get_payment_url(cart_id, payment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_payment_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to fetch | 
 **payment_name** | **str**| Payment module name | 

### Return type

[**PaymentUrl**](#PaymentUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

