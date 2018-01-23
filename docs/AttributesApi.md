# AttributesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_attribute**](#create_product_attribute) | **POST** /attributes | 
[**get_product_attributes**](#get_product_attributes) | **GET** /products/{product_id}/attributes | 
[**update_product_attribute**](#update_product_attribute) | **PUT** /attributes/{attribute_id} | 


## **create_product_attribute**
> ProductAttribute create_product_attribute(body)



Create new product attribute

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.AttributesApi()
body = kaemo_client.ProductAttributeCreateRequest() # ProductAttributeCreateRequest | 

try: 
    api_response = api_instance.create_product_attribute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->create_product_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAttributeCreateRequest**](#ProductAttributeCreateRequest)|  | 

### Return type

[**ProductAttribute**](#ProductAttribute)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_attributes**
> ProductAttributesResponse get_product_attributes(product_id, page=page, per_page=per_page)



Get product attributes. Important to add product to a cart. Allow to select if the customer will buy the product for download, streaming or both

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.AttributesApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_attributes(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_product_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ProductAttributesResponse**](#ProductAttributesResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_product_attribute**
> ProductAttribute update_product_attribute(attribute_id, body)



Update product attribute

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.AttributesApi()
attribute_id = 789 # int | Id of the attribute 
body = kaemo_client.ProductAttributeUpdateRequest() # ProductAttributeUpdateRequest | 

try: 
    api_response = api_instance.update_product_attribute(attribute_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->update_product_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **int**| Id of the attribute  | 
 **body** | [**ProductAttributeUpdateRequest**](#ProductAttributeUpdateRequest)|  | 

### Return type

[**ProductAttribute**](#ProductAttribute)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

