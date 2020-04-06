# WidgetsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_intro_image**](#get_intro_image) | **GET** /widgets/intro/images | 
[**get_widget_analytics**](#get_widget_analytics) | **GET** /widgets/analytics | 
[**get_widget_footer_menu**](#get_widget_footer_menu) | **GET** /widgets/footer-menu | 
[**get_widget_hook_phrase**](#get_widget_hook_phrase) | **GET** /widgets/hook-phrase | 
[**get_widget_slider**](#get_widget_slider) | **GET** /widgets/slider | 
[**get_widget_slider_item**](#get_widget_slider_item) | **GET** /widgets/slider/{slider_id} | 
[**get_widget_top_menu**](#get_widget_top_menu) | **GET** /widgets/top-menu | 


## **get_intro_image**
> list[Image] get_intro_image()



Get introduction image

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()

try: 
    api_response = api_instance.get_intro_image()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_intro_image: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Image]**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_widget_analytics**
> GoogleAnalytics get_widget_analytics()



Get Google Analytics configuration

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()

try: 
    api_response = api_instance.get_widget_analytics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widget_analytics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GoogleAnalytics**](#GoogleAnalytics)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_widget_footer_menu**
> WidgetFooterMenus get_widget_footer_menu(page=page, per_page=per_page)



Get footer menu list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_widget_footer_menu(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widget_footer_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**WidgetFooterMenus**](#WidgetFooterMenus)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_widget_hook_phrase**
> WidgetHookPhrases get_widget_hook_phrase(page=page, per_page=per_page)



Get hook phrase list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_widget_hook_phrase(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widget_hook_phrase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**WidgetHookPhrases**](#WidgetHookPhrases)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_widget_slider**
> WidgetSliders get_widget_slider(page=page, per_page=per_page)



Get slider list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_widget_slider(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widget_slider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**WidgetSliders**](#WidgetSliders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_widget_slider_item**
> WidgetSlider get_widget_slider_item(slider_id)



Get slider item

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()
slider_id = 789 # int | Slider ID to fetch

try: 
    api_response = api_instance.get_widget_slider_item(slider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widget_slider_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slider_id** | **int**| Slider ID to fetch | 

### Return type

[**WidgetSlider**](#WidgetSlider)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_widget_top_menu**
> WidgetTopMenus get_widget_top_menu(page=page, per_page=per_page)



Get top menu list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.WidgetsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_widget_top_menu(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widget_top_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**WidgetTopMenus**](#WidgetTopMenus)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

