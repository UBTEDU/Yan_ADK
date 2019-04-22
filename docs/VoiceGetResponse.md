# VoiceGetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 返回码，0表示正常 | 
**status** | **str** | 当获取语义理解或是语音听写状态时，状态有 &#39;idle&#39;, &#39;run&#39;。 当为语音合成时, 状态有 &#39;idle&#39;, &#39;run&#39;, &#39;build&#39;, &#39;wait&#39;。 在语音合成中 &#39;idle&#39; 为该tts任务不存在, build为正在合成该段语音, run为播放该段语音, wait为处于等待执行状态。在语义理解或是语音听写中，&#39;idle为非执行状态&#39;, &#39;run&#39;为正在运行。  | [optional] 
**timestamp** | **int** | 时间戳, Unix标准时间 | [optional] 
**data** | **object** | 语音返回数据 | 
**msg** | **str** | 提示信息 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


