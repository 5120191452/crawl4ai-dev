---
title: "ark.ark_power.power package"
docname: "ark.ark_power.power"
source: "http://orion.longsys.com/ark.ark_power.power.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_power.power package
## Submodules
## ark.ark_power.power.ark_power_factory module

_class _ark.ark_power.power.ark_power_factory.ArkPowerFactory(_* args_, _** kwargs_)

Bases: `object`
Responsible for controlling the power device. it dynamically selects the appropriate adapter based on the type of power device provided and delegates the power control and other related operations to the selected adapter.

create_object(_powerdevice_type_)


Brief:

Initialising objects(based on power control equipment types)

Parameters:

**powerdevice_type** – optional values in the DeviceType enumeration class are supported

Returns:

Success returns the corresponding object, failure returns None.
## ark.ark_power.power.ark_power_interface module

_class _ark.ark_power.power.ark_power_interface.ArkPowerInterface

Bases: `ABC`
Abstract class that declares an interface for the operation of oven.

_abstract _cold_boot(_off_wait_time =10_, _on_wait_time =10_, _cycle =1_)


Brief:

Control the PC host to wait for a period of time, then power off and shut down, and after waiting for another period of time, power on and boot up the system.

Parameters:

  * **(****int****)** (_cycle_) – The time to wait before shutting down the system. The param unit is second.
  * **(****int****)** – The time to wait before booting up the system. The param unit is second.
  * **(****int****)** – The number of cycles to be executed.


Returns:

Success returns 0, failure returns the corresponding error code.

_abstract _continuous_current_acquisition(_acquisition_count_ , _acquisition_interval_ , _dc_current_range =DCCurrentRange.A_1_)


Brief:

This method is used to test the DC current of a device. It allows the user to set the number of acquisitions and the acquisition interval to suit different measurement needs and environments. The method provides flexible measurement configurations, allowing users to acquire accurate voltage data based on specific application scenarios.

Parameters:

  * **acquisition_count** – The number of collections is the total number of samples collected during a single measurement.
  * **acquisition_interval** – The acquisition interval, in seconds (s), is the time between the end of the previous acquisition time and the start of the next acquisition.
  * **dc_current_range** – The measurement range for DC current, using the DCCurrentRange enumeration. Defaults to DCCurrentRange.A_1 to simplify basic usage while allowing range adjustment for different current levels.


Returns:

error codes and a list of DC current values for each detection.DC current values for each detection.

⚠️ Notes:

1.Currently, this interface is only applicable for scenarios involving precision current instruments. 2.Please ensure that the interface is used in DMM (measurement) mode of the precision ammeter. The explanation of the relevant DMM mode can be found at the bottom.

_abstract _continuous_voltage_acquisition(_acquisition_count_ , _acquisition_interval_ , _dc_voltage_range =DCVoltageRange.V_1_)

This method is used to test the DC voltage of a device. It allows the user to set the number of acquisitions and the acquisition interval to suit different measurement needs and environments. The method provides flexible measurement configurations, allowing users to acquire accurate voltage data based on specific application scenarios.

Parameters:

  * **acquisition_count** – The number of collections is the total number of samples collected during a single measurement.
  * **acquisition_interval** – The acquisition interval, in seconds (s), is the time between the end of one acquisition and the start of the next.
  * **dc_voltage_range** – The measurement range for DC voltage. Defaults to DCVoltageRange.V_1 to simplify basic usage while allowing range adjustment for different voltage levels.


Returns:

Error codes and a list of DC voltage values for each detection.

⚠️ Notes:

1. Currently, this interface is only applicable for scenarios involving precision current instruments. 2. Please ensure that the interface is used in DMM (measurement) mode of the precision ammeter. The explanation of the relevant DMM mode can be found at the bottom.

_abstract _get_SDIO_vol(_pin_)


Brief:

Get SDIO voltage value.

Parameters:

