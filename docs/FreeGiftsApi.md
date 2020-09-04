# FreeGiftsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consume_free_gift**](#consume_free_gift) | **PUT** /free-gifts/{free_gift_id}/consume | 
[**create_free_gift**](#create_free_gift) | **POST** /free-gifts | 
[**delete_free_gift**](#delete_free_gift) | **DELETE** /free-gifts/{free_gift_id} | 
[**get_free_gift**](#get_free_gift) | **GET** /free-gifts/{free_gift_id} | 
[**get_free_gift_token**](#get_free_gift_token) | **GET** /free-gifts/{free_gift_id}/token | 
[**get_free_gifts**](#get_free_gifts) | **GET** /free-gifts | 
[**send_free_gift**](#send_free_gift) | **POST** /free-gifts/{free_gift_id}/send | 
[**update_free_gift**](#update_free_gift) | **PUT** /free-gifts/{free_gift_id} | 


## **consume_free_gift**
> consume_free_gift(free_gift_id, customer_id, token=token)



Consume free Gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
free_gift_id = 789 # int | Free Gift ID to fetch
customer_id = 789 # int | Customer ID to fetch
token = 'token_example' # str | Free Gift token to check (optional) (optional)

try: 
    api_instance.consume_free_gift(free_gift_id, customer_id, token=token)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->consume_free_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_gift_id** | **int**| Free Gift ID to fetch | 
 **customer_id** | **int**| Customer ID to fetch | 
 **token** | **str**| Free Gift token to check (optional) | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_free_gift**
> FreeGift create_free_gift(body)



Create free Gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
body = kinow_client.FreeGift1() # FreeGift1 | Free Gift settings

try: 
    api_response = api_instance.create_free_gift(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->create_free_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FreeGift1**](#FreeGift1)| Free Gift settings | 

### Return type

[**FreeGift**](#FreeGift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_free_gift**
> delete_free_gift(free_gift_id)



Delete free Gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
free_gift_id = 789 # int | Free Gift ID to fetch

try: 
    api_instance.delete_free_gift(free_gift_id)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->delete_free_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_gift_id** | **int**| Free Gift ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_free_gift**
> FreeGift get_free_gift(free_gift_id)



Get free Gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
free_gift_id = 789 # int | Free Gift ID to fetch

try: 
    api_response = api_instance.get_free_gift(free_gift_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->get_free_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_gift_id** | **int**| Free Gift ID to fetch | 

### Return type

[**FreeGift**](#FreeGift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_free_gift_token**
> GiftToken get_free_gift_token(free_gift_id)



Get free Gift token

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
free_gift_id = 789 # int | Free Gift ID to fetch

try: 
    api_response = api_instance.get_free_gift_token(free_gift_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->get_free_gift_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_gift_id** | **int**| Free Gift ID to fetch | 

### Return type

[**GiftToken**](#GiftToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_free_gifts**
> Gifts get_free_gifts(unused_only=unused_only)



Get free Gifts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
unused_only = 56 # int | Only unused Gifts (optional)

try: 
    api_response = api_instance.get_free_gifts(unused_only=unused_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->get_free_gifts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unused_only** | **int**| Only unused Gifts | [optional] 

### Return type

[**Gifts**](#Gifts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **send_free_gift**
> send_free_gift(free_gift_id)



Send free Gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
free_gift_id = 789 # int | Free Gift ID to fetch

try: 
    api_instance.send_free_gift(free_gift_id)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->send_free_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_gift_id** | **int**| Free Gift ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_free_gift**
> FreeGift update_free_gift(free_gift_id, body)



Update free Gift

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.FreeGiftsApi()
free_gift_id = 789 # int | Free Gift ID to fetch
body = kinow_client.Gift1() # Gift1 | Free Gift settings

try: 
    api_response = api_instance.update_free_gift(free_gift_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreeGiftsApi->update_free_gift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_gift_id** | **int**| Free Gift ID to fetch | 
 **body** | [**Gift1**](#Gift1)| Free Gift settings | 

### Return type

[**FreeGift**](#FreeGift)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

