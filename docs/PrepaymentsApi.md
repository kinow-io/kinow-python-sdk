# PrepaymentsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_prepayment_balances**](#get_customer_prepayment_balances) | **GET** /customers/{customer_id}/prepayment-balance | 
[**get_customer_prepayment_operations**](#get_customer_prepayment_operations) | **GET** /customers/{customer_id}/prepayment-operations | 
[**get_prepayment_bonus**](#get_prepayment_bonus) | **GET** /prepayment/bonus/{prepayment_bonus_id} | 
[**get_prepayment_bonus_list**](#get_prepayment_bonus_list) | **GET** /prepayment/bonus | 
[**get_prepayment_operation**](#get_prepayment_operation) | **GET** /prepayment/operations/{prepayment_operation_id} | 
[**get_prepayment_operations**](#get_prepayment_operations) | **GET** /prepayment/operations | 
[**get_prepayment_recharge**](#get_prepayment_recharge) | **GET** /prepayment/recharges/{prepayment_recharge_id} | 
[**get_prepayment_recharges**](#get_prepayment_recharges) | **GET** /prepayment/recharges | 


## **get_customer_prepayment_balances**
> list[PrepaymentBalance] get_customer_prepayment_balances(customer_id)



Get PrepaymentBalances list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
customer_id = 789 # int | Customer ID to fetch

try: 
    api_response = api_instance.get_customer_prepayment_balances(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_customer_prepayment_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 

### Return type

[**list[PrepaymentBalance]**](#PrepaymentBalance)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_prepayment_operations**
> PrepaymentOperations get_customer_prepayment_operations(customer_id, type=type, page=page, per_page=per_page)



Get PrepaymentOperations list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
customer_id = 789 # int | Customer ID to fetch
type = 'type_example' # str |  (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_prepayment_operations(customer_id, type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_customer_prepayment_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **type** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PrepaymentOperations**](#PrepaymentOperations)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_bonus**
> PrepaymentBonus get_prepayment_bonus(prepayment_bonus_id)



Get PrepaymentBonus

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
prepayment_bonus_id = 789 # int | PrepaymentBonus ID to fetch

try: 
    api_response = api_instance.get_prepayment_bonus(prepayment_bonus_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_bonus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_bonus_id** | **int**| PrepaymentBonus ID to fetch | 

### Return type

[**PrepaymentBonus**](#PrepaymentBonus)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_bonus_list**
> PrepaymentBonus1 get_prepayment_bonus_list(page=page, per_page=per_page)



Get PrepaymentBonus list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_prepayment_bonus_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_bonus_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PrepaymentBonus1**](#PrepaymentBonus1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_operation**
> PrepaymentOperation get_prepayment_operation(prepayment_operation_id)



Get PrepaymentOperation

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
prepayment_operation_id = 789 # int | PrepaymentOperation ID to fetch

try: 
    api_response = api_instance.get_prepayment_operation(prepayment_operation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_operation_id** | **int**| PrepaymentOperation ID to fetch | 

### Return type

[**PrepaymentOperation**](#PrepaymentOperation)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_operations**
> PrepaymentOperations get_prepayment_operations(type=type, page=page, per_page=per_page)



Get PrepaymentOperations list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
type = 'type_example' # str |  (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_prepayment_operations(type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PrepaymentOperations**](#PrepaymentOperations)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_recharge**
> PrepaymentRecharge get_prepayment_recharge(prepayment_recharge_id)



Get PrepaymentRecharge

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
prepayment_recharge_id = 789 # int | PrepaymentRecharge ID to fetch

try: 
    api_response = api_instance.get_prepayment_recharge(prepayment_recharge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_recharge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_recharge_id** | **int**| PrepaymentRecharge ID to fetch | 

### Return type

[**PrepaymentRecharge**](#PrepaymentRecharge)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_recharges**
> PrepaymentRecharges get_prepayment_recharges(page=page, per_page=per_page)



Get PrepaymentRecharges list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PrepaymentsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_prepayment_recharges(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_recharges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PrepaymentRecharges**](#PrepaymentRecharges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

