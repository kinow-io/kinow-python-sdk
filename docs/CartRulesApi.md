# CartRulesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cart_rule_to_cart**](#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
[**create_cart_rule**](#create_cart_rule) | **POST** /cart-rules | 
[**delete_cart_rule**](#delete_cart_rule) | **DELETE** /cart-rules/{cart_rule_id} | 
[**get_cart_rule**](#get_cart_rule) | **GET** /cart-rules/{cart_rule_id} | 
[**get_cart_rules**](#get_cart_rules) | **GET** /cart-rules | 
[**update_cart_rule**](#update_cart_rule) | **PUT** /cart-rules/{cart_rule_id} | 


## **attach_cart_rule_to_cart**
> attach_cart_rule_to_cart(cart_id, code)



Attach cart rule to cart

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CartRulesApi()
cart_id = 'cart_id_example' # str | Id of the cart to fetch
code = 'code_example' # str | Code of the cart rule to attach

try: 
    api_instance.attach_cart_rule_to_cart(cart_id, code)
except ApiException as e:
    print("Exception when calling CartRulesApi->attach_cart_rule_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| Id of the cart to fetch | 
 **code** | **str**| Code of the cart rule to attach | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_cart_rule**
> create_cart_rule(body)



Create new cart rule

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CartRulesApi()
body = kaemo_client.CartRule() # CartRule | 

try: 
    api_instance.create_cart_rule(body)
except ApiException as e:
    print("Exception when calling CartRulesApi->create_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartRule**](#CartRule)|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_cart_rule**
> delete_cart_rule(cart_rule_id)



Delete cart rule

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CartRulesApi()
cart_rule_id = 56 # int | 

try: 
    api_instance.delete_cart_rule(cart_rule_id)
except ApiException as e:
    print("Exception when calling CartRulesApi->delete_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_rule_id** | **int**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_cart_rule**
> CartRule get_cart_rule(cart_rule_id)



Get cart rule by id

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CartRulesApi()
cart_rule_id = 789 # int | ID of the cart rule to fetch

try: 
    api_response = api_instance.get_cart_rule(cart_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartRulesApi->get_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_rule_id** | **int**| ID of the cart rule to fetch | 

### Return type

[**CartRule**](#CartRule)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_cart_rules**
> CartRules get_cart_rules(page=page, per_page=per_page)



Get cart rules list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CartRulesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_cart_rules(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartRulesApi->get_cart_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**CartRules**](#CartRules)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_cart_rule**
> update_cart_rule(cart_rule_id, body)



Update cart rule

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CartRulesApi()
cart_rule_id = 56 # int | 
body = kaemo_client.CartRule() # CartRule | 

try: 
    api_instance.update_cart_rule(cart_rule_id, body)
except ApiException as e:
    print("Exception when calling CartRulesApi->update_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_rule_id** | **int**|  | 
 **body** | [**CartRule**](#CartRule)|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

