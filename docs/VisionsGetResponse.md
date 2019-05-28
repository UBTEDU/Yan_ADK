# VisionsGetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Return code, 0 means success | 
**type** | **str** |  The possible \&quot;type\&quot; value as below: - recognition - tracking - gender - age_group - quantity - color_detect - age - expression - tracking  | [optional] 
**data** | [**VisionsResults**](VisionsResults.md) |  | [optional] 
**timestamp** | **int** | The timestamp. | [optional] 
**status** | **str** |  The vision task status. The possible values: - idle - run  | [optional] 
**msg** | **str** | Return message | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


