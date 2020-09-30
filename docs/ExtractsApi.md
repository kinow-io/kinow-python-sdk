# ExtractsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cover_to_extract**](#attach_cover_to_extract) | **POST** /extracts/{extract_id}/cover | 
[**attach_features_to_extract**](#attach_features_to_extract) | **POST** /extracts/{extract_id}/features | 
[**create_extract**](#create_extract) | **POST** /extracts | 
[**create_subtitle**](#create_subtitle) | **POST** /extracts/{extract_id}/subtitle | 
[**delete_extract**](#delete_extract) | **DELETE** /extracts/{extract_id} | 
[**get_extract**](#get_extract) | **GET** /extracts/{extract_id} | 
[**get_extract_features**](#get_extract_features) | **GET** /extracts/{extract_id}/features | 
[**get_extract_player**](#get_extract_player) | **GET** /extracts/{extract_id}/player | 
[**get_extracts**](#get_extracts) | **GET** /extracts | 
[**get_product_extracts**](#get_product_extracts) | **GET** /products/{product_id}/extracts | 
[**update_extract**](#update_extract) | **PUT** /extracts/{extract_id} | 


## **attach_cover_to_extract**
> attach_cover_to_extract(extract_id, id_image)



Attach cover to extract (the image need to be attached to the product)

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to fetch
id_image = 789 # int | Image ID to attach

try: 
    api_instance.attach_cover_to_extract(extract_id, id_image)
except ApiException as e:
    print("Exception when calling ExtractsApi->attach_cover_to_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to fetch | 
 **id_image** | **int**| Image ID to attach | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **attach_features_to_extract**
> attach_features_to_extract(extract_id, features)



Attach feature to extract

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | 
features = 'features_example' # str |       To attach existing FeatureValue to Product:      ```      [{      \"id_feature\":3,      \"id_feature_value\":5      }]      ```        To create a custom FeatureValue:      ```      [{      \"id_feature\":3,      \"custom_value\":[{      \"lang\": 1,      \"value\": \"string\"      }]      }]      ```

try: 
    api_instance.attach_features_to_extract(extract_id, features)
except ApiException as e:
    print("Exception when calling ExtractsApi->attach_features_to_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**|  | 
 **features** | **str**|       To attach existing FeatureValue to Product:      &#x60;&#x60;&#x60;      [{      \&quot;id_feature\&quot;:3,      \&quot;id_feature_value\&quot;:5      }]      &#x60;&#x60;&#x60;        To create a custom FeatureValue:      &#x60;&#x60;&#x60;      [{      \&quot;id_feature\&quot;:3,      \&quot;custom_value\&quot;:[{      \&quot;lang\&quot;: 1,      \&quot;value\&quot;: \&quot;string\&quot;      }]      }]      &#x60;&#x60;&#x60; | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_extract**
> Extract create_extract(body)



Create new extract

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
body = kinow_client.Extract() # Extract | 

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

## **create_subtitle**
> Subtitle create_subtitle(extract_id, body)



Create new Extract Subtitle

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to attach the created Subtitle
body = kinow_client.CreateExtractSubtitleRequest() # CreateExtractSubtitleRequest | Subtitle settings

try: 
    api_response = api_instance.create_subtitle(extract_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->create_subtitle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to attach the created Subtitle | 
 **body** | [**CreateExtractSubtitleRequest**](#CreateExtractSubtitleRequest)| Subtitle settings | 

### Return type

[**Subtitle**](#Subtitle)

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to update

try: 
    api_instance.delete_extract(extract_id)
except ApiException as e:
    print("Exception when calling ExtractsApi->delete_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to update | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_extract**
> Extract get_extract(extract_id)



Get extract

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to fetch

try: 
    api_response = api_instance.get_extract(extract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to fetch | 

### Return type

[**Extract**](#Extract)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_extract_features**
> Features get_extract_features(extract_id, page=page, per_page=per_page)



Get extract features

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_extract_features(extract_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_extract_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Features**](#Features)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_extract_player**
> Player get_extract_player(extract_id)



Get extract's player

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to fetch

try: 
    api_response = api_instance.get_extract_player(extract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_extract_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to fetch | 

### Return type

[**Player**](#Player)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_extracts**
> Videos1 get_extracts(page=page, per_page=per_page, features=features, filters=filters, ip=ip)



Get extracts list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
features = 'features_example' # str |       ```      features[*][value]=string&features[*][operator]=strict&features[1][value]=string&features[1][operator]=strict      _______________        {      \"*\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"1\": {      \"value\": \"string\",      \"operator\": \"contains\"      }      } ```      Operator can be: strict, contains, between, in, gt (greater than), lt (lower than).      To search on all features, you can pass * as featureId. (optional)
filters = 'filters_example' # str |       ```      name[value]=string&name[operator]=strict&duration[value]=string&duration[operator]=gt      _______________        {      \"name\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"duration\": {      \"value\": \"string\",      \"operator\": \"gt\"      }      } ```      Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)
ip = 'ip_example' # str | Filter by user IP (optional)

try: 
    api_response = api_instance.get_extracts(page=page, per_page=per_page, features=features, filters=filters, ip=ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_extracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **features** | **str**|       &#x60;&#x60;&#x60;      features[*][value]&#x3D;string&amp;features[*][operator]&#x3D;strict&amp;features[1][value]&#x3D;string&amp;features[1][operator]&#x3D;strict      _______________        {      \&quot;*\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;1\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      }      } &#x60;&#x60;&#x60;      Operator can be: strict, contains, between, in, gt (greater than), lt (lower than).      To search on all features, you can pass * as featureId. | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      name[value]&#x3D;string&amp;name[operator]&#x3D;strict&amp;duration[value]&#x3D;string&amp;duration[operator]&#x3D;gt      _______________        {      \&quot;name\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;duration\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;gt\&quot;      }      } &#x60;&#x60;&#x60;      Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 
 **ip** | **str**| Filter by user IP | [optional] 

### Return type

[**Videos1**](#Videos1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_extracts**
> Videos1 get_product_extracts(product_id, ip=ip, page=page, per_page=per_page)



Get extracts of a product

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
product_id = 789 # int | Product ID to fetch
ip = 'ip_example' # str | Filter by user IP (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_extracts(product_id, ip=ip, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_product_extracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
 **ip** | **str**| Filter by user IP | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Videos1**](#Videos1)

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ExtractsApi()
extract_id = 789 # int | Extract ID to fetch
body = kinow_client.Extract() # Extract | 

try: 
    api_response = api_instance.update_extract(extract_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->update_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to fetch | 
 **body** | [**Extract**](#Extract)|  | 

### Return type

[**Extract**](#Extract)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

