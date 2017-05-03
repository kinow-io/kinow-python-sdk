# OrderStatesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_state**](#get_order_state) | **GET** /order-states/{order_state_id} | 
[**get_order_states**](#get_order_states) | **GET** /order-states | 


## **get_order_state**
> OrderState get_order_state(order_state_id)



Get order state

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.OrderStatesApi()
order_state_id = 789 # int | ID of the order state to fetch

try: 
    api_response = api_instance.get_order_state(order_state_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatesApi->get_order_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_state_id** | **int**| ID of the order state to fetch | 

### Return type

[**OrderState**](#OrderState)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_order_states**
> OrderStates get_order_states(page=page, per_page=per_page)



Get order state list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.OrderStatesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_order_states(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatesApi->get_order_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**OrderStates**](#OrderStates)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

