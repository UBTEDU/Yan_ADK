# VisionsGetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 返回码，0表示正常 | 
**type** | **str** | 消息类型。 一次只返回一种类型的数据。 type 允许的值为: &#39;recognition&#39;, &#39;tracking&#39;,&#39;gender&#39;, &#39;age_group&#39;, &#39;quantity&#39;, &#39;color_detect&#39; | 
**data** | [**VisionsResults**](VisionsResults.md) |  | [optional] 
**timestamp** | **int** | 任务时间戳 | [optional] 
**status** | **str** | 状态 | [optional] 
**msg** | **str** | 提示信息 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


