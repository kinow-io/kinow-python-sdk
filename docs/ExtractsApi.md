# ExtractsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extract**](#create_extract) | **POST** /extracts | 
[**delete_extract**](#delete_extract) | **DELETE** /extracts/{extract_id} | 
[**get_extract_player**](#get_extract_player) | **GET** /extracts/{extract_id}/player | 
[**get_product_extracts**](#get_product_extracts) | **GET** /products/{product_id}/extracts | 
[**update_extract**](#update_extract) | **PUT** /extracts/{extract_id} | 


## **create_extract**
> Extract create_extract(body)



Create new extract

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ExtractsApi()
body = kaemo_client.Extract() # Extract | 

try: 
    api_response = api_instance.create_extract(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->create_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Extract**](#Extract)|  | 

### Return type

[**Extract**](#Extract)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_extract**
> delete_extract(extract_id)



Delete extract

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ExtractsApi()
extract_id = 789 # int | ID of the video to update

try: 
    api_instance.delete_extract(extract_id)
except ApiException as e:
    print("Exception when calling ExtractsApi->delete_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| ID of the video to update | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_extract_player**
> PlayerConfiguration get_extract_player(extract_id)



Get extract's player

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ExtractsApi()
extract_id = 789 # int | ID of the extract to fetch

try: 
    api_response = api_instance.get_extract_player(extract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_extract_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| ID of the extract to fetch | 

### Return type

[**PlayerConfiguration**](#PlayerConfiguration)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_extracts**
> ProductExtractsResponse get_product_extracts(product_id, page=page, per_page=per_page)



Get extracts of a product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ExtractsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_extracts(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_product_extracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ProductExtractsResponse**](#ProductExtractsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_extract**
> Extract update_extract(extract_id, body)



Update extract

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ExtractsApi()
extract_id = 789 # int | ID of the video to update
body = kaemo_client.Extract() # Extract | 

try: 
    api_response = api_instance.update_extract(extract_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->update_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| ID of the video to update | 
 **body** | [**Extract**](#Extract)|  | 

### Return type

[**Extract**](#Extract)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

