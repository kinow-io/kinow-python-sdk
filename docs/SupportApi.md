# SupportApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message**](#create_message) | **POST** /support | 
[**get_contacts**](#get_contacts) | **GET** /support/contacts | 


## **create_message**
> Support create_message(id_lang, email, id_contact, message, id_product=id_product, id_order=id_order, send_mail=send_mail)



Create new message

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.SupportApi()
id_lang = 56 # int | 
email = 'email_example' # str | 
id_contact = 56 # int | 
message = 'message_example' # str | 
id_product = 56 # int |  (optional)
id_order = 56 # int |  (optional)
send_mail = true # bool |  (optional)

try: 
    api_response = api_instance.create_message(id_lang, email, id_contact, message, id_product=id_product, id_order=id_order, send_mail=send_mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportApi->create_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_lang** | **int**|  | 
 **email** | **str**|  | 
 **id_contact** | **int**|  | 
 **message** | **str**|  | 
 **id_product** | **int**|  | [optional] 
 **id_order** | **int**|  | [optional] 
 **send_mail** | **bool**|  | [optional] 

### Return type

[**Support**](#Support)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_contacts**
> Contacts get_contacts(page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get contacts list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.SupportApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_contacts(page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Contacts**](#Contacts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

