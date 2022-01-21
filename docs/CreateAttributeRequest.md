## CreateAttributeRequest

### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product ID to attach this access | [optional] 
**video_group_id** | **int** | Video Group ID to restrict this access | [optional] 
**video_id** | **int** | Video ID to restrict this access | [optional] 
**type** | **str** | RENT, BUY or SUBSCRIPTION | [optional] 
**mode** | **str** | BOTH (Streaming &amp; Download), STREAMING or DOWNLOAD | [optional] 
**quality** | **str** | ALL, HD or SD | [optional] 
**price** | **float** | Retail price to sell this access | [optional] 
**price_mode** | **int** | Pre-tax price (0) or price with tax (1) | [optional] 
**duration** | **int** | Duration in days while user can access videos | [optional] 
**watching_duration** | **int** | Duration in days while user can watch video after first play | [optional] 
**maximum_views** | **int** | Maximum views a user can watch video | [optional] 

[[Back to Model list]](#documentation-for-models) [[Back to API list]](#documentation-for-api-endpoints)


