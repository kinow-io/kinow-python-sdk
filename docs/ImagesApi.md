# ImagesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_screenshot**](#delete_product_screenshot) | **DELETE** /products/{product_id}/screenshots/{image_id} | 
[**get_actor_cover_image**](#get_actor_cover_image) | **GET** /actors/{actor_id}/cover | 
[**get_category_banner**](#get_category_banner) | **GET** /categories/{category_id}/banner | 
[**get_director_cover_image**](#get_director_cover_image) | **GET** /directors/{director_id}/cover | 
[**get_intro_image**](#get_intro_image) | **GET** /widgets/intro/images | 
[**get_product_cover_image**](#get_product_cover_image) | **GET** /products/{product_id}/cover | 
[**get_product_images**](#get_product_images) | **GET** /products/{product_id}/images | 
[**get_product_screenshots**](#get_product_screenshots) | **GET** /products/{product_id}/screenshots | 
[**get_subscription_cover_image**](#get_subscription_cover_image) | **GET** /subscriptions/{subscription_id}/cover | 
[**get_video_cover**](#get_video_cover) | **GET** /videos/{video_id}/cover | 
[**upload_actor_cover**](#upload_actor_cover) | **POST** /actors/{actor_id}/cover | 
[**upload_category_banner**](#upload_category_banner) | **POST** /category/{category_id}/banner | 
[**upload_director_cover**](#upload_director_cover) | **POST** /directors/{director_id}/cover | 
[**upload_product_cover**](#upload_product_cover) | **POST** /products/{product_id}/cover | 
[**upload_product_screenshot**](#upload_product_screenshot) | **PUT** /products/{product_id}/screenshots/{image_id} | 
[**upload_product_screenshots**](#upload_product_screenshots) | **POST** /products/{product_id}/screenshots | 
[**upload_subscription_cover**](#upload_subscription_cover) | **POST** /subscriptions/{subscription_id}/cover | 


## **delete_product_screenshot**
> delete_product_screenshot(product_id, image_id)



Delete product screenshot

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
product_id = 3.4 # float | Id of the product
image_id = 3.4 # float | Id of the image to delete

try: 
    api_instance.delete_product_screenshot(product_id, image_id)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_product_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| Id of the product | 
 **image_id** | **float**| Id of the image to delete | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_actor_cover_image**
> Image get_actor_cover_image(actor_id)



Get cover image of an actor

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
actor_id = 789 # int | ID of the actor to fetch

try: 
    api_response = api_instance.get_actor_cover_image(actor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_actor_cover_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **int**| ID of the actor to fetch | 

### Return type

[**Image**](#Image)

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
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

## **get_director_cover_image**
> Image get_director_cover_image(director_id)



Get cover image of a director

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
director_id = 789 # int | ID of the director to fetch

try: 
    api_response = api_instance.get_director_cover_image(director_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_director_cover_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **int**| ID of the director to fetch | 

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()

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

## **get_product_cover_image**
> Image get_product_cover_image(product_id)



Get cover image of a product

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
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

## **get_product_screenshots**
> list[Screenshot] get_product_screenshots(product_id)



Get product screenshots

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
product_id = 789 # int | ID of the product to fetch

try: 
    api_response = api_instance.get_product_screenshots(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_product_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 

### Return type

[**list[Screenshot]**](#Screenshot)

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
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

## **get_video_cover**
> Image get_video_cover(video_id)



Get video cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
video_id = 789 # int | ID of the video to fetch

try: 
    api_response = api_instance.get_video_cover(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_video_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_actor_cover**
> Image upload_actor_cover(actor_id, file, hash, hash_algorithm=hash_algorithm)



Upload actor cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
actor_id = 3.4 # float | Id of the actor
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_actor_cover(actor_id, file, hash, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_actor_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **float**| Id of the actor | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_category_banner**
> Image upload_category_banner(category_id, file, hash, hash_algorithm=hash_algorithm)



Upload category banner

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
category_id = 3.4 # float | Id of the category
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_category_banner(category_id, file, hash, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_category_banner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **float**| Id of the category | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_director_cover**
> Image upload_director_cover(director_id, file, hash, hash_algorithm=hash_algorithm)



Upload director cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
director_id = 3.4 # float | Id of the director
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_director_cover(director_id, file, hash, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_director_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **float**| Id of the director | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_product_cover**
> Image upload_product_cover(product_id, file, hash, hash_algorithm=hash_algorithm)



Upload product cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
product_id = 3.4 # float | Id of the product
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_product_cover(product_id, file, hash, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_product_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| Id of the product | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_product_screenshot**
> Screenshot upload_product_screenshot(product_id, image_id, position=position)



Upload product screenshot

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
product_id = 3.4 # float | Id of the product
image_id = 3.4 # float | Id of the product
position = 3.4 # float |  (optional)

try: 
    api_response = api_instance.upload_product_screenshot(product_id, image_id, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_product_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| Id of the product | 
 **image_id** | **float**| Id of the product | 
 **position** | **float**|  | [optional] 

### Return type

[**Screenshot**](#Screenshot)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_product_screenshots**
> list[Screenshot] upload_product_screenshots(product_id, file, hash, hash_algorithm=hash_algorithm, position=position)



Upload product screenshots

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
product_id = 3.4 # float | Id of the product
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)
position = 3.4 # float |  (optional)

try: 
    api_response = api_instance.upload_product_screenshots(product_id, file, hash, hash_algorithm=hash_algorithm, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_product_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| Id of the product | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 
 **position** | **float**|  | [optional] 

### Return type

[**list[Screenshot]**](#Screenshot)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **upload_subscription_cover**
> Image upload_subscription_cover(subscription_id, file, hash, hash_algorithm=hash_algorithm)



Upload subscription cover

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ImagesApi()
subscription_id = 3.4 # float | Id of the subscription
file = '/path/to/file.txt' # file | 
hash = 'hash_example' # str | 
hash_algorithm = 'hash_algorithm_example' # str | Hash algorithm to check the hash file (default value is: sha256) (optional)

try: 
    api_response = api_instance.upload_subscription_cover(subscription_id, file, hash, hash_algorithm=hash_algorithm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_subscription_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **float**| Id of the subscription | 
 **file** | **file**|  | 
 **hash** | **str**|  | 
 **hash_algorithm** | **str**| Hash algorithm to check the hash file (default value is: sha256) | [optional] 

### Return type

[**Image**](#Image)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

