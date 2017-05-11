# CustomersApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cart_to_customer**](#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
[**check_customer_credentials**](#check_customer_credentials) | **POST** /customers/check-credentials | 
[**create_customer**](#create_customer) | **POST** /customers | 
[**create_facebook_id**](#create_facebook_id) | **POST** /facebook/customers | 
[**delete_customer**](#delete_customer) | **DELETE** /customers/{customer_id} | 
[**get_customer**](#get_customer) | **GET** /customers/{customer_id} | 
[**get_customer_accesses_subscriptions**](#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
[**get_customer_accesses_videos**](#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
[**get_customer_address**](#get_customer_address) | **GET** /customers/{customer_id}/address | 
[**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
[**get_customer_orders**](#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
[**get_customers**](#get_customers) | **GET** /customers | 
[**get_player_url**](#get_player_url) | **GET** /customers/{customer_id}/videos/{video_id}/player | 
[**update_customer**](#update_customer) | **PUT** /customers/{customer_id} | 


## **attach_cart_to_customer**
> Cart attach_cart_to_customer(customer_id, cart_id)



Attach cart to customer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch
cart_id = 789 # int | ID of the cart to attach

try: 
    api_response = api_instance.attach_cart_to_customer(customer_id, cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->attach_cart_to_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **cart_id** | **int**| ID of the cart to attach | 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **check_customer_credentials**
> Customer check_customer_credentials(email, password)



Check customer credentials

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
email = 'email_example' # str | Email of the customer to check
password = 'password_example' # str | Password of the customer to check

try: 
    api_response = api_instance.check_customer_credentials(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->check_customer_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the customer to check | 
 **password** | **str**| Password of the customer to check | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_customer**
> Customer create_customer(body)



Create new customer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
body = kaemo_client.Customer() # Customer | Created user object

try: 
    api_response = api_instance.create_customer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](#Customer)| Created user object | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_facebook_id**
> create_facebook_id(customer_id, facebook_id)



Create new Facebook ID for user

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | Customer ID
facebook_id = 'facebook_id_example' # str | Facebook ID

try: 
    api_instance.create_facebook_id(customer_id, facebook_id)
except ApiException as e:
    print("Exception when calling CustomersApi->create_facebook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID | 
 **facebook_id** | **str**| Facebook ID | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_customer**
> delete_customer(customer_id)



Delete customer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to delete

try: 
    api_instance.delete_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to delete | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer**
> Customer get_customer(customer_id)



Get customer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch

try: 
    api_response = api_instance.get_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_accesses_subscriptions**
> SubscriptionAccesses get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page)



Get customer accesses for subscription

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_accesses_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_accesses_videos**
> SubscriptionAccesses get_customer_accesses_videos(customer_id, page=page, per_page=per_page)



Get customer access for videos

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_accesses_videos(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_accesses_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_address**
> Address get_customer_address(customer_id)



Get customer address

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch

try: 
    api_response = api_instance.get_customer_address(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 

### Return type

[**Address**](#Address)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_has_access_to_video**
> get_customer_has_access_to_video(customer_id, video_id)



Get customer access to video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch
video_id = 789 # int | ID of the video to fetch

try: 
    api_instance.get_customer_has_access_to_video(customer_id, video_id)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_has_access_to_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **video_id** | **int**| ID of the video to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_orders**
> Orders get_customer_orders(customer_id, page=page, per_page=per_page)



Get customer orders

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_orders(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Orders**](#Orders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customers**
> Customers get_customers(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get customer list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     filters[email][value]=string&filters[email][operator]=strict&filters[firstname][value]=string&filters[firstname][operator]=contains     _______________      {     \"email\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"firstname\": {     \"value\": \"string\",     \"operator\": \"contains\"     }     } ```Operator can be strict, contains, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_customers(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     filters[email][value]&#x3D;string&amp;filters[email][operator]&#x3D;strict&amp;filters[firstname][value]&#x3D;string&amp;filters[firstname][operator]&#x3D;contains     _______________      {     \&quot;email\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;firstname\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     }     } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Customers**](#Customers)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_player_url**
> VideoUrl get_player_url(customer_id, video_id)



Get video player url

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | Id of the customer to fetch
video_id = 789 # int | Id of the video to fetch

try: 
    api_response = api_instance.get_player_url(customer_id, video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_player_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to fetch | 
 **video_id** | **int**| Id of the video to fetch | 

### Return type

[**VideoUrl**](#VideoUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_customer**
> Customer update_customer(customer_id, body)



Update customer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomersApi()
customer_id = 789 # int | ID of the customer to fetch
body = kaemo_client.Customer() # Customer | Body of the customer

try: 
    api_response = api_instance.update_customer(customer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **body** | [**Customer**](#Customer)| Body of the customer | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

