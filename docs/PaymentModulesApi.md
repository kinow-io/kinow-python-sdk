# PaymentModulesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cart_payment_modules**](#get_cart_payment_modules) | **GET** /carts/{cart_id}/payments | 
[**get_payment_methods**](#get_payment_methods) | **GET** /customers/{customer_id}/payments/{payment_name}/payment-methods | 
[**get_payment_methods_with_ip**](#get_payment_methods_with_ip) | **GET** /customers/{customer_id}/payments/{payment_name}/payment-methods/{ip_address} | 
[**get_payment_modules**](#get_payment_modules) | **GET** /payment-modules | 
[**get_payment_token**](#get_payment_token) | **GET** /payment-modules/token/{token} | 
[**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
[**get_pending_payments**](#get_pending_payments) | **GET** /customers/{customer_id}/payments/{payment_name}/pending | 
[**get_pending_payments_with_ip**](#get_pending_payments_with_ip) | **GET** /customers/{customer_id}/payments/{payment_name}/pending/{ip_address} | 
[**prepare_payment**](#prepare_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/prepare | 
[**recurring_payment**](#recurring_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/recurring | 
[**update_payment_method**](#update_payment_method) | **PUT** /customers/{customer_id}/payments/{payment_name}/payment-method | 
[**validate_free_order**](#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
[**validate_payment**](#validate_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 


## **get_cart_payment_modules**
> PaymentModules get_cart_payment_modules(cart_id, page=page, per_page=per_page)



Get payment gateways list available for given cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_cart_payment_modules(cart_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_cart_payment_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PaymentModules**](#PaymentModules)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_methods**
> list[PaymentMethodsResponse] get_payment_methods(customer_id, payment_name)



Get payment methods saved for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

[**list[PaymentMethodsResponse]**](#PaymentMethodsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_methods_with_ip**
> list[PaymentMethodsResponse] get_payment_methods_with_ip(customer_id, payment_name, ip_address)



Get payment methods saved for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

[**list[PaymentMethodsResponse]**](#PaymentMethodsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_modules**
> PaymentModuleListResponse get_payment_modules(page=page, per_page=per_page)



Get payment gateways list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

[**PaymentModuleListResponse**](#PaymentModuleListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_token**
> PaymentToken1 get_payment_token(token)



Get payment token details

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
token = 56 # int | Token to fetch

try: 
    api_response = api_instance.get_payment_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->get_payment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **int**| Token to fetch | 

### Return type

[**PaymentToken1**](#PaymentToken1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_url**
> PaymentUrlResponse get_payment_url(cart_id, payment_name)



Get payment gateway URL to use in iframe

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

[**PaymentUrlResponse**](#PaymentUrlResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_pending_payments**
> list[PaymentDetailsResponse] get_pending_payments(payment_name, customer_id)



Get pending payments for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

[**list[PaymentDetailsResponse]**](#PaymentDetailsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_pending_payments_with_ip**
> PaymentDetailsListResponse get_pending_payments_with_ip(payment_name, customer_id, ip_address)



Get pending payments for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

[**PaymentDetailsListResponse**](#PaymentDetailsListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **prepare_payment**
> PaymentDetailsResponse1 prepare_payment(cart_id, payment_name, ip_address=ip_address)



Prepare payment on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment gateway name
ip_address = 'ip_address_example' # str | Use IP address in payment process (optional)

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
 **ip_address** | **str**| Use IP address in payment process | [optional] 

### Return type

[**PaymentDetailsResponse1**](#PaymentDetailsResponse1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **recurring_payment**
> recurring_payment(cart_id, payment_name, payment_argument)



Validate recurring payment on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment gateway name
payment_argument = kinow_client.PaymentArguments() # PaymentArguments | Payment argument

try: 
    api_instance.recurring_payment(cart_id, payment_name, payment_argument)
except ApiException as e:
    print("Exception when calling PaymentModulesApi->recurring_payment: %s\n" % e)
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

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
customer_id = 789 # int | 
payment_name = 'payment_name_example' # str | 
payment_arguments = kinow_client.UpdatePaymentRequest() # UpdatePaymentRequest | Payment arguments
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
 **payment_arguments** | [**UpdatePaymentRequest**](#UpdatePaymentRequest)| Payment arguments | 
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

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.PaymentModulesApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment gateway name
payment_argument = kinow_client.PaymentArgumentsResponse() # PaymentArgumentsResponse | Payment argument

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
 **payment_argument** | [**PaymentArgumentsResponse**](#PaymentArgumentsResponse)| Payment argument | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

