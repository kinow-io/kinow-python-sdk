# kinow_client
Public api for Kinow back office

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.83
- Package version: 1.0.0
- Build date: 2019-05-21T09:37:11.377Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/kinow-io/kinow-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kinow-io/kinow-python-sdk.git`)

Then import the package:
```python
import kinow_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kinow_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = kinow_client.AccessesApi()
category_id = 789 # int | ID of the category to fetch
customer_id = 789 # int |  (optional)

try:
    api_response = api_instance.get_available_category(category_id, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessesApi->get_available_category: %s\n" % e)

```

## Enable Debug Logs
You can enable debug logging to get information about what is sent or received by the SDK.

When submitting a support request, it is best to provide the logs file for a faster resolution of your issue.

```python
# To be done before doing anything with the SDK
# Activate debug logs
kinow_client.configuration.debug = true

# (optionally) Set debug file location (no file is used by default)
kinow_client.configuration.logger_file = "path/to/logger/file"
```

## Documentation for API Endpoints

All URIs are relative to *https://api.kinow.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessesApi* | [**get_available_category**](docs/AccessesApi.md#get_available_category) | **GET** /categories-accesses/{category_id} | 
*AccessesApi* | [**get_customer_has_access_to_product**](docs/AccessesApi.md#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
*AccessesApi* | [**get_customer_has_access_to_video**](docs/AccessesApi.md#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
*AccessesApi* | [**get_product_availability**](docs/AccessesApi.md#get_product_availability) | **GET** /products/{product_id}/access | 
*ActorsApi* | [**create_actor**](docs/ActorsApi.md#create_actor) | **POST** /actors | 
*ActorsApi* | [**delete_actor**](docs/ActorsApi.md#delete_actor) | **DELETE** /actors/{actor_id} | 
*ActorsApi* | [**get_actor**](docs/ActorsApi.md#get_actor) | **GET** /actors/{actor_id} | 
*ActorsApi* | [**get_actors**](docs/ActorsApi.md#get_actors) | **GET** /actors | 
*ActorsApi* | [**get_product_actors**](docs/ActorsApi.md#get_product_actors) | **GET** /products/{product_id}/actors | 
*ActorsApi* | [**update_actor**](docs/ActorsApi.md#update_actor) | **PUT** /actors/{actor_id} | 
*AddressApi* | [**get_customer_address**](docs/AddressApi.md#get_customer_address) | **GET** /customers/{customer_id}/address | 
*AddressApi* | [**update_address**](docs/AddressApi.md#update_address) | **PUT** /addresses/{address_id} | 
*AttributesApi* | [**create_product_attribute**](docs/AttributesApi.md#create_product_attribute) | **POST** /attributes | 
*AttributesApi* | [**get_product_attributes**](docs/AttributesApi.md#get_product_attributes) | **GET** /products/{product_id}/attributes | 
*AttributesApi* | [**update_product_attribute**](docs/AttributesApi.md#update_product_attribute) | **PUT** /attributes/{attribute_id} | 
*BlogCategoriesApi* | [**get_blog_categories**](docs/BlogCategoriesApi.md#get_blog_categories) | **GET** /blog-categories | 
*BlogCategoriesApi* | [**get_blog_category**](docs/BlogCategoriesApi.md#get_blog_category) | **GET** /blog-categories/{blog_category_id} | 
*BlogPagesApi* | [**get_blog_page**](docs/BlogPagesApi.md#get_blog_page) | **GET** /blog-pages/{blog_page_id} | 
*BlogPagesApi* | [**get_blog_pages**](docs/BlogPagesApi.md#get_blog_pages) | **GET** /blog-pages | 
*BookmarksApi* | [**attach_bookmark_to_customer**](docs/BookmarksApi.md#attach_bookmark_to_customer) | **POST** /customers/{customer_id}/bookmarks | 
*BookmarksApi* | [**detach_bookmark_from_customer**](docs/BookmarksApi.md#detach_bookmark_from_customer) | **DELETE** /customers/{customer_id}/bookmarks/{product_id} | 
*BookmarksApi* | [**get_customer_bookmarks**](docs/BookmarksApi.md#get_customer_bookmarks) | **GET** /customers/{customer_id}/bookmarks | 
*CMSCategoriesApi* | [**create_cms_category**](docs/CMSCategoriesApi.md#create_cms_category) | **POST** /cms-categories | 
*CMSCategoriesApi* | [**get_cms_categories**](docs/CMSCategoriesApi.md#get_cms_categories) | **GET** /cms-categories | 
*CMSCategoriesApi* | [**update_cms_category**](docs/CMSCategoriesApi.md#update_cms_category) | **PUT** /cms-categories/{cms_category_id} | 
*CMSPagesApi* | [**create_cms_page**](docs/CMSPagesApi.md#create_cms_page) | **POST** /cms-pages | 
*CMSPagesApi* | [**get_cms_pages**](docs/CMSPagesApi.md#get_cms_pages) | **GET** /cms-pages | 
*CMSPagesApi* | [**update_cms_page**](docs/CMSPagesApi.md#update_cms_page) | **PUT** /cms-pages/{cms_page_id} | 
*CartRulesApi* | [**attach_cart_rule_to_cart**](docs/CartRulesApi.md#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
*CartRulesApi* | [**create_cart_rule**](docs/CartRulesApi.md#create_cart_rule) | **POST** /cart-rules | 
*CartRulesApi* | [**delete_cart_rule**](docs/CartRulesApi.md#delete_cart_rule) | **DELETE** /cart-rules/{cart_rule_id} | 
*CartRulesApi* | [**get_cart_rule**](docs/CartRulesApi.md#get_cart_rule) | **GET** /cart-rules/{cart_rule_id} | 
*CartRulesApi* | [**get_cart_rules**](docs/CartRulesApi.md#get_cart_rules) | **GET** /cart-rules | 
*CartRulesApi* | [**update_cart_rule**](docs/CartRulesApi.md#update_cart_rule) | **PUT** /cart-rules/{cart_rule_id} | 
*CartsApi* | [**add_product_to_cart**](docs/CartsApi.md#add_product_to_cart) | **POST** /carts/{cart_id}/products | 
*CartsApi* | [**attach_cart_rule_to_cart**](docs/CartsApi.md#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
*CartsApi* | [**attach_cart_to_customer**](docs/CartsApi.md#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
*CartsApi* | [**create_cart**](docs/CartsApi.md#create_cart) | **POST** /carts | 
*CartsApi* | [**delete_cart**](docs/CartsApi.md#delete_cart) | **DELETE** /carts/{cart_id} | 
*CartsApi* | [**delete_product_from_cart**](docs/CartsApi.md#delete_product_from_cart) | **DELETE** /carts/{cart_id}/products | 
*CartsApi* | [**get_cart**](docs/CartsApi.md#get_cart) | **GET** /carts/{cart_id} | 
*CartsApi* | [**get_customer_carts**](docs/CartsApi.md#get_customer_carts) | **GET** /customers/{customer_id}/carts | 
*CartsApi* | [**get_last_cart**](docs/CartsApi.md#get_last_cart) | **GET** /customers/{customer_id}/last-cart | 
*CartsApi* | [**get_payment_url**](docs/CartsApi.md#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
*CartsApi* | [**update_cart**](docs/CartsApi.md#update_cart) | **PUT** /carts/{cart_id} | 
*CartsApi* | [**validate_cart**](docs/CartsApi.md#validate_cart) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 
*CartsApi* | [**validate_free_order**](docs/CartsApi.md#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
*CategoriesApi* | [**create_category**](docs/CategoriesApi.md#create_category) | **POST** /categories | 
*CategoriesApi* | [**get_available_category**](docs/CategoriesApi.md#get_available_category) | **GET** /categories-accesses/{category_id} | 
*CategoriesApi* | [**get_categories**](docs/CategoriesApi.md#get_categories) | **GET** /categories | 
*CategoriesApi* | [**get_categories_from_category**](docs/CategoriesApi.md#get_categories_from_category) | **GET** /categories/{category_id}/categories | 
*CategoriesApi* | [**get_category**](docs/CategoriesApi.md#get_category) | **GET** /categories/{category_id} | 
*CategoriesApi* | [**get_category_banner**](docs/CategoriesApi.md#get_category_banner) | **GET** /categories/{category_id}/banner | 
*CategoriesApi* | [**get_category_features**](docs/CategoriesApi.md#get_category_features) | **GET** /categories/{category_id}/features | 
*CategoriesApi* | [**get_category_products**](docs/CategoriesApi.md#get_category_products) | **GET** /categories/{category_id}/products | 
*CategoriesApi* | [**get_product_categories**](docs/CategoriesApi.md#get_product_categories) | **GET** /products/{product_id}/categories | 
*CategoriesApi* | [**get_subscription_categories**](docs/CategoriesApi.md#get_subscription_categories) | **GET** /subscriptions/{subscription_id}/categories | 
*CountriesApi* | [**get_countries**](docs/CountriesApi.md#get_countries) | **GET** /countries | 
*CurrenciesApi* | [**get_currencies**](docs/CurrenciesApi.md#get_currencies) | **GET** /currencies | 
*CustomerThreadsApi* | [**get_customer_thread**](docs/CustomerThreadsApi.md#get_customer_thread) | **GET** /customer-threads/{customer_thread_id} | 
*CustomerThreadsApi* | [**get_customer_threads**](docs/CustomerThreadsApi.md#get_customer_threads) | **GET** /customer-threads | 
*CustomersApi* | [**attach_cart_to_customer**](docs/CustomersApi.md#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
*CustomersApi* | [**check_customer_credentials**](docs/CustomersApi.md#check_customer_credentials) | **POST** /customers/check-credentials | 
*CustomersApi* | [**create_customer**](docs/CustomersApi.md#create_customer) | **POST** /customers | 
*CustomersApi* | [**create_facebook_id**](docs/CustomersApi.md#create_facebook_id) | **POST** /customers/facebook | 
*CustomersApi* | [**delete_customer**](docs/CustomersApi.md#delete_customer) | **DELETE** /customers/{customer_id} | 
*CustomersApi* | [**generate_authentication_token**](docs/CustomersApi.md#generate_authentication_token) | **GET** /customers/{customer_id}/authentication-token | 
*CustomersApi* | [**get_customer**](docs/CustomersApi.md#get_customer) | **GET** /customers/{customer_id} | 
*CustomersApi* | [**get_customer_accesses_subscriptions**](docs/CustomersApi.md#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
*CustomersApi* | [**get_customer_accesses_videos**](docs/CustomersApi.md#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
*CustomersApi* | [**get_customer_address**](docs/CustomersApi.md#get_customer_address) | **GET** /customers/{customer_id}/address | 
*CustomersApi* | [**get_customer_can_see_product**](docs/CustomersApi.md#get_customer_can_see_product) | **GET** /customers/{customer_id}/products/{product_id}/can-see | 
*CustomersApi* | [**get_customer_current_views**](docs/CustomersApi.md#get_customer_current_views) | **GET** /customers/{customer_id}/current-views | 
*CustomersApi* | [**get_customer_groups**](docs/CustomersApi.md#get_customer_groups) | **GET** /customers/{customer_id}/groups | 
*CustomersApi* | [**get_customer_has_access_to_product**](docs/CustomersApi.md#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
*CustomersApi* | [**get_customer_has_access_to_video**](docs/CustomersApi.md#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
*CustomersApi* | [**get_customer_orders**](docs/CustomersApi.md#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
*CustomersApi* | [**get_customers**](docs/CustomersApi.md#get_customers) | **GET** /customers | 
*CustomersApi* | [**get_facebook_customer**](docs/CustomersApi.md#get_facebook_customer) | **GET** /customers/facebook/{facebook_id} | 
*CustomersApi* | [**get_payment_customer_id**](docs/CustomersApi.md#get_payment_customer_id) | **GET** /customers/{customer_id}/payments/{payment_name}/customer | 
*CustomersApi* | [**update_customer**](docs/CustomersApi.md#update_customer) | **PUT** /customers/{customer_id} | 
*DirectorsApi* | [**create_director**](docs/DirectorsApi.md#create_director) | **POST** /directors | 
*DirectorsApi* | [**delete_director**](docs/DirectorsApi.md#delete_director) | **DELETE** /directors/{director_id} | 
*DirectorsApi* | [**get_director**](docs/DirectorsApi.md#get_director) | **GET** /directors/{director_id} | 
*DirectorsApi* | [**get_directors**](docs/DirectorsApi.md#get_directors) | **GET** /directors | 
*DirectorsApi* | [**get_product_directors**](docs/DirectorsApi.md#get_product_directors) | **GET** /products/{product_id}/directors | 
*DirectorsApi* | [**update_director**](docs/DirectorsApi.md#update_director) | **PUT** /directors/{director_id} | 
*ExtractsApi* | [**attach_cover_to_extract**](docs/ExtractsApi.md#attach_cover_to_extract) | **POST** /extracts/{extract_id}/cover | 
*ExtractsApi* | [**create_extract**](docs/ExtractsApi.md#create_extract) | **POST** /extracts | 
*ExtractsApi* | [**delete_extract**](docs/ExtractsApi.md#delete_extract) | **DELETE** /extracts/{extract_id} | 
*ExtractsApi* | [**get_extract_player**](docs/ExtractsApi.md#get_extract_player) | **GET** /extracts/{extract_id}/player | 
*ExtractsApi* | [**get_product_extracts**](docs/ExtractsApi.md#get_product_extracts) | **GET** /products/{product_id}/extracts | 
*ExtractsApi* | [**update_extract**](docs/ExtractsApi.md#update_extract) | **PUT** /extracts/{extract_id} | 
*FeatureValuesApi* | [**attach_features_to_product**](docs/FeatureValuesApi.md#attach_features_to_product) | **POST** /products/{product_id}/features | 
*FeatureValuesApi* | [**attach_features_to_video**](docs/FeatureValuesApi.md#attach_features_to_video) | **POST** /videos/{video_id}/features | 
*FeatureValuesApi* | [**detach_feature_to_product**](docs/FeatureValuesApi.md#detach_feature_to_product) | **DELETE** products/{product_id}/features/{feature_id} | 
*FeatureValuesApi* | [**get_feature_values**](docs/FeatureValuesApi.md#get_feature_values) | **GET** /feature-values | 
*FeaturesApi* | [**attach_features_to_product**](docs/FeaturesApi.md#attach_features_to_product) | **POST** /products/{product_id}/features | 
*FeaturesApi* | [**attach_features_to_video**](docs/FeaturesApi.md#attach_features_to_video) | **POST** /videos/{video_id}/features | 
*FeaturesApi* | [**detach_feature_to_product**](docs/FeaturesApi.md#detach_feature_to_product) | **DELETE** products/{product_id}/features/{feature_id} | 
*FeaturesApi* | [**get_category_features**](docs/FeaturesApi.md#get_category_features) | **GET** /categories/{category_id}/features | 
*FeaturesApi* | [**get_feature_values**](docs/FeaturesApi.md#get_feature_values) | **GET** /feature-values | 
*FeaturesApi* | [**get_features**](docs/FeaturesApi.md#get_features) | **GET** /features | 
*FeaturesApi* | [**get_product_features**](docs/FeaturesApi.md#get_product_features) | **GET** /products/{product_id}/features | 
*FeaturesApi* | [**get_video_features**](docs/FeaturesApi.md#get_video_features) | **GET** /videos/{video_id}/features | 
*GendersApi* | [**get_genders**](docs/GendersApi.md#get_genders) | **GET** /genders | 
*GeolocationsApi* | [**geolocations**](docs/GeolocationsApi.md#geolocations) | **POST** /geolocations | 
*GeolocationsApi* | [**get_product_geolocations**](docs/GeolocationsApi.md#get_product_geolocations) | **GET** /products/{product_id}/geolocations | 
*GeolocationsApi* | [**get_product_geolocations_by_ip**](docs/GeolocationsApi.md#get_product_geolocations_by_ip) | **POST** /products/{product_id}/geolocations | 
*GeolocationsApi* | [**get_video_geolocation**](docs/GeolocationsApi.md#get_video_geolocation) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
*GeolocationsApi* | [**set_product_geolocation**](docs/GeolocationsApi.md#set_product_geolocation) | **PUT** /products/{product_id}/geolocations | 
*GeolocationsApi* | [**set_video_geolocation**](docs/GeolocationsApi.md#set_video_geolocation) | **PUT** /videos/{video_id}/geolocations | 
*GroupsApi* | [**attach_customer_to_group**](docs/GroupsApi.md#attach_customer_to_group) | **POST** /groups/{group_id}/customers | 
*GroupsApi* | [**detach_customer_from_group**](docs/GroupsApi.md#detach_customer_from_group) | **DELETE** /groups/{group_id}/customers/{customer_id} | 
*GroupsApi* | [**get_group**](docs/GroupsApi.md#get_group) | **GET** /groups/{group_id} | 
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /groups | 
*GroupsApi* | [**get_product_groups**](docs/GroupsApi.md#get_product_groups) | **GET** /products/{product_id}/groups | 
*ImagesApi* | [**get_actor_cover_image**](docs/ImagesApi.md#get_actor_cover_image) | **GET** /actors/{actor_id}/cover | 
*ImagesApi* | [**get_category_banner**](docs/ImagesApi.md#get_category_banner) | **GET** /categories/{category_id}/banner | 
*ImagesApi* | [**get_director_cover_image**](docs/ImagesApi.md#get_director_cover_image) | **GET** /directors/{director_id}/cover | 
*ImagesApi* | [**get_intro_image**](docs/ImagesApi.md#get_intro_image) | **GET** /widgets/intro/images | 
*ImagesApi* | [**get_product_cover_image**](docs/ImagesApi.md#get_product_cover_image) | **GET** /products/{product_id}/cover | 
*ImagesApi* | [**get_product_images**](docs/ImagesApi.md#get_product_images) | **GET** /products/{product_id}/images | 
*ImagesApi* | [**get_product_screenshots**](docs/ImagesApi.md#get_product_screenshots) | **GET** /products/{product_id}/screenshots | 
*ImagesApi* | [**get_subscription_cover_image**](docs/ImagesApi.md#get_subscription_cover_image) | **GET** /subscriptions/{subscription_id}/cover | 
*ImagesApi* | [**get_video_cover**](docs/ImagesApi.md#get_video_cover) | **GET** /videos/{video_id}/cover | 
*ImagesApi* | [**upload_actor_cover**](docs/ImagesApi.md#upload_actor_cover) | **POST** /actors/{actor_id}/cover | 
*ImagesApi* | [**upload_category_banner**](docs/ImagesApi.md#upload_category_banner) | **POST** /category/{category_id}/banner | 
*ImagesApi* | [**upload_director_cover**](docs/ImagesApi.md#upload_director_cover) | **POST** /directors/{director_id}/cover | 
*ImagesApi* | [**upload_product_cover**](docs/ImagesApi.md#upload_product_cover) | **POST** /products/{product_id}/cover | 
*ImagesApi* | [**upload_product_screenshot**](docs/ImagesApi.md#upload_product_screenshot) | **PUT** /products/{product_id}/screenshots/{image_id} | 
*ImagesApi* | [**upload_product_screenshot_0**](docs/ImagesApi.md#upload_product_screenshot_0) | **DELETE** /products/{product_id}/screenshots/{image_id} | 
*ImagesApi* | [**upload_product_screenshots**](docs/ImagesApi.md#upload_product_screenshots) | **POST** /products/{product_id}/screenshots | 
*ImagesApi* | [**upload_subscription_cover**](docs/ImagesApi.md#upload_subscription_cover) | **POST** /subscriptions/{subscription_id}/cover | 
*LanguagesApi* | [**get_languages**](docs/LanguagesApi.md#get_languages) | **GET** /languages | 
*MediaFilesApi* | [**get_media_source_files**](docs/MediaFilesApi.md#get_media_source_files) | **GET** /media-sources/{source_id}/files | 
*MediaFilesApi* | [**post_media_source_files**](docs/MediaFilesApi.md#post_media_source_files) | **POST** /media-sources/{source_id}/files | 
*MediaSourcesApi* | [**get_media_source**](docs/MediaSourcesApi.md#get_media_source) | **GET** /media-sources/{source_id} | 
*MediaSourcesApi* | [**get_media_source_files**](docs/MediaSourcesApi.md#get_media_source_files) | **GET** /media-sources/{source_id}/files | 
*MediaSourcesApi* | [**get_media_sources**](docs/MediaSourcesApi.md#get_media_sources) | **GET** /media-sources | 
*MediaSourcesApi* | [**post_media_source_files**](docs/MediaSourcesApi.md#post_media_source_files) | **POST** /media-sources/{source_id}/files | 
*OAuthApi* | [**get_token**](docs/OAuthApi.md#get_token) | **POST** /get-token | 
*OrderHistoriesApi* | [**get_order_histories**](docs/OrderHistoriesApi.md#get_order_histories) | **GET** /orders/{order_id}/histories | 
*OrderStatesApi* | [**get_order_state**](docs/OrderStatesApi.md#get_order_state) | **GET** /order-states/{order_state_id} | 
*OrderStatesApi* | [**get_order_states**](docs/OrderStatesApi.md#get_order_states) | **GET** /order-states | 
*OrdersApi* | [**get_customer_orders**](docs/OrdersApi.md#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
*OrdersApi* | [**get_order**](docs/OrdersApi.md#get_order) | **GET** /orders/{order_id} | 
*OrdersApi* | [**get_order_histories**](docs/OrdersApi.md#get_order_histories) | **GET** /orders/{order_id}/histories | 
*OrdersApi* | [**get_order_invoice**](docs/OrdersApi.md#get_order_invoice) | **GET** /orders/{order_id}/invoice | 
*OrdersApi* | [**get_orders**](docs/OrdersApi.md#get_orders) | **GET** /orders | 
*PaymentModulesApi* | [**get_payment_modules**](docs/PaymentModulesApi.md#get_payment_modules) | **GET** /payment-modules | 
*PaymentModulesApi* | [**get_payment_url**](docs/PaymentModulesApi.md#get_payment_url) | **GET** /carts/{cart_id}/payments/{payment_name} | 
*PaymentModulesApi* | [**validate_cart**](docs/PaymentModulesApi.md#validate_cart) | **POST** /carts/{cart_id}/payments/{payment_name}/validate | 
*PaymentModulesApi* | [**validate_free_order**](docs/PaymentModulesApi.md#validate_free_order) | **POST** /carts/{cart_id}/validate-free-order | 
*ProductAccessesApi* | [**create_product_access**](docs/ProductAccessesApi.md#create_product_access) | **POST** /product-accesses | 
*ProductAccessesApi* | [**delete_product_access**](docs/ProductAccessesApi.md#delete_product_access) | **DELETE** /product-accesses/{product_access_id} | 
*ProductAccessesApi* | [**get_customer_accesses_subscriptions**](docs/ProductAccessesApi.md#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
*ProductAccessesApi* | [**get_customer_accesses_videos**](docs/ProductAccessesApi.md#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
*ProductAccessesApi* | [**get_product_access**](docs/ProductAccessesApi.md#get_product_access) | **GET** /product-accesses/{product_access_id} | 
*ProductAccessesApi* | [**get_product_accesses**](docs/ProductAccessesApi.md#get_product_accesses) | **GET** /product-accesses | 
*ProductAccessesApi* | [**stop_subscription**](docs/ProductAccessesApi.md#stop_subscription) | **PUT** /customers/{customer_id}/unsubscribe | 
*ProductAccessesApi* | [**update_product_access**](docs/ProductAccessesApi.md#update_product_access) | **PUT** /product-accesses/{product_access_id} | 
*ProductsApi* | [**attach_features_to_product**](docs/ProductsApi.md#attach_features_to_product) | **POST** /products/{product_id}/features | 
*ProductsApi* | [**attach_product_to_actor**](docs/ProductsApi.md#attach_product_to_actor) | **POST** /products/{product_id}/actors | 
*ProductsApi* | [**attach_product_to_category**](docs/ProductsApi.md#attach_product_to_category) | **POST** /products/{product_id}/categories | 
*ProductsApi* | [**attach_product_to_director**](docs/ProductsApi.md#attach_product_to_director) | **POST** /products/{product_id}/directors | 
*ProductsApi* | [**attach_product_to_director_0**](docs/ProductsApi.md#attach_product_to_director_0) | **POST** /products/{product_id}/groups | 
*ProductsApi* | [**attach_video_to_product**](docs/ProductsApi.md#attach_video_to_product) | **POST** /products/{product_id}/videos | 
*ProductsApi* | [**create_product**](docs/ProductsApi.md#create_product) | **POST** /products | 
*ProductsApi* | [**delete_product**](docs/ProductsApi.md#delete_product) | **DELETE** /products/{product_id} | 
*ProductsApi* | [**detach_feature_to_product**](docs/ProductsApi.md#detach_feature_to_product) | **DELETE** products/{product_id}/features/{feature_id} | 
*ProductsApi* | [**detach_product_from_actor**](docs/ProductsApi.md#detach_product_from_actor) | **DELETE** /products/{product_id}/actors/{actor_id} | 
*ProductsApi* | [**detach_product_from_category**](docs/ProductsApi.md#detach_product_from_category) | **DELETE** /products/{product_id}/categories/{category_id} | 
*ProductsApi* | [**detach_product_from_director**](docs/ProductsApi.md#detach_product_from_director) | **DELETE** /products/{product_id}/directors/{director_id} | 
*ProductsApi* | [**detach_product_from_group**](docs/ProductsApi.md#detach_product_from_group) | **POST** /products/{product_id}/groups/{group_id} | 
*ProductsApi* | [**get_category_products**](docs/ProductsApi.md#get_category_products) | **GET** /categories/{category_id}/products | 
*ProductsApi* | [**get_customer_has_access_to_product**](docs/ProductsApi.md#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
*ProductsApi* | [**get_product**](docs/ProductsApi.md#get_product) | **GET** /products/{product_id} | 
*ProductsApi* | [**get_product_actors**](docs/ProductsApi.md#get_product_actors) | **GET** /products/{product_id}/actors | 
*ProductsApi* | [**get_product_attributes**](docs/ProductsApi.md#get_product_attributes) | **GET** /products/{product_id}/attributes | 
*ProductsApi* | [**get_product_availability**](docs/ProductsApi.md#get_product_availability) | **GET** /products/{product_id}/access | 
*ProductsApi* | [**get_product_categories**](docs/ProductsApi.md#get_product_categories) | **GET** /products/{product_id}/categories | 
*ProductsApi* | [**get_product_cover_image**](docs/ProductsApi.md#get_product_cover_image) | **GET** /products/{product_id}/cover | 
*ProductsApi* | [**get_product_directors**](docs/ProductsApi.md#get_product_directors) | **GET** /products/{product_id}/directors | 
*ProductsApi* | [**get_product_extracts**](docs/ProductsApi.md#get_product_extracts) | **GET** /products/{product_id}/extracts | 
*ProductsApi* | [**get_product_features**](docs/ProductsApi.md#get_product_features) | **GET** /products/{product_id}/features | 
*ProductsApi* | [**get_product_geolocations**](docs/ProductsApi.md#get_product_geolocations) | **GET** /products/{product_id}/geolocations | 
*ProductsApi* | [**get_product_geolocations_by_ip**](docs/ProductsApi.md#get_product_geolocations_by_ip) | **POST** /products/{product_id}/geolocations | 
*ProductsApi* | [**get_product_images**](docs/ProductsApi.md#get_product_images) | **GET** /products/{product_id}/images | 
*ProductsApi* | [**get_products**](docs/ProductsApi.md#get_products) | **GET** /products | 
*ProductsApi* | [**get_products_from_product**](docs/ProductsApi.md#get_products_from_product) | **GET** /products/{product_id}/products | 
*ProductsApi* | [**get_videos_from_product**](docs/ProductsApi.md#get_videos_from_product) | **GET** /products/{product_id}/videos | 
*ProductsApi* | [**search_products**](docs/ProductsApi.md#search_products) | **GET** /products/search/{search_query} | 
*ProductsApi* | [**set_product_geolocation**](docs/ProductsApi.md#set_product_geolocation) | **PUT** /products/{product_id}/geolocations | 
*ProductsApi* | [**update_product**](docs/ProductsApi.md#update_product) | **PUT** /products/{product_id} | 
*StatsApi* | [**get_customer_group_total_watched**](docs/StatsApi.md#get_customer_group_total_watched) | **GET** /video-stats/customer-group | 
*StatsApi* | [**get_customer_sessions**](docs/StatsApi.md#get_customer_sessions) | **GET** /video-stats/sessions | 
*StatsApi* | [**get_customer_video_stats**](docs/StatsApi.md#get_customer_video_stats) | **GET** /video-stats/customers | 
*StatsApi* | [**get_video_stats**](docs/StatsApi.md#get_video_stats) | **GET** /video-stats/videos | 
*SubscriptionsApi* | [**get_disabled_subscriptions**](docs/SubscriptionsApi.md#get_disabled_subscriptions) | **GET** /videos/{video_id}/disabled-subscriptions | 
*SubscriptionsApi* | [**get_subscription**](docs/SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subscription_id} | 
*SubscriptionsApi* | [**get_subscription_categories**](docs/SubscriptionsApi.md#get_subscription_categories) | **GET** /subscriptions/{subscription_id}/categories | 
*SubscriptionsApi* | [**get_subscription_cover_image**](docs/SubscriptionsApi.md#get_subscription_cover_image) | **GET** /subscriptions/{subscription_id}/cover | 
*SubscriptionsApi* | [**get_subscriptions**](docs/SubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | 
*TasksApi* | [**create_task**](docs/TasksApi.md#create_task) | **POST** /tasks | 
*VideosApi* | [**attach_cover_to_video**](docs/VideosApi.md#attach_cover_to_video) | **POST** /videos/{video_id}/cover | 
*VideosApi* | [**attach_features_to_video**](docs/VideosApi.md#attach_features_to_video) | **POST** /videos/{video_id}/features | 
*VideosApi* | [**attach_video_to_product**](docs/VideosApi.md#attach_video_to_product) | **POST** /products/{product_id}/videos | 
*VideosApi* | [**create_video**](docs/VideosApi.md#create_video) | **POST** /videos | 
*VideosApi* | [**delete_video**](docs/VideosApi.md#delete_video) | **DELETE** /videos/{video_id} | 
*VideosApi* | [**get_customer_has_access_to_video**](docs/VideosApi.md#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
*VideosApi* | [**get_disabled_subscriptions**](docs/VideosApi.md#get_disabled_subscriptions) | **GET** /videos/{video_id}/disabled-subscriptions | 
*VideosApi* | [**get_video**](docs/VideosApi.md#get_video) | **GET** /videos/{video_id} | 
*VideosApi* | [**get_video_access**](docs/VideosApi.md#get_video_access) | **GET** /videos/{video_id}/customers/{customer_id}/access | 
*VideosApi* | [**get_video_download_url**](docs/VideosApi.md#get_video_download_url) | **GET** /videos/{video_id}/download-url | 
*VideosApi* | [**get_video_features**](docs/VideosApi.md#get_video_features) | **GET** /videos/{video_id}/features | 
*VideosApi* | [**get_video_geolocation**](docs/VideosApi.md#get_video_geolocation) | **GET** /videos/{video_id}/geolocation | 
*VideosApi* | [**get_video_geolocation_0**](docs/VideosApi.md#get_video_geolocation_0) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
*VideosApi* | [**get_video_player**](docs/VideosApi.md#get_video_player) | **GET** /videos/{video_id}/player | 
*VideosApi* | [**get_video_subtitles**](docs/VideosApi.md#get_video_subtitles) | **GET** /videos/{video_id}/subtitles | 
*VideosApi* | [**get_video_views**](docs/VideosApi.md#get_video_views) | **GET** /videos/{video_id}/views | 
*VideosApi* | [**get_videos**](docs/VideosApi.md#get_videos) | **GET** /videos | 
*VideosApi* | [**get_videos_from_product**](docs/VideosApi.md#get_videos_from_product) | **GET** /products/{product_id}/videos | 
*VideosApi* | [**set_video_geolocation**](docs/VideosApi.md#set_video_geolocation) | **PUT** /videos/{video_id}/geolocations | 
*VideosApi* | [**update_video**](docs/VideosApi.md#update_video) | **PUT** /videos/{video_id} | 
*WidgetsApi* | [**get_intro_image**](docs/WidgetsApi.md#get_intro_image) | **GET** /widgets/intro/images | 
*WidgetsApi* | [**get_widget_footer_menu**](docs/WidgetsApi.md#get_widget_footer_menu) | **GET** /widgets/footer-menu | 
*WidgetsApi* | [**get_widget_slider**](docs/WidgetsApi.md#get_widget_slider) | **GET** /widgets/slider | 
*WidgetsApi* | [**get_widget_slider_item**](docs/WidgetsApi.md#get_widget_slider_item) | **GET** /widgets/slider/{slider_id} | 
*WidgetsApi* | [**get_widget_top_menu**](docs/WidgetsApi.md#get_widget_top_menu) | **GET** /widgets/top-menu | 


## Documentation For Models

 - [Actor](docs/Actor.md)
 - [Actors](docs/Actors.md)
 - [Address](docs/Address.md)
 - [BlogCategory](docs/BlogCategory.md)
 - [BlogCategoryLists](docs/BlogCategoryLists.md)
 - [BlogPage](docs/BlogPage.md)
 - [BlogPageLists](docs/BlogPageLists.md)
 - [CMSCategoriesLists](docs/CMSCategoriesLists.md)
 - [CMSCategory](docs/CMSCategory.md)
 - [CMSPage](docs/CMSPage.md)
 - [CMSPageLists](docs/CMSPageLists.md)
 - [Cart](docs/Cart.md)
 - [CartBody](docs/CartBody.md)
 - [CartRule](docs/CartRule.md)
 - [CartRuleRestrictionGroup](docs/CartRuleRestrictionGroup.md)
 - [CartRuleRestrictionGroupItem](docs/CartRuleRestrictionGroupItem.md)
 - [CartRules](docs/CartRules.md)
 - [Carts](docs/Carts.md)
 - [Categories](docs/Categories.md)
 - [Category](docs/Category.md)
 - [CategoryImages](docs/CategoryImages.md)
 - [Countries](docs/Countries.md)
 - [Country](docs/Country.md)
 - [Currencies](docs/Currencies.md)
 - [Currency](docs/Currency.md)
 - [Customer](docs/Customer.md)
 - [CustomerCreateRequest](docs/CustomerCreateRequest.md)
 - [CustomerCurrentViews](docs/CustomerCurrentViews.md)
 - [CustomerGroupVideoStats](docs/CustomerGroupVideoStats.md)
 - [CustomerGroupVideoStats1](docs/CustomerGroupVideoStats1.md)
 - [CustomerId](docs/CustomerId.md)
 - [CustomerThread](docs/CustomerThread.md)
 - [CustomerThread1](docs/CustomerThread1.md)
 - [CustomerVideoStats](docs/CustomerVideoStats.md)
 - [CustomerVideoStats1](docs/CustomerVideoStats1.md)
 - [Customers](docs/Customers.md)
 - [Director](docs/Director.md)
 - [Director1](docs/Director1.md)
 - [DownloadUrl](docs/DownloadUrl.md)
 - [Extract](docs/Extract.md)
 - [Feature](docs/Feature.md)
 - [FeatureValue](docs/FeatureValue.md)
 - [Features](docs/Features.md)
 - [Gender](docs/Gender.md)
 - [Genders](docs/Genders.md)
 - [Geoloc](docs/Geoloc.md)
 - [Geolocs](docs/Geolocs.md)
 - [Group](docs/Group.md)
 - [Groups](docs/Groups.md)
 - [I18nField](docs/I18nField.md)
 - [Image](docs/Image.md)
 - [Language](docs/Language.md)
 - [Languages](docs/Languages.md)
 - [MediaFile](docs/MediaFile.md)
 - [MediaFiles](docs/MediaFiles.md)
 - [MediaSource](docs/MediaSource.md)
 - [MediaSources](docs/MediaSources.md)
 - [OAuthToken](docs/OAuthToken.md)
 - [Order](docs/Order.md)
 - [OrderHistories](docs/OrderHistories.md)
 - [OrderHistory](docs/OrderHistory.md)
 - [OrderState](docs/OrderState.md)
 - [OrderStates](docs/OrderStates.md)
 - [Orders](docs/Orders.md)
 - [Pagination](docs/Pagination.md)
 - [PaymentArguments](docs/PaymentArguments.md)
 - [PaymentModule](docs/PaymentModule.md)
 - [PaymentModules](docs/PaymentModules.md)
 - [PaymentUrl](docs/PaymentUrl.md)
 - [PlayerConfiguration](docs/PlayerConfiguration.md)
 - [Product](docs/Product.md)
 - [ProductAccess](docs/ProductAccess.md)
 - [ProductAttribute](docs/ProductAttribute.md)
 - [ProductAttributeCreateRequest](docs/ProductAttributeCreateRequest.md)
 - [ProductAttributeUpdateRequest](docs/ProductAttributeUpdateRequest.md)
 - [ProductAttributesResponse](docs/ProductAttributesResponse.md)
 - [ProductExtractsResponse](docs/ProductExtractsResponse.md)
 - [ProductImagesResponse](docs/ProductImagesResponse.md)
 - [Products](docs/Products.md)
 - [Products1](docs/Products1.md)
 - [Screenshot](docs/Screenshot.md)
 - [SessionVideoStat](docs/SessionVideoStat.md)
 - [SessionVideoStats](docs/SessionVideoStats.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionAccesses](docs/SubscriptionAccesses.md)
 - [Subscriptions](docs/Subscriptions.md)
 - [Subtitle](docs/Subtitle.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [TaskCreateRequest](docs/TaskCreateRequest.md)
 - [TaskFactory](docs/TaskFactory.md)
 - [Video](docs/Video.md)
 - [VideoFreeAccess](docs/VideoFreeAccess.md)
 - [VideoStat](docs/VideoStat.md)
 - [VideoStats](docs/VideoStats.md)
 - [VideoSubtitlesResponse](docs/VideoSubtitlesResponse.md)
 - [VideoViews](docs/VideoViews.md)
 - [Videos](docs/Videos.md)
 - [WidgetFooterMenu](docs/WidgetFooterMenu.md)
 - [WidgetFooterMenus](docs/WidgetFooterMenus.md)
 - [WidgetSlider](docs/WidgetSlider.md)
 - [WidgetSliders](docs/WidgetSliders.md)
 - [WidgetTopMenu](docs/WidgetTopMenu.md)
 - [WidgetTopMenus](docs/WidgetTopMenus.md)

