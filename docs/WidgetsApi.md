# WidgetsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_intro_image**](#get_intro_image) | **GET** /widgets/intro/images | 
[**get_slider_images**](#get_slider_images) | **GET** /widgets/slider/images | 
[**get_widget_footer_menu**](#get_widget_footer_menu) | **GET** /widgets/footer-menu | 
[**get_widget_top_menu**](#get_widget_top_menu) | **GET** /widgets/top-menu | 


## **get_intro_image**
> list[Image] get_intro_image()



Get introduction image

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.WidgetsApi()

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

## **get_slider_images**
> list[Image] get_slider_images()



Get introduction image

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.WidgetsApi()

try: 
    api_response = api_instance.get_slider_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_slider_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Image]**](#Image)

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
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.WidgetsApi()
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

## **get_widget_top_menu**
> WidgetTopMenus get_widget_top_menu(page=page, per_page=per_page)



Get top menu list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.WidgetsApi()
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

