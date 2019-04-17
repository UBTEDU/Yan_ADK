# VisionsTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 任务类型。 type 允许上传的值有 &#39;tracking&#39;, &#39;recognition&#39;, &#39;gender&#39;, &#39;age_group&#39;, &#39;quantity&#39;, &#39;color_detect&#39;  | 
**operation** | **str** | 执行命令。 operation 允许上传的值有 &#39;start&#39;, &#39;stop&#39;  | 
**option** | **str** | 任务名称。 option 允许上传的值有 &#39;face&#39;, &#39;color&#39;。 组合限制：tracking任务支持face, recognition任务支持face。quantity任务支持face。 age_group, gender支持face。color_detect任务支持color。 | [optional] 
**timestamp** | **int** | 视觉任务时间戳 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


