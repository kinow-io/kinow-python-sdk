# PaymentModulesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_methods**](#get_payment_methods) | **GET** /customers/{customer_id}/payments/{payment_name}/payment-methods | 
[**get_payment_methods_with_ip**](#get_payment_methods_with_ip) | **GET** /customers/{customer_id}/payments/{payment_name}/payment-methods/{ip_address} | 
[**get_payment_modules**](#get_payment_modules) | **GET** /payment-modules | 
[**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
[**get_pending_payments**](#get_pending_payments) | **GET** /customers/{customer_id}/payments/{payment_name}/pending | 
[**get_pending_payments_with_ip**](#get_pending_payments_with_ip) | **GET** /customers/{customer_id}/payments/{payment_name}/pending/{ip_address} | 
[**prepare_payment**](#prepare_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/prepare | 
[**update_payment_method**](#update_payment_method) | **PUT** /customers/{customer_id}/payments/{payment_name}/payment-method | 
[**validate_free_order**](#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
[**validate_payment**](#validate_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 


## **get_payment_methods**
> list[PaymentMethods] get_payment_methods(customer_id, payment_name)



Get payment methods saved for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
customer_id = 789 # int | 
payment_name = 'payment_name_example' # str | 

try: 
    api_response = api_instance.get_payment_methods(customer_id, payment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **payment_name** | **str**|  | 

### Return type

[**list[PaymentMethods]**](#PaymentMethods)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_methods_with_ip**
> list[PaymentMethods] get_payment_methods_with_ip(customer_id, payment_name, ip_address)



Get payment methods saved for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
customer_id = 789 # int | 
payment_name = 'payment_name_example' # str | 
ip_address = 'ip_address_example' # str | Filter by user IP

try: 
    api_response = api_instance.get_payment_methods_with_ip(customer_id, payment_name, ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_payment_methods_with_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **payment_name** | **str**|  | 
 **ip_address** | **str**| Filter by user IP | 

### Return type

[**list[PaymentMethods]**](#PaymentMethods)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_modules**
> PaymentModules get_payment_modules(page=page, per_page=per_page)



Get payment gateways list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
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



Get payment gateway URL to use in iframe

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment gateway name

try: 
    api_response = api_instance.get_payment_url(cart_id, payment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_payment_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment gateway name | 

### Return type

[**PaymentUrl**](#PaymentUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_pending_payments**
> list[PaymentDetails] get_pending_payments(payment_name, customer_id)



Get pending payments for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
payment_name = 'payment_name_example' # str | 
customer_id = 789 # int | 

try: 
    api_response = api_instance.get_pending_payments(payment_name, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_pending_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_name** | **str**|  | 
 **customer_id** | **int**|  | 

### Return type

[**list[PaymentDetails]**](#PaymentDetails)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_pending_payments_with_ip**
> list[PaymentDetails] get_pending_payments_with_ip(payment_name, customer_id, ip_address)



Get pending payments for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
payment_name = 'payment_name_example' # str | 
customer_id = 789 # int | 
ip_address = 'ip_address_example' # str | Filter by user IP

try: 
    api_response = api_instance.get_pending_payments_with_ip(payment_name, customer_id, ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_pending_payments_with_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_name** | **str**|  | 
 **customer_id** | **int**|  | 
 **ip_address** | **str**| Filter by user IP | 

### Return type

[**list[PaymentDetails]**](#PaymentDetails)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **prepare_payment**
> PaymentDetails1 prepare_payment(cart_id, payment_name, ip_address=ip_address)



Prepare payment on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment gateway name
ip_address = 'ip_address_example' # str | Filter by user IP (optional)

try: 
    api_response = api_instance.prepare_payment(cart_id, payment_name, ip_address=ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->prepare_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment gateway name | 
 **ip_address** | **str**| Filter by user IP | [optional] 

### Return type

[**PaymentDetails1**](#PaymentDetails1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_payment_method**
> update_payment_method(customer_id, payment_name, payment_arguments, ip_address=ip_address)



Update payment method for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
customer_id = 789 # int | 
payment_name = 'payment_name_example' # str | 
payment_arguments = kinow_client.PaymentArguments() # PaymentArguments | Payment arguments
ip_address = 'ip_address_example' # str | Filter by user IP (optional)

try: 
    api_instance.update_payment_method(customer_id, payment_name, payment_arguments, ip_address=ip_address)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->update_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **payment_name** | **str**|  | 
 **payment_arguments** | [**PaymentArguments**](#PaymentArguments)| Payment arguments | 
 **ip_address** | **str**| Filter by user IP | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **validate_free_order**
> validate_free_order(cart_id)



Validate cart without payment method (only for carts with a total of 0)

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to validate

try: 
    api_instance.validate_free_order(cart_id)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->validate_free_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to validate | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **validate_payment**
> validate_payment(cart_id, payment_name, payment_argument)



Validate payment on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment gateway name
payment_argument = kinow_client.PaymentArguments() # PaymentArguments | Payment argument

try: 
    api_instance.validate_payment(cart_id, payment_name, payment_argument)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->validate_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment gateway name | 
 **payment_argument** | [**PaymentArguments**](#PaymentArguments)| Payment argument | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

