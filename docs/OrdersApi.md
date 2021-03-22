# OrdersApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_orders**](#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
[**get_order**](#get_order) | **GET** /orders/{order_id} | 
[**get_order_histories**](#get_order_histories) | **GET** /orders/{order_id}/histories | 
[**get_order_invoice**](#get_order_invoice) | **GET** /orders/{order_id}/invoice | 
[**get_orders**](#get_orders) | **GET** /orders | 


## **get_customer_orders**
> Orders get_customer_orders(customer_id, page=page, per_page=per_page)



Get customer orders

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
api_instance = kinow_client.OrdersApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_orders(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_customer_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Orders**](#Orders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_order**
> Order get_order(order_id)



Get order

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
api_instance = kinow_client.OrdersApi()
order_id = 789 # int | Order ID to fetch

try: 
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID to fetch | 

### Return type

[**Order**](#Order)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_order_histories**
> OrderHistories get_order_histories(order_id, page=page, per_page=per_page)



Get order histories

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
api_instance = kinow_client.OrdersApi()
order_id = 789 # int | Order ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_order_histories(order_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_histories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**OrderHistories**](#OrderHistories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_order_invoice**
> str get_order_invoice(order_id, to_blob=to_blob)



Get order invoice

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
api_instance = kinow_client.OrdersApi()
order_id = 789 # int | Order ID to fetch
to_blob = true # bool | Get PDF content in blob (optional) (default to true)

try: 
    api_response = api_instance.get_order_invoice(order_id, to_blob=to_blob)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID to fetch | 
 **to_blob** | **bool**| Get PDF content in blob | [optional] [default to true]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_orders**
> Orders get_orders(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get order list

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
api_instance = kinow_client.OrdersApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |   email[value]=string&email[operator]=strict&firstname[value]=string&firstname[operator]=contains    ```  {      \"email\": {          \"value\": \"string\",          \"operator\": \"strict\"      },      \"firstname\": {          \"value\": \"string\",          \"operator\": \"contains\"      },      \"invoice_date\": {          \"value\": [\"Y-m-d\", \"Y-m-d\"],          \"operator\": \"between\"      }  }```  Operator can be strict, contains, between, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_orders(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|   email[value]&#x3D;string&amp;email[operator]&#x3D;strict&amp;firstname[value]&#x3D;string&amp;firstname[operator]&#x3D;contains    &#x60;&#x60;&#x60;  {      \&quot;email\&quot;: {          \&quot;value\&quot;: \&quot;string\&quot;,          \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;firstname\&quot;: {          \&quot;value\&quot;: \&quot;string\&quot;,          \&quot;operator\&quot;: \&quot;contains\&quot;      },      \&quot;invoice_date\&quot;: {          \&quot;value\&quot;: [\&quot;Y-m-d\&quot;, \&quot;Y-m-d\&quot;],          \&quot;operator\&quot;: \&quot;between\&quot;      }  }&#x60;&#x60;&#x60;  Operator can be strict, contains, between, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Orders**](#Orders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

