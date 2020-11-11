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
[**detach_cart_rule_from_cart**](#detach_cart_rule_from_cart) | **DELETE** /carts/{cart_id}/cart-rules/{cart_rule_id} | 
[**empty_cart**](#empty_cart) | **POST** /carts/{cart_id}/empty | 
[**get_cart**](#get_cart) | **GET** /carts/{cart_id} | 
[**get_carts**](#get_carts) | **GET** /carts | 
[**get_customer_carts**](#get_customer_carts) | **GET** /customers/{customer_id}/carts | 
[**get_last_cart**](#get_last_cart) | **GET** /customers/{customer_id}/last-cart | 
[**get_losts_carts**](#get_losts_carts) | **GET** /carts/losts-carts | 
[**get_payment_url**](#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
[**get_price**](#get_price) | **POST** /carts/price | 
[**prepare_payment**](#prepare_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/prepare | 
[**update_cart**](#update_cart) | **PUT** /carts/{cart_id} | 
[**validate_free_order**](#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
[**validate_payment**](#validate_payment) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 


## **add_product_to_cart**
> Cart add_product_to_cart(cart_id, product_id, product_attribute_id=product_attribute_id, switch_subscription_id=switch_subscription_id, is_gift=is_gift, ip_address=ip_address)



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
product_attribute_id = 789 # int | ProductAttribute ID, required to add product to cart if product is not a subscription (optional)
switch_subscription_id = 789 # int | When customer want to switch subscription, switch_subscription_id is the product access ID that match with the subscription to cancel (optional)
is_gift = false # bool | Allows bypass of access check (in case the current user already bought the product and it cannot be reordered) (optional) (default to false)
ip_address = 'ip_address_example' # str | IP address (optional)

try: 
    api_response = api_instance.add_product_to_cart(cart_id, product_id, product_attribute_id=product_attribute_id, switch_subscription_id=switch_subscription_id, is_gift=is_gift, ip_address=ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->add_product_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **product_id** | **int**| Product ID to add to cart | 
 **product_attribute_id** | **int**| ProductAttribute ID, required to add product to cart if product is not a subscription | [optional] 
 **switch_subscription_id** | **int**| When customer want to switch subscription, switch_subscription_id is the product access ID that match with the subscription to cancel | [optional] 
 **is_gift** | **bool**| Allows bypass of access check (in case the current user already bought the product and it cannot be reordered) | [optional] [default to false]
 **ip_address** | **str**| IP address | [optional] 

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
> Cart create_cart(body)



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
body = kinow_client.Cart1() # Cart1 | Cart settings

try: 
    api_response = api_instance.create_cart(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->create_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cart1**](#Cart1)| Cart settings | 

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

## **detach_cart_rule_from_cart**
> detach_cart_rule_from_cart(cart_id, cart_rule_id)



Detach Cart rule from Cart

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
cart_rule_id = 789 # int | Cart rule ID to detach

try: 
    api_instance.detach_cart_rule_from_cart(cart_id, cart_rule_id)
except ApiException as e:
    print("Exception when calling CartsApi->detach_cart_rule_from_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **cart_rule_id** | **int**| Cart rule ID to detach | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **empty_cart**
> empty_cart(cart_id)



Remove all items in a Cart

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
cart_id = 789 # int | Cart ID to empty

try: 
    api_instance.empty_cart(cart_id)
except ApiException as e:
    print("Exception when calling CartsApi->empty_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to empty | 

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

## **get_carts**
> Carts get_carts(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get Carts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     name[value]=string&name[operator]=contains&date_add[value]=string&date_add[operator]=lt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"contains\"     },     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_carts(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     name[value]&#x3D;string&amp;name[operator]&#x3D;contains&amp;date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     },     \&quot;date_add\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;lt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Carts**](#Carts)

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
filters = 'filters_example' # str |      ```     date_add[value]=string&date_add[operator]=lt     _______________      {     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)
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
 **filters** | **str**|      &#x60;&#x60;&#x60;     date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt     _______________      {     \&quot;date_add\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;lt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 
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

## **get_losts_carts**
> Carts get_losts_carts(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get losts Carts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |  ``` date_add[value]=string&date_add[operator]=lt _______________  {     \"date_add\": {         \"value\": \"string\",         \"operator\": \"lt\"     } } ``` Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_losts_carts(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_losts_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|  &#x60;&#x60;&#x60; date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt _______________  {     \&quot;date_add\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;lt\&quot;     } } &#x60;&#x60;&#x60; Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Carts**](#Carts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_url**
> PaymentUrl get_payment_url(cart_id, payment_name)



Get payment gateway URL to use in iframe

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
payment_name = 'payment_name_example' # str | Payment gateway name

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
 **payment_name** | **str**| Payment gateway name | 

### Return type

[**PaymentUrl**](#PaymentUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_price**
> list[CartPrice] get_price(body)



Get prices for multiple Carts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CartsApi()
body = kinow_client.CartIDList() # CartIDList | List of Cart IDs separated by comma, eg. '42,21,84'

try: 
    api_response = api_instance.get_price(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartIDList**](#CartIDList)| List of Cart IDs separated by comma, eg. &#39;42,21,84&#39; | 

### Return type

[**list[CartPrice]**](#CartPrice)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **prepare_payment**
> PaymentDetails1 prepare_payment(cart_id, payment_name, ip_address=ip_address)



Prepare payment on a payment gateway

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
payment_name = 'payment_name_example' # str | Payment gateway name
ip_address = 'ip_address_example' # str | Use IP address in payment process (optional)

try: 
    api_response = api_instance.prepare_payment(cart_id, payment_name, ip_address=ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->prepare_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment gateway name | 
 **ip_address** | **str**| Use IP address in payment process | [optional] 

### Return type

[**PaymentDetails1**](#PaymentDetails1)

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
body = kinow_client.Cart2() # Cart2 | Cart settings

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
 **body** | [**Cart2**](#Cart2)| Cart settings | 

### Return type

[**Cart**](#Cart)

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

## **validate_payment**
> validate_payment(cart_id, payment_name, payment_argument)



Validate payment on a payment gateway

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
payment_name = 'payment_name_example' # str | Payment gateway name
payment_argument = kinow_client.PaymentArguments() # PaymentArguments | Payment argument

try: 
    api_instance.validate_payment(cart_id, payment_name, payment_argument)
except ApiException as e:
    print("Exception when calling CartsApi->validate_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **payment_name** | **str**| Payment gateway name | 
 **payment_argument** | [**PaymentArguments**](#PaymentArguments)| Payment argument | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

