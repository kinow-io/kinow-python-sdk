# CategoriesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_categories**](#get_available_categories) | **GET** /categories-accesses | 
[**get_available_category**](#get_available_category) | **GET** /categories-accesses/{category_id} | 
[**get_categories**](#get_categories) | **GET** /categories | 
[**get_categories_from_category**](#get_categories_from_category) | **GET** /categories/{category_id}/categories | 
[**get_category**](#get_category) | **GET** /categories/{category_id} | 
[**get_category_banner**](#get_category_banner) | **GET** /categories/{category_id}/banner | 
[**get_category_features**](#get_category_features) | **GET** /categories/{category_id}/features | 
[**get_category_products**](#get_category_products) | **GET** /categories/{category_id}/products | 


## **get_available_categories**
> Categories get_available_categories(customer_id=customer_id, page=page, per_page=per_page)



Get available categories

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
customer_id = 789 # int | ID of the customer to fetch (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_available_categories(customer_id=customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_available_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Categories**](#Categories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_available_category**
> Category get_available_category(category_id, customer_id=customer_id)



Get available category

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
category_id = 789 # int | ID of the category to fetch
customer_id = 789 # int |  (optional)

try: 
    api_response = api_instance.get_available_category(category_id, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_available_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of the category to fetch | 
 **customer_id** | **int**|  | [optional] 

### Return type

[**Category**](#Category)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_categories**
> Categories get_categories(page=page, per_page=per_page, features=features, filters=filters)



Get categories list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
features = 'features_example' # str |  ``` features[*][value]=string&features[*][operator]=strict&features[1][value]=string&features[1][operator]=strict _______________  {     \"*\": {         \"value\": \"string\",         \"operator\": \"strict\"     },     \"1\": {         \"value\": \"string\",         \"operator\": \"contains\"     } } ``` Operator can be strict, contains, gt or lt. To search on all features, you can pass * as featureId. (optional)
filters = 'filters_example' # str |  ``` filters[name][value]=string&filters[name][operator]=strict&filters[description][value]=string&filters[description][operator]=contains _______________  {     \"name\": {         \"value\": \"string\",         \"operator\": \"strict\"     },     \"description\": {         \"value\": \"string\",         \"operator\": \"contains\"     } } ``` Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_categories(page=page, per_page=per_page, features=features, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **features** | **str**|  &#x60;&#x60;&#x60; features[*][value]&#x3D;string&amp;features[*][operator]&#x3D;strict&amp;features[1][value]&#x3D;string&amp;features[1][operator]&#x3D;strict _______________  {     \&quot;*\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;1\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;contains\&quot;     } } &#x60;&#x60;&#x60; Operator can be strict, contains, gt or lt. To search on all features, you can pass * as featureId. | [optional] 
 **filters** | **str**|  &#x60;&#x60;&#x60; filters[name][value]&#x3D;string&amp;filters[name][operator]&#x3D;strict&amp;filters[description][value]&#x3D;string&amp;filters[description][operator]&#x3D;contains _______________  {     \&quot;name\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;description\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;contains\&quot;     } } &#x60;&#x60;&#x60; Operator can be strict, contains, gt or lt. | [optional] 

### Return type

[**Categories**](#Categories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_categories_from_category**
> Categories get_categories_from_category(category_id, page=page, per_page=per_page)



Get categories list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
category_id = 789 # int | 
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_categories_from_category(category_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories_from_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Categories**](#Categories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category**
> Category get_category(category_id)



Get category

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
category_id = 789 # int | ID of the category to fetch

try: 
    api_response = api_instance.get_category(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of the category to fetch | 

### Return type

[**Category**](#Category)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_banner**
> Image get_category_banner(category_id)



Get banner of a category

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
category_id = 789 # int | ID of the category to fetch

try: 
    api_response = api_instance.get_category_banner(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_banner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of the category to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_features**
> Features get_category_features(category_id, page=page, per_page=per_page)



Get category features

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
category_id = 789 # int | ID of the category to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_category_features(category_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of the category to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Features**](#Features)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_products**
> Products get_category_products(category_id, page=page, per_page=per_page)



Get category products

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CategoriesApi()
category_id = 789 # int | ID of the category to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_category_products(category_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of the category to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Products**](#Products)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)
