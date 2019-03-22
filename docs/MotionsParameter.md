# MotionsParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 动作名称,除了内置动作还有:raise/crouch/stretch/come on/wave/bend/walk/turn around/head/bow | 
**direction** | **str** | 部分动作有方向属性，取值说明：（1）left 只适用于name取值为raise, stretch, come on, wave, bend, turn around, walk, head；（2）right 只适用于name取值为：raise, stretch, come on, wave, bend, turn around, walk, head；（3）both  只适用于name取值为：raise, stretch, come on, wave；（4）front 只适用于name取值为：walk, head；（5）back 只适用name取值为： walk； | [optional] 
**repeat** | **int** | 动作重复执行的次数 | [optional] [default to 1]
**speed** | **str** | 部分动作(raise/crouch/stretch/come on/wave/bend/walk/turn around/head/bow)可设置运动速度 | [optional] [default to 'normal']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