**pin** – SDIO Pin Parameters: 0: SD_D0, 1: SD_D1, 2: SD_D2, 3: SD_D3, 4: SD_CMD, 5: SD_CLK

Returns:

This function returns two values, the result of the operation, the SDIO actual voltage value. The result of the operation: Success returns 0, failure returns the corresponding error code. The SDIO actual voltage: SDIO vol.

_abstract _get_current_data(_num =0_)


Brief:

Get N sets of current data (Applicable to Digitize mode if you use precision current instruments).

Parameters:

**num** – get the number of groups(N) of current. Default 0 means to retrieve all data

Returns:

res: Success returns 0, failure returns the corresponding error code data: - For mcu: A list containing N current data values. - For precision current instruments: A string representing the file path to a CSV file containing the captured current data.

_abstract _get_current_nplc()

Get the Number of Power Line Cycles (NPLC) from precision current instruments.
NPLC indicates the number of power line cycles used by the benchtop multimeter during a measurement. A power line cycle is typically:
  * **50 Hz** : 20 milliseconds
  * **60 Hz** : 16.67 milliseconds


The NPLC value determines the sampling duration. A higher NPLC value (e.g., 5) provides higher accuracy and lower noise but takes more time. A lower NPLC value (e.g., 0.1) allows for faster measurements.

Returns:

Success returns 0, failure returns the corresponding error code.

⚠️ Notes:

1. Currently, this interface is only applicable for scenarios involving precision current instruments. 2. Please ensure that the interface is used in DMM (measurement) mode of the precision ammeter. The explanation of the relevant DMM mode can be found at the bottom.

_abstract _get_current_voltage()


Brief:

Get current voltage value.

Returns:

This function returns three values, the result of the operation, the current vcc, the current vccq. The result of the operation: Success returns 0, failure returns the corresponding error code. The current vcc: current vcc value. The current vccq: current vccq value.

_abstract _get_power_consumption()


Brief:

Getting the power consumption of a power supply. This feature is not supported at this time due to MCU protocol.

Returns:

self.module_err | self.error_list.err_function_not_supported

_abstract _get_target_voltage()


Brief:

Get target voltage value.

Returns:

This function returns three values, the result of the operation, the target vcc, the target vccq. The result of the operation: Success returns 0, failure returns the corresponding error code. The target vcc: target vcc value. The target vccq: target vccq value.

_abstract _get_voltage_data(_num =0_)


Brief:

Get N sets of voltage data (Applicable to Digitize mode if you use precision current instruments).

Parameters:

**num** – get the number of groups(N) of voltage. Default 0 means to retrieve all data

Returns:

res: Success returns 0, failure returns the corresponding error code data: - For mcu: A list containing N current data values. - For precision current instruments: A string representing the file path to a CSV file containing the captured current data.

_abstract _get_voltage_nplc()

Get the Number of Power Line Cycles (NPLC) for precision current instruments.
NPLC indicates the number of power line cycles used by the benchtop multimeter during a measurement. A power line cycle is typically a 50 Hz or 60 Hz cycle, i.e., 20 milliseconds or 16.67 milliseconds.
The NPLC value determines how many times the multimeter samples the signal in one cycle (i.e., the higher the NPLC value, the more cycles to be sampled and the longer the sampling time).
If high accuracy and low noise measurements are required, a higher NPLC value can be selected, e.g. 5. If fast measurements are required, a lower NPLC value can be selected, e.g. 0.1.

Returns:

Success returns 0, failure returns the corresponding error code.

⚠️ Notes:

1. Currently, this interface is only applicable for scenarios involving precision current instruments. 2. Please ensure that the interface is used in DMM (measurement) mode of the precision ammeter. The explanation of the relevant DMM mode can be found at the bottom.

_abstract _gpio_control(_pa_number_ , _level_)


Brief:

Controls the pull-up/pull-down state of PA series GPIO pins.

