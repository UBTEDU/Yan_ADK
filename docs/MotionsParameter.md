# MotionsParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  Beside the default and user uploaded motion name, it also can support below value: - raise - crouch - stretch - come on - wave - bend - walk - turn around - head - bow | 
**direction** | **str** |  When the name is raise | stretch | come on | wave, direction value as below: - left - right - both  When the name is bend | turn around, direction value as below: - left - right  When the name is walk, direction value as below: - front - back - left - right  When the name is head, direction value as below: - front - left - right  | [optional] 
**repeat** | **int** | The motion running times | [optional] [default to 1]
**speed** | **str** |  All the supported speed: - very slow - slow - normal - fast - very fast | [optional] [default to 'normal']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


