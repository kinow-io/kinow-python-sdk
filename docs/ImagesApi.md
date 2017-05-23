# ImagesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_category_banner**](#get_category_banner) | **GET** /categories/{category_id}/banner | 
[**get_intro_image**](#get_intro_image) | **GET** /widgets/intro/images | 
[**get_manufacturer_cover_image**](#get_manufacturer_cover_image) | **GET** /manufacturers/{manufacturer_id}/cover | 
[**get_product_cover_image**](#get_product_cover_image) | **GET** /products/{product_id}/cover | 
[**get_product_images**](#get_product_images) | **GET** /products/{product_id}/images | 
[**get_slider_images**](#get_slider_images) | **GET** /widgets/slider/images | 
[**get_subscription_cover_image**](#get_subscription_cover_image) | **GET** /subscriptions/{subscription_id}/cover | 
[**get_supplier_cover_image**](#get_supplier_cover_image) | **GET** /suppliers/{supplier_id}/cover | 
[**get_video_cover**](#get_video_cover) | **GET** /videos/{video_id}/cover | 


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
api_instance = kaemo_client.ImagesApi()
category_id = 789 # int | ID of the category to fetch

try: 
    api_response = api_instance.get_category_banner(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_category_banner: %s\n" % e)
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
api_instance = kaemo_client.ImagesApi()

try: 
    api_response = api_instance.get_intro_image()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_intro_image: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Image]**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_manufacturer_cover_image**
> Image get_manufacturer_cover_image(manufacturer_id)



Get cover image of a manufacturer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ImagesApi()
manufacturer_id = 789 # int | ID of the manufacturer to fetch

try: 
    api_response = api_instance.get_manufacturer_cover_image(manufacturer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_manufacturer_cover_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer_id** | **int**| ID of the manufacturer to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_cover_image**
> Image get_product_cover_image(product_id)



Get cover image of a product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ImagesApi()
product_id = 789 # int | ID of the product to fetch

try: 
    api_response = api_instance.get_product_cover_image(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_product_cover_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_images**
> ProductImagesResponse get_product_images(product_id, type=type, page=page, per_page=per_page)



Get images attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ImagesApi()
product_id = 789 # int | ID of the product to fetch
type = 'type_example' # str | type as screen_small or screen_large (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_images(product_id, type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_product_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **type** | **str**| type as screen_small or screen_large | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ProductImagesResponse**](#ProductImagesResponse)

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
api_instance = kaemo_client.ImagesApi()

try: 
    api_response = api_instance.get_slider_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_slider_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Image]**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_subscription_cover_image**
> Image get_subscription_cover_image(subscription_id)



Get cover image of a subscription

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ImagesApi()
subscription_id = 789 # int | ID of the subscription to fetch

try: 
    api_response = api_instance.get_subscription_cover_image(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_subscription_cover_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| ID of the subscription to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_supplier_cover_image**
> Image get_supplier_cover_image(supplier_id)



Get cover image of a supplier

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ImagesApi()
supplier_id = 789 # int | ID of the supplier to fetch

try: 
    api_response = api_instance.get_supplier_cover_image(supplier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_supplier_cover_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **int**| ID of the supplier to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_cover**
> Image get_video_cover(video)



Get video cover

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ImagesApi()
video = 789 # int | ID of the video to fetch

try: 
    api_response = api_instance.get_video_cover(video)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_video_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | **int**| ID of the video to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

