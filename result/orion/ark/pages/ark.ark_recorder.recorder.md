---
title: "ark.ark_recorder.recorder package"
docname: "ark.ark_recorder.recorder"
source: "http://orion.longsys.com/ark.ark_recorder.recorder.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_recorder.recorder package
## Submodules
## ark.ark_recorder.recorder.ark_recorder_factory module

_class _ark.ark_recorder.recorder.ark_recorder_factory.ArkRecorderFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_recorder_type_)


Brief:

Initialising objects.

Returns:

Recorder object.
## ark.ark_recorder.recorder.ark_recorder_interface module

_class _ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface

Bases: `ABC`
Abstract class that declares interfaces for the operation of recorder.

get_data()


Brief:

Get the data from the previous measurement.

Returns:

(tuple) A tuple containing: - error_code (int): The error code, 0 indicates success, non-zero indicates failure. - data (list): The data recorded in the previous measurement.

_abstract _init(_device_address_ , _username_ , _password_)


Brief:

Init the recorder component,

Parameters:

  * **device_address** – (str) The recorder’s ip address.
  * **username** – (str) The recorder’s username.
  * **password** – (str) The recorder’s password.


Returns:

(int) Error code, 0 indicates success, non-zero indicates failure.

save_channel_data_to_csv(_data_ , _file_path_)


Brief:

Save the collected channel data to a CSV file. This function takes the collected data from dynamic or periodic measurements and writes it into a CSV file for storage and analysis.

Parameters:

  * **data** – (List) The data to be saved, typically collected from the start_measurement or start_dynamic_measurement function. This list contains the values collected from each channel during the measurement process.
  * **file_path** – (str) The path of the csv file would be store in.


Returns:

(int) Error code, 0 indicates success, non-zero indicates failure.

_abstract _set_channel_properties(_ch_num_ , _input_type_ , _channel_range_)


Brief:

Set the properties of a channel. This function configures the measurement properties for each channel of the data logger. By setting the measurement type (TEMP or DC) and range, the user can collect different types of test data based on the actual testing requirements.

Parameters:

  * **ch_num** – (int) Channel number, a positive integer starting from 1. The GL840 has 20 channels by default without any expansion.
  * **input_type** – (InputType) Measurement type, either TEMP (temperature) or DC (direct current voltage), defined by the InputType enum.
  * **channel_range** – (TEMPRange or DCRange) Range specification, defined by either the TEMPRange or DCRange enum. If the measurement type is TEMP, channel_range should be a TEMPRange value, o therwise it should be a DCRange value.


Returns:

(int) Error code, 0 indicates success, non-zero indicates failure.

start_dynamic_measurement(_measure_interval_)


Brief:

Start dynamic measurement. The user can set the sampling interval, and the measurement process will continue running until an external signal is received to stop it. This interface is suitable for scenarios where the duration of the measurement is unknown, such as real-time monitoring or dynamic experiments. The data could be aquired after the measurement complete using interface “get_data”.

Parameters:

**measure_interval** – (Interval) Measurement interval, The sampling interval, which specifies the time gap between consecutive measurements, defined by the Interval enum.

Returns:

(tuple) A tuple containing: - error_code (int): The error code, 0 indicates success, non-zero indicates failure.

start_measurement(_measure_count_ , _measure_interval_)


Brief:

Start dynamic measurement. This function allows the user to specify the number of measurements and the time interval between them. It collects data from the channels at the specified frequency. The data could be aquired after the measurement complete using interface “get_data”.

Parameters:

  * **measure_count** – (int) The number of measurements to be taken. Specifies how many times data should be collected.
  * **measure_interval** – (Interval) Measurement interval, The sampling interval, which specifies the time gap between consecutive measurements, defined by the Interval enum.


Returns:

(tuple) A tuple containing: - error_code (int): The error code, 0 indicates success, non-zero indicates failure.

stop_dynamic_measurement()


Brief:

Stop the ongoing dynamic measurement. This function halts the measurement process that was started by the start_dynamic_measurement function. The process will stop immediately upon receiving the signal.

Returns:

(int) Error code, 0 indicates success, non-zero indicates failure.

_class _ark.ark_recorder.recorder.ark_recorder_interface.DC_Range(_value_)

Bases: `Enum`
An enumeration.

DC_100V _ = '100V'_


DC_100mV _ = '100mV'_


DC_10V _ = '10V'_


DC_1V _ = '1V'_


DC_1_5V _ = '1-5V'_


DC_200mV _ = '200mV'_


DC_20V _ = '20V'_


DC_20mV _ = '20mV'_


DC_2V _ = '2V'_


DC_500mV _ = '500mV'_


DC_50V _ = '50V'_


DC_50mV _ = '50mV'_


DC_5V _ = '5V'_


_class _ark.ark_recorder.recorder.ark_recorder_interface.InputType(_value_)

Bases: `Enum`
An enumeration.

DC _ = 'DC'_


TEMP _ = 'TEMP'_


_class _ark.ark_recorder.recorder.ark_recorder_interface.Interval(_value_)

Bases: `Enum`
An enumeration.

H_1 _ = '3600s'_


MIN_1 _ = '60s'_


MIN_10 _ = '600s'_


MIN_2 _ = '120s'_


MIN_20 _ = '1200s'_


MIN_30 _ = '1800s'_


MIN_5 _ = '300s'_


MS_200 _ = '200ms'_


MS_250 _ = '250ms'_


MS_500 _ = '500ms'_


S_1 _ = '1s'_


S_10 _ = '10s'_


S_2 _ = '2s'_


S_20 _ = '20s'_


S_30 _ = '30s'_


S_5 _ = '5s'_


_class _ark.ark_recorder.recorder.ark_recorder_interface.RecorderType(_value_)

Bases: `Enum`
An enumeration.

GL840 _ = 'GL840'_


GL860 _ = 'GL860'_


_class _ark.ark_recorder.recorder.ark_recorder_interface.TEMP_Range(_value_)

Bases: `Enum`
An enumeration.

TEMP_100C _ = '100'_


TEMP_2000C _ = '2000'_


TEMP_500C _ = '500'_

## Module contents
