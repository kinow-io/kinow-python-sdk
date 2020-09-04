# PlaylistsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_playlist_bookmark**](#create_playlist_bookmark) | **POST** /playlists | 
[**delete_playlist_bookmark**](#delete_playlist_bookmark) | **DELETE** /playlists/{playlist_id} | 
[**get_customer_playlists**](#get_customer_playlists) | **GET** /customers/{customer_id}/playlists | 
[**get_playlist**](#get_playlist) | **GET** /playlists/{playlist_id} | 
[**update_playlist_bookmark**](#update_playlist_bookmark) | **PUT** /playlists/{playlist_id} | 


## **create_playlist_bookmark**
> PlaylistBookmark create_playlist_bookmark(customer_id, name)



Create playlist bookmark

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PlaylistsApi()
customer_id = 789 # int | 
name = 'name_example' # str | 

try: 
    api_response = api_instance.create_playlist_bookmark(customer_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->create_playlist_bookmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

[**PlaylistBookmark**](#PlaylistBookmark)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_playlist_bookmark**
> delete_playlist_bookmark(playlist_id)



Delete playlist bookmark

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PlaylistsApi()
playlist_id = 56 # int | 

try: 
    api_instance.delete_playlist_bookmark(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->delete_playlist_bookmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_playlists**
> Playlists get_customer_playlists(customer_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)



Get customer playlists

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PlaylistsApi()
customer_id = 789 # int | 
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_customer_playlists(customer_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_customer_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Playlists**](#Playlists)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_playlist**
> PlaylistBookmark get_playlist(playlist_id)



Get playlist

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PlaylistsApi()
playlist_id = 789 # int | Playlist ID to fetch

try: 
    api_response = api_instance.get_playlist(playlist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist ID to fetch | 

### Return type

[**PlaylistBookmark**](#PlaylistBookmark)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_playlist_bookmark**
> PlaylistBookmark update_playlist_bookmark(playlist_id, body)



Update playlist

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.PlaylistsApi()
playlist_id = 789 # int | Playlist ID to update
body = kinow_client.PlaylistBookmarkUpdate() # PlaylistBookmarkUpdate | Playlist settings

try: 
    api_response = api_instance.update_playlist_bookmark(playlist_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->update_playlist_bookmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist ID to update | 
 **body** | [**PlaylistBookmarkUpdate**](#PlaylistBookmarkUpdate)| Playlist settings | 

### Return type

[**PlaylistBookmark**](#PlaylistBookmark)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

