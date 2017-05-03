# OAuthApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](#get_token) | **POST** /get-token | 


## **get_token**
> OAuthToken get_token(client_id, client_secret)



Get authentication token

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.OAuthApi()
client_id = 'client_id_example' # str | Client Id given by your back office
client_secret = 'client_secret_example' # str | Client secret given by your back office

try: 
    api_response = api_instance.get_token(client_id, client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client Id given by your back office | 
 **client_secret** | **str**| Client secret given by your back office | 

### Return type

[**OAuthToken**](#OAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

