---
title: "ark.ark_recorder package"
docname: "ark.ark_recorder"
source: "http://orion.longsys.com/ark.ark_recorder.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_recorder package
## Subpackages
  * [ark.ark_recorder.recorder package](ark.ark_recorder.recorder.md)
    * [Submodules](ark.ark_recorder.recorder.md#submodules)
    * [ark.ark_recorder.recorder.ark_recorder_factory module](ark.ark_recorder.recorder.md#module-ark.ark_recorder.recorder.ark_recorder_factory)
      * [`ArkRecorderFactory`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_factory.ArkRecorderFactory)
        * [`ArkRecorderFactory.create_object()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_factory.ArkRecorderFactory.create_object)
    * [ark.ark_recorder.recorder.ark_recorder_interface module](ark.ark_recorder.recorder.md#module-ark.ark_recorder.recorder.ark_recorder_interface)
      * [`ArkRecorderInterface`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface)
        * [`ArkRecorderInterface.get_data()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.get_data)
        * [`ArkRecorderInterface.init()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.init)
        * [`ArkRecorderInterface.save_channel_data_to_csv()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.save_channel_data_to_csv)
        * [`ArkRecorderInterface.set_channel_properties()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.set_channel_properties)
        * [`ArkRecorderInterface.start_dynamic_measurement()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.start_dynamic_measurement)
        * [`ArkRecorderInterface.start_measurement()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.start_measurement)
        * [`ArkRecorderInterface.stop_dynamic_measurement()`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.ArkRecorderInterface.stop_dynamic_measurement)
      * [`DC_Range`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range)
        * [`DC_Range.DC_100V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_100V)
        * [`DC_Range.DC_100mV`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_100mV)
        * [`DC_Range.DC_10V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_10V)
        * [`DC_Range.DC_1V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_1V)
        * [`DC_Range.DC_1_5V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_1_5V)
        * [`DC_Range.DC_200mV`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_200mV)
        * [`DC_Range.DC_20V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_20V)
        * [`DC_Range.DC_20mV`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_20mV)
        * [`DC_Range.DC_2V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_2V)
        * [`DC_Range.DC_500mV`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_500mV)
        * [`DC_Range.DC_50V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_50V)
        * [`DC_Range.DC_50mV`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_50mV)
        * [`DC_Range.DC_5V`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.DC_Range.DC_5V)
      * [`InputType`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.InputType)
        * [`InputType.DC`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.InputType.DC)
        * [`InputType.TEMP`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.InputType.TEMP)
      * [`Interval`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval)
        * [`Interval.H_1`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.H_1)
        * [`Interval.MIN_1`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MIN_1)
        * [`Interval.MIN_10`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MIN_10)
        * [`Interval.MIN_2`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MIN_2)
        * [`Interval.MIN_20`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MIN_20)
        * [`Interval.MIN_30`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MIN_30)
        * [`Interval.MIN_5`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MIN_5)
        * [`Interval.MS_200`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MS_200)
        * [`Interval.MS_250`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MS_250)
        * [`Interval.MS_500`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.MS_500)
        * [`Interval.S_1`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.S_1)
        * [`Interval.S_10`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.S_10)
        * [`Interval.S_2`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.S_2)
        * [`Interval.S_20`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.S_20)
        * [`Interval.S_30`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.S_30)
        * [`Interval.S_5`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.Interval.S_5)
      * [`RecorderType`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.RecorderType)
        * [`RecorderType.GL840`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.RecorderType.GL840)
        * [`RecorderType.GL860`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.RecorderType.GL860)
      * [`TEMP_Range`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.TEMP_Range)
        * [`TEMP_Range.TEMP_100C`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.TEMP_Range.TEMP_100C)
        * [`TEMP_Range.TEMP_2000C`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.TEMP_Range.TEMP_2000C)
        * [`TEMP_Range.TEMP_500C`](ark.ark_recorder.recorder.md#ark.ark_recorder.recorder.ark_recorder_interface.TEMP_Range.TEMP_500C)
    * [Module contents](ark.ark_recorder.recorder.md#module-ark.ark_recorder.recorder)


## Module contents
@Module : ark_recorder
@Date : 2024/11/30 13:51
@Version : V1.0.0
The ark_recorder module is based on the GL840 data logger, the component can set the properties of each channel of the recorder, collect data in real time, provide data monitoring during the test process, and facilitate the analysis of problems.
