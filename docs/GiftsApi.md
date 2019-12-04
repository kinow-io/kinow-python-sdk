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
[**send_gift**](#send_gift) | **POST** /gifts/{gift_id}/send | 
[**update_gift**](#update_gift) | **PUT** /gifts/{gift_id} | 


## **consume_gift**
> consume_gift(gift_id, customer_id, token=token)



Consume gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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



Create gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GiftsApi()
body = kinow_client.Gift() # Gift | 

try: 
    api_response = api_instance.create_gift(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->create_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Gift**](#Gift)|  | 

### Return type

[**Gift**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_gift**
> delete_gift(gift_id)



Delete gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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



Delete gifts in cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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



Get gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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



Get gift in cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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



Get gift token

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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
> Gifts get_gifts(unused_only=unused_only)



Get gifts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GiftsApi()
unused_only = 56 # int | Only unused gifts (optional)

try: 
    api_response = api_instance.get_gifts(unused_only=unused_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftsApi->get_gifts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unused_only** | **int**| Only unused gifts | [optional] 

### Return type

[**Gifts**](#Gifts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **send_gift**
> send_gift(gift_id)



Send gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

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



Update gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GiftsApi()
gift_id = 789 # int | Gift ID to fetch
body = kinow_client.Gift() # Gift | 

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
 **body** | [**Gift**](#Gift)|  | 

### Return type

[**Gift**](#Gift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

