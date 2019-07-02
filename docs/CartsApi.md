# CartsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_to_cart**](#add_product_to_cart) | **POST** /carts/{cart_id}/products | 
[**attach_cart_rule_to_cart**](#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
[**attach_cart_to_customer**](#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
[**create_cart**](#create_cart) | **POST** /carts | 
[**delete_cart**](#delete_cart) | **DELETE** /carts/{cart_id} | 
[**delete_product_from_cart**](#delete_product_from_cart) | **DELETE** /carts/{cart_id}/products | 
[**get_cart**](#get_cart) | **GET** /carts/{cart_id} | 
[**get_customer_carts**](#get_customer_carts) | **GET** /customers/{customer_id}/carts | 
[**get_last_cart**](#get_last_cart) | **GET** /customers/{customer_id}/last-cart | 
[**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
[**update_cart**](#update_cart) | **PUT** /carts/{cart_id} | 
[**validate_cart**](#validate_cart) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 
[**validate_free_order**](#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 


## **add_product_to_cart**
> Cart add_product_to_cart(cart_id, product_id, product_attribute_id=product_attribute_id, switch_subscription_id=switch_subscription_id)



Add product to cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch
product_id = 789 # int | Product ID to add to cart
product_attribute_id = 789 # int | Product attribute ID, required to add product to cart if product is not a subscription (optional)
switch_subscription_id = 789 # int | When customer want to switch subscription, switch_subscription_id is the product access ID that match with the subscription to cancel (optional)

try: 
    api_response = api_instance.add_product_to_cart(cart_id, product_id, product_attribute_id=product_attribute_id, switch_subscription_id=switch_subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->add_product_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **product_id** | **int**| Product ID to add to cart | 
 **product_attribute_id** | **int**| Product attribute ID, required to add product to cart if product is not a subscription | [optional] 
 **switch_subscription_id** | **int**| When customer want to switch subscription, switch_subscription_id is the product access ID that match with the subscription to cancel | [optional] 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **attach_cart_rule_to_cart**
> attach_cart_rule_to_cart(cart_id, code)



Attach cart rule to cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch
code = 'code_example' # str | Code of the cart rule to attach

try: 
    api_instance.attach_cart_rule_to_cart(cart_id, code)
except ApiException as e:
    print("Exception when calling CartsApi->attach_cart_rule_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **code** | **str**| Code of the cart rule to attach | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **attach_cart_to_customer**
> Cart attach_cart_to_customer(customer_id, cart_id)



Attach cart to customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
customer_id = 789 # int | Customer ID to fetch
cart_id = 789 # int | Cart ID to attach

try: 
    api_response = api_instance.attach_cart_to_customer(customer_id, cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->attach_cart_to_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **cart_id** | **int**| Cart ID to attach | 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_cart**
> Cart create_cart(body=body)



Create new cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
body = kinow_client.CartBody() # CartBody | Create cart object (optional)

try: 
    api_response = api_instance.create_cart(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->create_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartBody**](#CartBody)| Create cart object | [optional] 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_cart**
> delete_cart(cart_id)



Delete cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch

try: 
    api_instance.delete_cart(cart_id)
except ApiException as e:
    print("Exception when calling CartsApi->delete_cart: %s\n" % e)
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

## **delete_product_from_cart**
> delete_product_from_cart(cart_id, product_id, product_attribute_id=product_attribute_id)



Remove product from cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch
product_id = 789 # int | Product ID to delete from cart
product_attribute_id = 789 # int | Product attribute ID, required to add product to cart if product is not a subscription (optional)

try: 
    api_instance.delete_product_from_cart(cart_id, product_id, product_attribute_id=product_attribute_id)
except ApiException as e:
    print("Exception when calling CartsApi->delete_product_from_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **product_id** | **int**| Product ID to delete from cart | 
 **product_attribute_id** | **int**| Product attribute ID, required to add product to cart if product is not a subscription | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_cart**
> Cart get_cart(cart_id)



Get cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch

try: 
    api_response = api_instance.get_cart(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_carts**
> Carts get_customer_carts(customer_id, page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get customer carts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     date_add[value]=string&date_add[operator]=lt     _______________      {     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```     Operator can be strict, contains, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_customer_carts(customer_id, page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_customer_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt     _______________      {     \&quot;date_add\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;lt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be strict, contains, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Carts**](#Carts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_last_cart**
> Cart get_last_cart(customer_id)



Get customer last cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
customer_id = 789 # int | Customer ID to fetch

try: 
    api_response = api_instance.get_last_cart(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_last_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_url**
> PaymentUrl get_payment_url(cart_id, payment_name)



Get payment url

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment module name

try: 
    api_response = api_instance.get_payment_url(cart_id, payment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_payment_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment module name | 

### Return type

[**PaymentUrl**](#PaymentUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_cart**
> Cart update_cart(cart_id, body)



Update cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart id
body = kinow_client.Cart() # Cart | Cart body

try: 
    api_response = api_instance.update_cart(cart_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->update_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart id | 
 **body** | [**Cart**](#Cart)| Cart body | 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **validate_cart**
> validate_cart(cart_id, payment_name, payment_arguments)



Validate order

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to fetch
payment_name = 'payment_name_example' # str | Payment module name
payment_arguments = kinow_client.PaymentArguments() # PaymentArguments | payment arguments, token and tokenType

try: 
    api_instance.validate_cart(cart_id, payment_name, payment_arguments)
except ApiException as e:
    print("Exception when calling CartsApi->validate_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment module name | 
 **payment_arguments** | [**PaymentArguments**](#PaymentArguments)| payment arguments, token and tokenType | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **validate_free_order**
> validate_free_order(cart_id)



Validate cart without payment method (only for carts with a total of 0)

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to validate

try: 
    api_instance.validate_free_order(cart_id)
except ApiException as e:
    print("Exception when calling CartsApi->validate_free_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to validate | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

