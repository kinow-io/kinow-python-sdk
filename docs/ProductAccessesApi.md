# ProductAccessesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_access**](#create_product_access) | **POST** /product-accesses | 
[**delete_product_access**](#delete_product_access) | **DELETE** /product-accesses/{product_access_id} | 
[**get_customer_accesses_subscriptions**](#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
[**get_customer_accesses_videos**](#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
[**get_product_access**](#get_product_access) | **GET** /product-accesses/{product_access_id} | 
[**get_product_accesses**](#get_product_accesses) | **GET** /product-accesses | 
[**subscribe**](#subscribe) | **PUT** /product-accesses/{product_access_id}/subscribe | 
[**switch_subscription**](#switch_subscription) | **PUT** /product-accesses/{product_access_id}/switch | 
[**switch_subscription_delete**](#switch_subscription_delete) | **DELETE** /product-accesses/{product_access_id}/switch | 
[**switch_subscription_pending**](#switch_subscription_pending) | **GET** /product-accesses/{product_access_id}/switch | 
[**unsubscribe**](#unsubscribe) | **PUT** /product-accesses/{product_access_id}/unsubscribe | 
[**update_product_access**](#update_product_access) | **PUT** /product-accesses/{product_access_id} | 


## **create_product_access**
> ProductAccess create_product_access(body)



Create new product access

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
body = kinow_client.ProductAccess() # ProductAccess | 

try: 
    api_response = api_instance.create_product_access(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->create_product_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAccess**](#ProductAccess)|  | 

### Return type

[**ProductAccess**](#ProductAccess)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_product_access**
> delete_product_access(product_access_id)



Delete product access

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 789 # int | Access ID to fetch

try: 
    api_instance.delete_product_access(product_access_id)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->delete_product_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| Access ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_accesses_subscriptions**
> SubscriptionAccesses get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page, filters=filters)



Get customer accesses for subscription

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |       ```      type[value]=string&type[operator]=strict&cancel[value]=string&cancel[operator]=contains      _______________        {      \"type\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"cancel\": {      \"value\": \"string\",      \"operator\": \"contains\"      }      } ```Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_customer_accesses_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      type[value]&#x3D;string&amp;type[operator]&#x3D;strict&amp;cancel[value]&#x3D;string&amp;cancel[operator]&#x3D;contains      _______________        {      \&quot;type\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;cancel\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      }      } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_accesses_videos(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_customer_accesses_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_access**
> ProductAccess get_product_access(product_access_id)



Get product access

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 789 # int | Product access ID to fetch

try: 
    api_response = api_instance.get_product_access(product_access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_product_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| Product access ID to fetch | 

### Return type

[**ProductAccess**](#ProductAccess)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_accesses**
> SubscriptionAccesses get_product_accesses(page=page, per_page=per_page, type=type, date_add=date_add, date_add_direction=date_add_direction, date_exp=date_exp, date_exp_direction=date_exp_direction, filters=filters)



Get product accesses list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
type = 'type_example' # str | Filter by access type, available values are: video, sub (optional)
date_add = 'date_add_example' # str | Filter by creation date (optional)
date_add_direction = 'date_add_direction_example' # str | Choose the direction for date_add parameter, default value is after ,available values are: before, equal, after (optional)
date_exp = 'date_exp_example' # str | Filter by expiration date (optional)
date_exp_direction = 'date_exp_direction_example' # str | Choose the direction for date_exp parameter, default value is after ,available values are: before, equal, after (optional)
filters = 'filters_example' # str |       ```      type[value]=string&type[operator]=strict&cancel[value]=string&cancel[operator]=contains      _______________        {      \"type\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"cancel\": {      \"value\": \"string\",      \"operator\": \"contains\"      }      } ```Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_product_accesses(page=page, per_page=per_page, type=type, date_add=date_add, date_add_direction=date_add_direction, date_exp=date_exp, date_exp_direction=date_exp_direction, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_product_accesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **type** | **str**| Filter by access type, available values are: video, sub | [optional] 
 **date_add** | **str**| Filter by creation date | [optional] 
 **date_add_direction** | **str**| Choose the direction for date_add parameter, default value is after ,available values are: before, equal, after | [optional] 
 **date_exp** | **str**| Filter by expiration date | [optional] 
 **date_exp_direction** | **str**| Choose the direction for date_exp parameter, default value is after ,available values are: before, equal, after | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      type[value]&#x3D;string&amp;type[operator]&#x3D;strict&amp;cancel[value]&#x3D;string&amp;cancel[operator]&#x3D;contains      _______________        {      \&quot;type\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;cancel\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      }      } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **subscribe**
> subscribe(product_access_id)



Subcribe to a reccuring payment for an Access

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 789 # int | Access ID to fetch

try: 
    api_instance.subscribe(product_access_id)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| Access ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **switch_subscription**
> switch_subscription(product_access_id, subscription_id)



Switch an Access to another Subscription

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 'product_access_id_example' # str | Access ID to switch
subscription_id = 789 # int | Subscription to switch to

try: 
    api_instance.switch_subscription(product_access_id, subscription_id)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->switch_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **str**| Access ID to switch | 
 **subscription_id** | **int**| Subscription to switch to | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **switch_subscription_delete**
> switch_subscription_delete(product_access_id)



Delete Access pending switch

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 789 # int | Product access ID to fetch

try: 
    api_instance.switch_subscription_delete(product_access_id)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->switch_subscription_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| Product access ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **switch_subscription_pending**
> Subscription switch_subscription_pending(product_access_id)



Return Access pending switch

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 'product_access_id_example' # str | Access ID to fetch

try: 
    api_response = api_instance.switch_subscription_pending(product_access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->switch_subscription_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **str**| Access ID to fetch | 

### Return type

[**Subscription**](#Subscription)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **unsubscribe**
> unsubscribe(product_access_id)



Unsubcribe an Access recurring payment

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 789 # int | Access ID to fetch

try: 
    api_instance.unsubscribe(product_access_id)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| Access ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_product_access**
> ProductAccess update_product_access(product_access_id, body)



Update product access

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ProductAccessesApi()
product_access_id = 789 # int | Product access ID to update
body = kinow_client.ProductAccess() # ProductAccess | 

try: 
    api_response = api_instance.update_product_access(product_access_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->update_product_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| Product access ID to update | 
 **body** | [**ProductAccess**](#ProductAccess)|  | 

### Return type

[**ProductAccess**](#ProductAccess)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

