# VoiceGetOfflineSyntaxResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grammar** | **str** |  Define offline grammar. Only support alphabets.  | 
**slot** | [**list[VoiceOfflineSlot]**](VoiceOfflineSlot.md) |  Declare the slot, the content can support alphabets and numbers. All operators and keywords are half-width characters. The full-width characters cannot supported.  | 
**start** | **str** |  Declare the slot, the content can support alphabets and numbers. All operators and keywords are half-width characters. The full-width characters cannot supported.  | 
**startinfo** | **str** |  Define start rule details.  | 
**rule** | [**list[VoiceOfflineSyntaxRule]**](VoiceOfflineSyntaxRule.md) |  Define all offline rules&#39; name and value. The rule&#39;s value should not be NULL.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


