# VoiceGetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Return code, 0 means success | 
**status** | **str** |  All scenarios: If the task is auto transform (iat), the status value as below: - idle - run  If the task is auto speech recognition (asr), the status value as below: - idle - run  If the task is text to speech (tts), the status value as below: - idle - run - build - wait  | [optional] 
**timestamp** | **int** | Timestamp, Unix standard time. | [optional] 
**data** | **object** | Voice return value | 
**msg** | **str** | Return message | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


