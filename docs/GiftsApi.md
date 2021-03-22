# GiftsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consume_gift**](#consume_gift) | **PUT** /gifts/{gift_id}/consume | 
[**create_gift**](#create_gift) | **POST** /gifts | 
[**delete_gift**](#delete_gift) | **DELETE** /gifts/{gift_id} | 
[**delete_gifts_in_cart**](#delete_gifts_in_cart) | **DELETE** /carts/{cart_id}/gift/ | 
[**get_gift**](#get_gift) | **GET** /gifts/{gift_id} | 
[**get_gift_in_cart**](#get_gift_in_cart) | **GET** /carts/{cart_id}/gift | 
[**get_gift_token**](#get_gift_token) | **GET** /gifts/{gift_id}/token | 
[**get_gifts**](#get_gifts) | **GET** /gifts | 
[**get_gifts_in_cart**](#get_gifts_in_cart) | **GET** /carts/{cart_id}/gifts | 
[**send_gift**](#send_gift) | **POST** /gifts/{gift_id}/send | 
[**update_gift**](#update_gift) | **PUT** /gifts/{gift_id} | 


## **consume_gift**
> consume_gift(gift_id, customer_id, token=token)



Consume Gift

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
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch
customer_id = 789 # int | Customer ID to fetch
token = 'token_example' # str | Gift token to check (optional) (optional)

try: 
    api_instance.consume_gift(gift_id, customer_id, token=token)
except ApiException as e:
    print("Exception when calling GiftsApi->consume_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **int**| Gift ID to fetch | 
 **customer_id** | **int**| Customer ID to fetch | 
 **token** | **str**| Gift token to check (optional) | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_gift**
> Gift create_gift(body)



Create Gift

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
api_instance = kinow_client.GiftsApi()
body = kinow_client.Gift2() # Gift2 | Gift settings

try: 
    api_response = api_instance.create_gift(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->create_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Gift2**](#Gift2)| Gift settings | 

### Return type

[**Gift**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_gift**
> delete_gift(gift_id)



Delete Gift

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
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch

try: 
    api_instance.delete_gift(gift_id)
except ApiException as e:
    print("Exception when calling GiftsApi->delete_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **int**| Gift ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_gifts_in_cart**
> delete_gifts_in_cart(cart_id)



Delete Gifts in cart

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
api_instance = kinow_client.GiftsApi()
cart_id = 789 # int | Cart ID to fetch

try: 
    api_instance.delete_gifts_in_cart(cart_id)
except ApiException as e:
    print("Exception when calling GiftsApi->delete_gifts_in_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_gift**
> Gift get_gift(gift_id)



Get Gift

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
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch

try: 
    api_response = api_instance.get_gift(gift_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->get_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **int**| Gift ID to fetch | 

### Return type

[**Gift**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_gift_in_cart**
> Gift get_gift_in_cart(cart_id)



Get Gift in Cart

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
api_instance = kinow_client.GiftsApi()
cart_id = 789 # int | Cart ID to fetch

try: 
    api_response = api_instance.get_gift_in_cart(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->get_gift_in_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 

### Return type

[**Gift**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_gift_token**
> GiftToken get_gift_token(gift_id)



Get Gift token

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
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch

try: 
    api_response = api_instance.get_gift_token(gift_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->get_gift_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **int**| Gift ID to fetch | 

### Return type

[**GiftToken**](#GiftToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_gifts**
> Gifts1 get_gifts(unused_only=unused_only, paid_only=paid_only, page=page, per_page=per_page)



Get Gifts

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
api_instance = kinow_client.GiftsApi()
unused_only = true # bool | Filter only unused gifts (optional)
paid_only = true # bool | Filter only gifts linked to an order which is paid by the user (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_gifts(unused_only=unused_only, paid_only=paid_only, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->get_gifts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unused_only** | **bool**| Filter only unused gifts | [optional] 
 **paid_only** | **bool**| Filter only gifts linked to an order which is paid by the user | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Gifts1**](#Gifts1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_gifts_in_cart**
> list[Gift] get_gifts_in_cart(cart_id)



Get Gifts in cart

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
api_instance = kinow_client.GiftsApi()
cart_id = 789 # int | Cart ID to fetch

try: 
    api_response = api_instance.get_gifts_in_cart(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->get_gifts_in_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 

### Return type

[**list[Gift]**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **send_gift**
> send_gift(gift_id)



Send Gift

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
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch

try: 
    api_instance.send_gift(gift_id)
except ApiException as e:
    print("Exception when calling GiftsApi->send_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **int**| Gift ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_gift**
> Gift update_gift(gift_id, body)



Update Gift

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
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch
body = kinow_client.Gift3() # Gift3 | Gift settings

try: 
    api_response = api_instance.update_gift(gift_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->update_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **int**| Gift ID to fetch | 
 **body** | [**Gift3**](#Gift3)| Gift settings | 

### Return type

[**Gift**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

