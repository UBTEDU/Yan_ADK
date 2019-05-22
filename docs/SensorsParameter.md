# SensorsParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  All sensors&#39; type: - gyro    gyroscope sensor - infrared    infrared sensor - ultrasonic    ultrasonic sensor - touch   touch sensor - pressure  pressure sensor  | [default to 'gyro']
**id** | **int** |  | 
**value** | **int** |  When \&quot;operation\&quot; is \&quot;calibrate\&quot;, ignore this field. When \&quot;operation\&quot; is \&quot;modify\&quot;, it means setting the sensor&#39;s I2C address. Please note, when the slot value is exist, \&quot;modify\&quot; is not available.  All the sensor I2C address range as below: - Ultrasonic sensor   17~22; - Infrared sensor     23~28; - Touch sensor        29~34; - Pressure Sensor     35~40;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


