# VideoGroupsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_group**](#get_video_group) | **GET** /video-groups/{video_group_id} | 
[**get_video_groups**](#get_video_groups) | **GET** /video-groups | 
[**get_video_groups_from_product**](#get_video_groups_from_product) | **GET** /products/{product_id}/video-groups | 


## **get_video_group**
> VideoGroup get_video_group(video_group_id)



Get video group

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.VideoGroupsApi()
video_group_id = 789 # int | Video group ID to fetch

try: 
    api_response = api_instance.get_video_group(video_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoGroupsApi->get_video_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_group_id** | **int**| Video group ID to fetch | 

### Return type

[**VideoGroup**](#VideoGroup)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_groups**
> VideoGroup1 get_video_groups(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get video group list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.VideoGroupsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     email[value]=string&email[operator]=strict&firstname[value]=string&firstname[operator]=contains     _______________      {     \"email\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"firstname\": {     \"value\": \"string\",     \"operator\": \"contains\"     }     } ```Operator can be strict, contains, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_video_groups(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoGroupsApi->get_video_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     email[value]&#x3D;string&amp;email[operator]&#x3D;strict&amp;firstname[value]&#x3D;string&amp;firstname[operator]&#x3D;contains     _______________      {     \&quot;email\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;firstname\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     }     } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**VideoGroup1**](#VideoGroup1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_groups_from_product**
> VideoGroup1 get_video_groups_from_product(product_id, page=page, filters=filters, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get Video Groups attached to product

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.VideoGroupsApi()
product_id = 789 # int | Product ID to fetch
page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     name[value]=string&name[operator]=strict&duration[value]=string&duration[operator]=gt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"duration\": {     \"value\": \"string\",     \"operator\": \"gt\"     }     } ```     Operator can be strict, contains, gt or lt. (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_video_groups_from_product(product_id, page=page, filters=filters, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoGroupsApi->get_video_groups_from_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
 **page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     name[value]&#x3D;string&amp;name[operator]&#x3D;strict&amp;duration[value]&#x3D;string&amp;duration[operator]&#x3D;gt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;duration\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;gt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be strict, contains, gt or lt. | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**VideoGroup1**](#VideoGroup1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

