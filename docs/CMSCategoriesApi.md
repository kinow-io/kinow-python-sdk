# CMSCategoriesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cms_category**](#create_cms_category) | **POST** /cms-categories | 
[**get_cms_categories**](#get_cms_categories) | **GET** /cms-categories | 
[**update_cms_category**](#update_cms_category) | **PUT** /cms-categories/{cms_category_id} | 


## **create_cms_category**
> CMSCategory create_cms_category(body)



Create cms category

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CMSCategoriesApi()
body = kaemo_client.CMSCategory() # CMSCategory | 

try: 
    api_response = api_instance.create_cms_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSCategoriesApi->create_cms_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CMSCategory**](#CMSCategory)|  | 

### Return type

[**CMSCategory**](#CMSCategory)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_cms_categories**
> CMSCategoriesLists get_cms_categories(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get cms categories

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CMSCategoriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |  ``` filters[name][value]=string&filters[name][operator]=contains&filters[date_add][value]=string&filters[date_add][operator]=lt _______________  {     \"name\": {         \"value\": \"string\",         \"operator\": \"contains\"     },     \"date_add\": {         \"value\": \"string\",         \"operator\": \"lt\"     } } ``` Operator can be strict, contains, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_cms_categories(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSCategoriesApi->get_cms_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|  &#x60;&#x60;&#x60; filters[name][value]&#x3D;string&amp;filters[name][operator]&#x3D;contains&amp;filters[date_add][value]&#x3D;string&amp;filters[date_add][operator]&#x3D;lt _______________  {     \&quot;name\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;contains\&quot;     },     \&quot;date_add\&quot;: {         \&quot;value\&quot;: \&quot;string\&quot;,         \&quot;operator\&quot;: \&quot;lt\&quot;     } } &#x60;&#x60;&#x60; Operator can be strict, contains, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**CMSCategoriesLists**](#CMSCategoriesLists)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_cms_category**
> CMSCategory update_cms_category(cms_category_id, body)



Update cms category

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CMSCategoriesApi()
cms_category_id = 789 # int | ID of the CMS category to update
body = kaemo_client.CMSCategory() # CMSCategory | 

try: 
    api_response = api_instance.update_cms_category(cms_category_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSCategoriesApi->update_cms_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cms_category_id** | **int**| ID of the CMS category to update | 
 **body** | [**CMSCategory**](#CMSCategory)|  | 

### Return type

[**CMSCategory**](#CMSCategory)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