Parameters:

  * **pa_number** – The pin index to control (e.g., 6 for PA6, 7 for PA7, Currently, only these two values are supported).
  * **level** – The target voltage level (1 for PULL_UP, 0 for PULL_DOWN).


Returns:

The result of the operation: Success returns 0, failure returns the corresponding error code.

_abstract _hot_boot()


Brief:

instructs the system to restart immediately.

Returns:

Success returns 0, failure returns the corresponding error code.

_abstract _low_power_mode(_mode_)


Brief:

Entering low-power mode. This feature is not supported at this time due to MCU protocol.

Returns:

self.module_err | self.error_list.err_function_not_supported

_abstract _power_connect(_addr_ , _baudrate =115200_, _bytesize =8_, _parity ='N'_, _stopbits =1_, _timeout =3_, _xonxoff =False_, _rtscts =False_, _write_timeout =None_, _dsrdtr =False_, _inter_byte_timeout =None_, _exclusive =None_)


Breif:

Establishing a communication link with related power device(s).

Parameters:

  * **(****string****)** (_addr_) –
The address of the power control equipment. The address format of the power equipment controlling the Windows cold boot is ‘vid:pid’, for example, ‘0x0483:0x5750’. The address format of the power supply controlled by the MCU is a device file.
> In Linux, it is similar to “/dev/ttyUSB0”, while for the 3720, it is similar to “/dev/ttyMV1”.
The address format of the power supply controlled by the speed-spor is a device file, It represents speed spor itself, such as: “/dev/sdc”. The address format of the precision current instrument is the IP address displayed on the instrument, similar to “169.254.83.176”.
  * **others** – please reference <https://pyserial.readthedocs.io/en/latest/pyserial_api.html>


Returns:

Success returns 0, failure returns an error code

_abstract _power_disconnect()


Breif:

Disconnect from power control equipment.

_abstract _power_down()


Brief:

Powering down the storage media.

Returns:

Success returns 0, failure returns the corresponding error code

_abstract _power_off_on_slope(_vol_type_ , _is_power_on_)


Brief:

Power off on slope.

Parameters:

  * **vol_type** – Reference enumeration classes.
  * **is_power_on** – 0x01 indicates slope up, 0x00 indicates slope down.


Returns:

The result of the operation: Success returns 0, failure returns the corresponding error code.

_abstract _power_up()


Brief:

Powering up the storage media.

Returns:

Success returns 0, failure returns the corresponding error code

_abstract _pwrtest(_count =1_, _delay =5_, _period =30_, _sleep_state =3_, _wdk_path =None_)


Brief:

PwrTest Sleep Program.

Parameters:

  * **count** – Specifies the number of sleep/wake cycles to perform.
  * **delay** – Sets the delay (in seconds) before entering sleep.
  * **period** – Specifies the time (in seconds) the system stays in the sleep state before waking up.
  * **sleep_state** – Defines the sleep state to be tested. The options can represent different power states like standby (S1), sleep (S3), hibernate (S4), etc. For more detailed information, please refer to ‘<https://learn.microsoft.com/zh-cn/windows-hardware/drivers/devtest/pwrtest-syntax>’


Returns:

Success returns 0, failure returns the corresponding error code

_abstract _set_current(_current_)


Brief:

Setting current. This feature is not supported at this time due to MCU protocol.

Returns:

self.module_err | self.error_list.err_function_not_supported

_abstract _set_current_configuration(_cur_gear_ , _vol_gear_)


Brief:

Setting the MCU Current Configuration.

Parameters:

  * **cur_gear** – Current block, 1 for milliamps, 2 for microamps
  * **vol_gear** – Voltage gear, 1 for VCC, 2 for VCCQ


Returns:

Success returns 0, failure returns the corresponding error code cur_gear: Current current block, 1 indicates milliampere block, 2 indicates microampere block vol_gear: Current voltage block, 1 for VCC, 2 for VCCQ

_abstract _set_current_nplc(_nplc_value_)

