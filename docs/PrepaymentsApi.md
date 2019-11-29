# PrepaymentsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prepayment_balances**](#get_prepayment_balances) | **GET** /customers/{customer_id}/prepayment-balance/{type} | 
[**get_prepayment_bonus**](#get_prepayment_bonus) | **GET** /prepayment/bonus | 
[**get_prepayment_bonus_0**](#get_prepayment_bonus_0) | **GET** /prepayment/bonus/{prepayment_bonus_id} | 
[**get_prepayment_operation**](#get_prepayment_operation) | **GET** /prepayment/operations/{prepayment_operation_id} | 
[**get_prepayment_operations**](#get_prepayment_operations) | **GET** /customers/{customer_id}/prepayment-operation/{type} | 
[**get_prepayment_recharge**](#get_prepayment_recharge) | **GET** /prepayment/recharges/{prepayment_recharge_id} | 
[**get_prepayment_recharges**](#get_prepayment_recharges) | **GET** /prepayment/recharges | 


## **get_prepayment_balances**
> PrepaymentBalance get_prepayment_balances(customer_id, type)



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
type = 'type_example' # str | PrepaymentBalance type to fetch (currency or credit)

try: 
    api_response = api_instance.get_prepayment_balances(customer_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **type** | **str**| PrepaymentBalance type to fetch (currency or credit) | 

### Return type

[**PrepaymentBalance**](#PrepaymentBalance)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_bonus**
> PrepaymentBonus1 get_prepayment_bonus(page=page, per_page=per_page)



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
    api_response = api_instance.get_prepayment_bonus(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_bonus: %s\n" % e)
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

## **get_prepayment_bonus_0**
> PrepaymentBonus get_prepayment_bonus_0(prepayment_bonus_id)



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
    api_response = api_instance.get_prepayment_bonus_0(prepayment_bonus_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_bonus_0: %s\n" % e)
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
> PrepaymentOperations get_prepayment_operations(customer_id, type, page=page, per_page=per_page)



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
type = 'type_example' # str | PrepaymentOperation type to fetch (currency or credit)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_prepayment_operations(customer_id, type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaymentsApi->get_prepayment_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **type** | **str**| PrepaymentOperation type to fetch (currency or credit) | 
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

