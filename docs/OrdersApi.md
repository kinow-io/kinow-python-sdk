# OrdersApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_orders**](#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
[**get_order**](#get_order) | **GET** /orders/{order_id} | 
[**get_order_histories**](#get_order_histories) | **GET** /orders/{order_id}/histories | 
[**get_order_invoice**](#get_order_invoice) | **GET** /orders/{order_id}/invoice | 


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
api_instance = kaemo_client.OrdersApi()
customer_id = 789 # int | ID of the customer to fetch
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
 **customer_id** | **int**| ID of the customer to fetch | 
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
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.OrdersApi()
order_id = 789 # int | ID of the order to fetch

try: 
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of the order to fetch | 

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
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.OrdersApi()
order_id = 789 # int | ID of the order to fetch
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
 **order_id** | **int**| ID of the order to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**OrderHistories**](#OrderHistories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_order_invoice**
> str get_order_invoice(order_id)



Get order invoice

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.OrdersApi()
order_id = 789 # int | ID of the order to fetch

try: 
    api_response = api_instance.get_order_invoice(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of the order to fetch | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