Set the Number of Power Line Cycles (NPLC) for precision current instruments.
NPLC indicates the number of power line cycles used by the benchtop multimeter during a measurement. A power line cycle is typically a 50 Hz or 60 Hz cycle, i.e., 20 milliseconds or 16.67 milliseconds.
The NPLC value determines how many times the multimeter samples the signal in one cycle (i.e., the higher the NPLC value, the more cycles to be sampled and the longer the sampling time).
If high accuracy and low noise measurements are required, a higher NPLC value can be selected, e.g. 5. If fast measurements are required, a lower NPLC value can be selected, e.g. 0.1.

Parameters:

**nplc_value** – Power Line Cycle Number, specifies the number of power line cycles to be measured (0.0005NPLC~5NPLC). The user only needs to input a floating point number between 0.0005~5.

Returns:

Success returns 0, failure returns the corresponding error code.

⚠️ Notes:

1. Currently, this interface is only applicable for scenarios involving precision current instruments. 2. Please ensure that the interface is used in DMM (measurement) mode of the precision ammeter. The explanation of the relevant DMM mode can be found at the bottom.

_abstract _set_current_sampling_params(_sampling_time : int_, _sampling_number : int_)


Brief:

Set the current sampling time and number of samples (Applicable to Digitize mode).

Parameters:

  * **sampling_time** – current sampling time (in seconds, min. 1).
  * **sampling_number** – Number of samples to collect within the sampling time.


Notes:

  *

For power analyzer devices, the sampling rate is calculated as:

sampling_rate = sampling_number / sampling_time
  *

The sampling rate (in Hz) must be within the supported range:

1,000 Hz to 1,000,000 Hz
  * The actual supported range may vary depending on the instrument model.


Example:

If sampling_time = 10 seconds and sampling_number = 50,000, the effective sampling rate = 5,000 Hz.

Returns:

Success returns 0, failure returns the corresponding error code

⚠️ Notes:

  * Please use this function in conjunction with the “stop_measurement” function(Only when using precision current instruments).
  * If the stop_ceasure function is not called, the collection will continue for two hours before stopping.


_abstract _set_current_sampling_type(_sampling_type_)


Brief:

“set_current_sampling_type” is deprecated and will be removed in a future version. use “set_sampling_type” instead
details: please check set_sampling_type annotation

