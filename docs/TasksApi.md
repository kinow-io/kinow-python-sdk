# TasksApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](#create_task) | **POST** /tasks | 


## **create_task**
> Task create_task(body)



Create new task

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.TasksApi()
body = kinow_client.TaskCreateRequest() # TaskCreateRequest | Create task object

try: 
    api_response = api_instance.create_task(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskCreateRequest**](#TaskCreateRequest)| Create task object | 

### Return type

[**Task**](#Task)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

