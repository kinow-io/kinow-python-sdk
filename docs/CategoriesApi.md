# CategoriesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_features_to_category**](#attach_features_to_category) | **POST** /categories/{category_id}/features | 
[**create_category**](#create_category) | **POST** /categories | 
[**delete_category**](#delete_category) | **DELETE** /categories/{category_id} | 
[**get_available_category**](#get_available_category) | **GET** /categories-accesses/{category_id} | 
[**get_categories**](#get_categories) | **GET** /categories | 
[**get_categories_from_category**](#get_categories_from_category) | **GET** /categories/{category_id}/categories | 
[**get_category**](#get_category) | **GET** /categories/{category_id} | 
[**get_category_banner**](#get_category_banner) | **GET** /categories/{category_id}/banner | 
[**get_category_features**](#get_category_features) | **GET** /categories/{category_id}/features | 
[**get_category_images**](#get_category_images) | **GET** /categories/{category_id}/images | 
[**get_category_products**](#get_category_products) | **GET** /categories/{category_id}/products | 
[**get_category_video_player**](#get_category_video_player) | **GET** /categories/videos/{video_id}/player | 
[**get_category_video_subtitles**](#get_category_video_subtitles) | **GET** /categories/videos/{video_id}/subtitles | 
[**get_product_categories**](#get_product_categories) | **GET** /products/{product_id}/categories | 
[**get_subscription_categories**](#get_subscription_categories) | **GET** /subscriptions/{subscription_id}/categories | 
[**get_videos_from_categories**](#get_videos_from_categories) | **GET** /categories/videos | 
[**get_videos_from_category**](#get_videos_from_category) | **GET** /categories/{category_id}/videos | 
[**update_category**](#update_category) | **PUT** /categories/{category_id} | 
[**upload_category_cover**](#upload_category_cover) | **POST** /categories/{category_id}/cover | 
[**upload_category_image**](#upload_category_image) | **POST** /categories/{category_id}/image | 


## **attach_features_to_category**
> attach_features_to_category(category_id, features)



Attach feature to category

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | 
features = 'features_example' # str |      To attach existing FeatureValue to Category:     ```     [{     \"id_feature\":3,     \"id_feature_value\":5     }]     ```      To create a custom FeatureValue:     ```     [{     \"id_feature\":3,     \"custom_value\":[{     \"lang\": 1,     \"value\": \"string\"     }]     }]     ```

try: 
    api_instance.attach_features_to_category(category_id, features)
except ApiException as e:
    print("Exception when calling CategoriesApi->attach_features_to_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **features** | **str**|      To attach existing FeatureValue to Category:     &#x60;&#x60;&#x60;     [{     \&quot;id_feature\&quot;:3,     \&quot;id_feature_value\&quot;:5     }]     &#x60;&#x60;&#x60;      To create a custom FeatureValue:     &#x60;&#x60;&#x60;     [{     \&quot;id_feature\&quot;:3,     \&quot;custom_value\&quot;:[{     \&quot;lang\&quot;: 1,     \&quot;value\&quot;: \&quot;string\&quot;     }]     }]     &#x60;&#x60;&#x60; | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_category**
> Category create_category(body)



Create new category

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
body = kinow_client.Category() # Category | 

try: 
    api_response = api_instance.create_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Category**](#Category)|  | 

### Return type

[**Category**](#Category)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_category**
> delete_category(category_id)



Delete Category

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch

try: 
    api_instance.delete_category(category_id)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to fetch | 

### Return type

void (empty response body)

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch
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
 **category_id** | **int**| Category ID to fetch | 
 **customer_id** | **int**|  | [optional] 

### Return type

[**Category**](#Category)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_categories**
> Categories get_categories(page=page, per_page=per_page, features=features, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get categories list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
features = 'features_example' # str |  ``` features[*][value]=string&features[*][operator]=strict&features[1][value]=string&features[1][operator]=strict _______________  {     \"*\": {         \"value\": \"string\",         \"operator\": \"strict\"     },     \"1\": {         \"value\": \"string\",         \"operator\": \"contains\"     } } ``` Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). To search on all features, you can pass * as featureId. (optional)
filters = 'filters_example' # str |  ``` name[value]=string&name[operator]=strict&description[value]=string&description[operator]=contains _______________  {     \"name\": {         \"value\": \"string\",         \"operator\": \"strict\"     },     \"description\": {         \"value\": \"string\",         \"operator\": \"contains\"     } } ``` Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_categories(page=page, per_page=per_page, features=features, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **features** | **str**|  &#x60;&#x60;&#x60; features[*][value]&#x3D;string&amp;features[*][operator]&#x3D;strict&amp;features[1][value]&#x3D;string&amp;features[1][operator]&#x3D;strict _______________  {     \&quot;*\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;1\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;contains\&quot;     } } &#x60;&#x60;&#x60; Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). To search on all features, you can pass * as featureId. | [optional] 
 **filters** | **str**|  &#x60;&#x60;&#x60; name[value]&#x3D;string&amp;name[operator]&#x3D;strict&amp;description[value]&#x3D;string&amp;description[operator]&#x3D;contains _______________  {     \&quot;name\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;description\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;contains\&quot;     } } &#x60;&#x60;&#x60; Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Categories**](#Categories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_categories_from_category**
> Categories get_categories_from_category(category_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get categories list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | 
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_categories_from_category(category_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
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
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch

try: 
    api_response = api_instance.get_category(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to fetch | 

### Return type

[**Category**](#Category)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_banner**
> Image get_category_banner(category_id)



Get Category cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch

try: 
    api_response = api_instance.get_category_banner(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_banner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to fetch | 

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch
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
 **category_id** | **int**| Category ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Features**](#Features)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_images**
> CategoryImagesResponse get_category_images(category_id, type=type, page=page, per_page=per_page)



Get images attached to Category

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch
type = 'type_example' # str | Filter on specific Image type (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_category_images(category_id, type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to fetch | 
 **type** | **str**| Filter on specific Image type | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**CategoryImagesResponse**](#CategoryImagesResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_products**
> Products get_category_products(category_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction, ip=ip, features=features, filters=filters)



Get category products

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)
ip = 'ip_example' # str | Filter by user IP (optional)
features = 'features_example' # str |      ```     features[*][value]=string&features[*][operator]=strict&features[1][value]=string&features[1][operator]=strict     _______________      {     \"*\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"1\": {     \"value\": \"string\",     \"operator\": \"contains\"     }     } ```     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than).     To search on all features, you can pass * as featureId. (optional)
filters = 'filters_example' # str |      ```     name[value]=string&name][operator]=contains&date_add[value]=string&date_add[operator]=lt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"contains\"     },     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)

try: 
    api_response = api_instance.get_category_products(category_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction, ip=ip, features=features, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 
 **ip** | **str**| Filter by user IP | [optional] 
 **features** | **str**|      &#x60;&#x60;&#x60;     features[*][value]&#x3D;string&amp;features[*][operator]&#x3D;strict&amp;features[1][value]&#x3D;string&amp;features[1][operator]&#x3D;strict     _______________      {     \&quot;*\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;1\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than).     To search on all features, you can pass * as featureId. | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     name[value]&#x3D;string&amp;name][operator]&#x3D;contains&amp;date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     },     \&quot;date_add\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;lt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 

### Return type

[**Products**](#Products)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_video_player**
> Player get_category_video_player(video_id, customer_id=customer_id, country_id=country_id)



Get video player

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
video_id = 789 # int | Video ID to fetch
customer_id = 789 # int | Customer ID to fetch (optional)
country_id = 789 # int | Country ID to use in video analytics (optional)

try: 
    api_response = api_instance.get_category_video_player(video_id, customer_id=customer_id, country_id=country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_video_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Video ID to fetch | 
 **customer_id** | **int**| Customer ID to fetch | [optional] 
 **country_id** | **int**| Country ID to use in video analytics | [optional] 

### Return type

[**Player**](#Player)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_video_subtitles**
> VideoSubtitlesResponse get_category_video_subtitles(video_id, page=page, per_page=per_page)



Get subtitles of a video

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
video_id = 789 # int | Video ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_category_video_subtitles(video_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_video_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Video ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**VideoSubtitlesResponse**](#VideoSubtitlesResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_categories**
> Categories get_product_categories(product_id, page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get product categories

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
product_id = 789 # int | Product ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     name[value]=string&name[operator]=contains&date_add[value]=string&date_add[operator]=lt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"contains\"     },     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_product_categories(product_id, page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_product_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     name[value]&#x3D;string&amp;name[operator]&#x3D;contains&amp;date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     },     \&quot;date_add\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;lt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Categories**](#Categories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_subscription_categories**
> Categories get_subscription_categories(subscription_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get categories list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
subscription_id = 789 # int | 
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_subscription_categories(subscription_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_subscription_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Categories**](#Categories)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos_from_categories**
> Videos get_videos_from_categories(page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get Videos attached to Categories

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_videos_from_categories(page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_videos_from_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos_from_category**
> Videos get_videos_from_category(category_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get Videos attached to Category

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_videos_from_category(category_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_videos_from_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_category**
> Category update_category(category_id, body)



Update category

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 789 # int | Category ID to update
body = kinow_client.Category() # Category | 

try: 
    api_response = api_instance.update_category(category_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID to update | 
 **body** | [**Category**](#Category)|  | 

### Return type

[**Category**](#Category)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_category_cover**
> Image upload_category_cover(category_id, file, hash, hash_algorithm=hash_algorithm)



Upload Category cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 3.4 # float | Category ID to fetch
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_category_cover(category_id, file, hash, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->upload_category_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **float**| Category ID to fetch | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_category_image**
> Image upload_category_image(category_id, file, hash, image_type_name, hash_algorithm=hash_algorithm)



Upload Category image

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CategoriesApi()
category_id = 3.4 # float | Category ID to fetch
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
image_type_name = 'image_type_name_example' # str | Image types name to use to generate image assets
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_category_image(category_id, file, hash, image_type_name, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->upload_category_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **float**| Category ID to fetch | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **image_type_name** | **str**| Image types name to use to generate image assets | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

