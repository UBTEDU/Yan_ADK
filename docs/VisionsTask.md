# VisionsTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  Define the vision task type. The ranges should be in: - tracking - recognition - gender - age_group - quantity - color_detect - age - expression  | 
**operation** | **str** |  Define the vision task operation. The ranges should be in: - start - stop  | 
**option** | **str** |  Define the vision task option. The ranges should be in: - face - color - object  Constraint: If option is \&quot;face\&quot;, type should be in : - tracking - recognition - quantity - age_group - gender - age - expression  If option is \&quot;color\&quot;, type should be in : - color_detect If option is \&quot;object\&quot;, type should be in : - recognition  | [optional] 
**timestamp** | **int** | The vision task timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


