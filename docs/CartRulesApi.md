# kaemo_client.CartRulesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cart_rule_to_cart**](#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
[**get_cart_rule**](#get_cart_rule) | **GET** /cart-rules/{cart_rule_id} | 
[**get_cart_rules**](#get_cart_rules) | **GET** /cart-rules | 


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

