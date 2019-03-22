# VisionsTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 任务类型。 type 允许上传的值有 &#39;tracking&#39;, &#39;recognition&#39;, &#39;gender_analysis&#39;, &#39;age_analysis&#39;, &#39;expression_analysis&#39;, &#39;quantity&#39;  | 
**operation** | **str** | 执行命令。 operation 允许上传的值有 &#39;start&#39;, &#39;stop&#39;  | 
**option** | **str** | 任务名称。 option 允许上传的值有 &#39;face&#39;, &#39;hand&#39;, &#39;object&#39;。 组合限制：tracking任务支持face, recognition任务支持face, hand 与 object。quantity任务支持face与hand。 age_analysis, gender_analysis, age_analysis 与 expression_analysis只支持face | [optional] 
**timestamp** | **int** | 视觉任务时间戳 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


