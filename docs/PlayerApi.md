# PlayerApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extract_player**](#get_extract_player) | **GET** /extracts/{extract_id}/player | 


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
api_instance = kaemo_client.PlayerApi()
extract_id = 789 # int | ID of the extract to fetch

try: 
    api_response = api_instance.get_extract_player(extract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_extract_player: %s\n" % e)
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

