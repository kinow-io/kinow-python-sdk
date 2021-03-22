# ManufacturersApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manufacturer_cover_image**](#get_manufacturer_cover_image) | **GET** /manufacturers/{manufacturer_id}/cover | 


## **get_manufacturer_cover_image**
> Image get_manufacturer_cover_image(manufacturer_id)



Please, use __/directors/{actor_id}/cover__

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ManufacturersApi()
manufacturer_id = 789 # int | ID of the manufacturer to fetch

try: 
    api_response = api_instance.get_manufacturer_cover_image(manufacturer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManufacturersApi->get_manufacturer_cover_image: %s\n" % e)
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