_abstract _set_sampling_type(_sampling_type : [MeasurementType](ark.ark_power.power.md#ark.ark_power.power.ark_power_interface.MeasurementType "ark.ark_power.power.ark_power_interface.MeasurementType")_, _sensitivity_level : [ResolutionLevel](ark.ark_power.power.md#ark.ark_power.power.ark_power_interface.ResolutionLevel "ark.ark_power.power.ark_power_interface.ResolutionLevel") = ResolutionLevel.LEVEL_1_)


Brief:

Set the measurement range and precision for the power analyzer, based on the specified current or voltage type and resolution level (Applicable to Digitize mode).

Parameters:

  * **sampling_type** – MeasurementType Enum, indicating the type of measurement (e.g., uA, mA, A, mV, V)
  * **sensitivity_level** – ResolutionLevel Enum (LEVEL_1, LEVEL_10, LEVEL_100), default is LEVEL_1


Supported range values for power analyzer devices:

Voltage Ranges:

  * 100mV, 1V, 10V, 100V, 1000V
  * Accepted values: ‘100mV’, ‘1V’, ‘10V’, ‘100V’, ‘1000V’


Current Ranges:

  * 10uA, 100uA, 1mA, 10mA, 100mA, 1A, 3A
  * Accepted values: ‘10uA’, ‘100uA’, ‘1mA’, ‘10mA’, ‘100mA’, ‘1A’, ‘3A’


⚠️ Notes:

  * Only the above listed ranges are supported; using any unsupported value will raise an error.
  * Ensure the enum values map correctly to the expected device command strings.


Returns:

0 on success, or an appropriate error code on failure.

_abstract _set_slope_power_down_parameters(_vol_type_ , _node_num_ , _buffer_)


Brief:

Command Parameters Needed to Set Slope Power-Down.

Parameters:

  * **vol_type** – Reference enumeration classes(except vcc_and_vccq).
  * **node_num** – Actual number of waveform segments, supports up to 12 segments.
  * **buffer** – image data.


Returns:

The result of the operation: Success returns 0, failure returns the corresponding error code.

_abstract _set_slope_power_up_parameters(_vol_type_ , _node_num_ , _buffer_)


Brief:

Command Parameters Needed to Set Slope Power-Up.

Parameters:

  * **vol_type** – Reference enumeration classes(except vcc_and_vccq).
  * **node_num** – Actual number of waveform segments, supports up to 12 segments.
  * **buffer** – image data.


Returns:

The result of the operation: Success returns 0, failure returns the corresponding error code.

_abstract _set_vcc(_vcc_)


Brief:

Setting the voltage of the storage medium (VCC)

Parameters:

**vcc** – voltage (VCC) value to be set

Returns:

Success returns 0, failure returns the corresponding error code

_abstract _set_vcc_alarm_range(_vcc_min_ , _vcc_max_)


Brief:

Setting the voltage(VCC) alarm range

Parameters:

  * **vcc_min** – voltage value alarm lower(unit: millivolt)
  * **vcc_max** – voltage value alarm upper(unit: millivolt)


Returns:

Success returns 0, failure returns the corresponding error code

_abstract _set_vccq(_vccq_)


Brief:

Setting the EMMC vccq voltage

Parameters:

**vccq** – voltage (VCCQ) value to be set

Returns:

Success returns 0, failure returns the corresponding error code

_abstract _set_voltage_nplc(_nplc_value_)

Set the Number of Power Line Cycles (NPLC) for precision voltage measurement.
NPLC indicates the number of power line cycles used by the benchtop multimeter during a measurement. A power line cycle is typically a 50 Hz or 60 Hz cycle, i.e., 20 milliseconds or 16.67 milliseconds.
The NPLC value determines how many times the multimeter samples the signal in one cycle (i.e., the higher the NPLC value, the more cycles to be sampled and the longer the sampling time).
If high accuracy and low noise measurements are required, a higher NPLC value can be selected, e.g. 5. If fast measurements are required, a lower NPLC value can be selected, e.g. 0.1.

Parameters:

**nplc_value** – Power Line Cycle Number, specifies the number of power line cycles to be measured (0.0005NPLC~5NPLC). The user only needs to input a floating point number between 0.0005~5.

Returns:

Success returns 0, failure returns the corresponding error code.

⚠️ Notes:

1. Currently, this interface is only applicable for scenarios involving precision current instruments. 2. Please ensure that the interface is used in DMM (measurement) mode of the precision ammeter. The explanation of the relevant DMM mode can be found at the bottom.

_abstract _set_voltage_sampling_params(_sampling_time : int_, _sampling_number : int_)


Brief:

Configure voltage sampling parameters: total sampling duration and number of samples (Applicable to Digitize mode).

Parameters:

  * **sampling_time** – voltage sampling time (in seconds, min. 1).
  * **sampling_number** – Number of samples to collect within the sampling time.


Notes:

  *

For power analyzer devices, the sampling rate is calculated as:

sampling_rate = sampling_number / sampling_time
  *

The sampling rate (in Hz) must be within the supported range:

1,000 Hz to 1,000,000 Hz
  * The actual supported range may vary depending on the instrument model.


Example:

If sampling_time = 10 seconds and sampling_number = 50,000, the effective sampling rate = 5,000 Hz.

Returns:

0 on success, or a device-specific error code on failure.

⚠️ Notes:

  * Please use this function in conjunction with the “stop_measurement” function(Only when using precision current instruments).
  * If the stop_ceasure function is not called, the collection will continue for two hours before stopping.


_abstract _stop_measurement()


Brief:

This method stops the measurement of the precision current instruments.

⚠️ Notes:

  * This function is used to stop sampling. Please use it in conjunction with the set_current_samping_params function and the set_voltage_stampling_params function(Only when using precision current instruments)


_class _ark.ark_power.power.ark_power_interface.CurrentUnit(_value_)

Bases: `Enum`
An enumeration.

A _ = 'A'_


MA _ = 'mA'_


UA _ = 'uA'_


_class _ark.ark_power.power.ark_power_interface.DCCurrentRange(_value_)

Bases: `Enum`
An enumeration.

A_1 _ = 1_


A_3 _ = 3_


mA_1 _ = 0.001_


mA_10 _ = 0.01_


mA_100 _ = 0.1_


uA_10 _ = 1e-05_


uA_100 _ = 0.0001_


_class _ark.ark_power.power.ark_power_interface.DCVoltageRange(_value_)

Bases: `Enum`
An enumeration.

V_1 _ = 1_


V_10 _ = 10_


V_100 _ = 100_


V_1000 _ = 1000_


mV_100 _ = 0.1_


_class _ark.ark_power.power.ark_power_interface.InterfaceType(_value_)

Bases: `Enum`
Interfaces supported by the 3720

EMMC_3720_and_1296 _ = 'EMMC_3720_and_1296'_


SD_3720_and_1296 _ = 'SD_3720_and_1296'_


USB_3720_and_1296 _ = 'USB_3720_and_1296'_


_class _ark.ark_power.power.ark_power_interface.MeasurementType(_value_)

Bases: `Enum`
电流量级类型（单位），用于设置采样精度范围

A _ = 'A'_


V _ = 'V'_


mA _ = 'mA'_


mV _ = 'mV'_


uA _ = 'uA'_


_class _ark.ark_power.power.ark_power_interface.PowerType(_value_)

Bases: `Enum`
Supported types are serial_3720, power_win

power_meter _ = 'power_meter'_


power_win _ = 'power_win'_


scsi_speed_spor _ = 'scsi_speed_spor'_


serial_1296 _ = 'serial_1296'_


serial_3720 _ = 'serial_3720'_


serial_9300_6877 _ = 'serial_9300_6877'_


serial_relay _ = 'serial_relay'_


_class _ark.ark_power.power.ark_power_interface.RelayConfig(_value_)

Bases: `IntEnum`
固定硬件配置

CLOSE_NO_FEEDBACK _ = 0_


DEFAULT_CH _ = 1_


OPNE_NO_FEEDBACK _ = 1_


RESPONSE_LENGTH _ = 4_


START_BYTE _ = 160_


_class _ark.ark_power.power.ark_power_interface.RelayOp(_value_)

Bases: `IntEnum`
继电器操作码枚举

FLASH _ = 6_


OFF _ = 0_


OFF_FB _ = 2_


ON _ = 1_


ON_FB _ = 3_


QUERY _ = 5_


TOGGLE _ = 4_


_class _ark.ark_power.power.ark_power_interface.ResolutionLevel(_value_)

Bases: `Enum`
分辨率等级：控制测量灵敏度/精度

LEVEL_1 _ = 1_


LEVEL_10 _ = 10_


LEVEL_100 _ = 100_


LEVEL_3 _ = 3_


_class _ark.ark_power.power.ark_power_interface.VoltageType(_value_)

Bases: `Enum`
An enumeration.

vcc _ = 1_


vcc_and_vccq _ = 2_


vccq _ = 0_


_class _ark.ark_power.power.ark_power_interface.VoltageUnit(_value_)

Bases: `Enum`
An enumeration.

MV _ = 'mV'_


UV _ = 'uV'_


V _ = 'V'_

## Module contents
@Project ：pythonProject_power_control @File ：__init__.py.py @IDE ：PyCharm @Author ：厄运马马卡 @Date ：2024/3/29 9:35
