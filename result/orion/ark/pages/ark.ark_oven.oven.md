---
title: "ark.ark_oven.oven package"
docname: "ark.ark_oven.oven"
source: "http://orion.longsys.com/ark.ark_oven.oven.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_oven.oven package
## Submodules
## ark.ark_oven.oven.ark_oven_factory module

_class _ark.ark_oven.oven.ark_oven_factory.ArkOvenFactory(_* args_, _** kwargs_)

Bases: `object`
Responsible for controlling the oven. it dynamically selects the appropriate adapter based on the type of oven provided and delegates the temperature control and other related operations to the selected adapter.

create_object(_oven_type_)


Brief:

Initialising objects(based on temperature control equipment types)

Parameters:

**oven_type** – optional values in the OvenType enumeration class are supported

Returns:

Success returns the corresponding object, failure returns None.

_class _ark.ark_oven.oven.ark_oven_factory.OvenType(_value_)

Bases: `Enum`
Supported types are serial_3720, network_temp_chamber_zz, network_temp_chamber_sw, mock_temp_chamber

mock_temp_chamber _ = 'mock_temp_chamber'_


network_temp_chamber_sw _ = 'network_temp_chamber_sw'_


network_temp_chamber_zz _ = 'network_temp_chamber_zz'_


serial_3720 _ = 'serial_3720'_

## ark.ark_oven.oven.ark_oven_interface module

_class _ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface

Bases: `ABC`
Abstract class that declares an interface for the operation of oven.

_abstract _get_current_temp()


Brief:

Get the current temperature value in the test chamber.

Returns:

res: execution result (error returns the corresponding error code) current_temp: current test chamber temperature.

_abstract _get_door_state()


Brief:

Obtain the status of the temperature control device door

Returns:

res: execution result (error returns the corresponding error code) status: True means the door is open, False means the door is closed.

_abstract _get_fault_state()


Brief:

Obtain the fault/alarm status of temperature control equipment.

Returns:

res: execution result, 0 indicates success, non-0 indicates failure. fault_state: True means fault/alarm exists, False means normal. fault_details: fault/alarm details, returns None on failure.

_abstract _get_programs_temperature_data()


Brief:

Get all valid program groups and their segment configurations from the oven.

Returns:

res: execution result (0 indicates success, non-0 indicates failure). programs: list of valid program groups, each item is a dict:

```
[
    {
        "program_no": int,
        "segment_count": int,
        "segments": [
            {
                "segment": int,
                "temperature": float,   # ℃
                "humidity": float,      # %
                "hour": int,
                "minute": int,
                "second": int,
                "duration_seconds": int
            },
            ...
        ],
        "loop": {
            "group_loop_count": int,
            "group_link": int
        }
    },
    ...
]

```
Copy to clipboard
Returns None on failure.

_abstract _get_run_program_number()


Brief:

Get the program number of the current program running mode

Returns:

res: execution result (error returns the corresponding error code) number: Current running program number.

_abstract _get_run_state()


Brief:

Obtain the operating status of temperature control equipment

Returns:

res: execution result (error returns the corresponding error code) status: True represents running, False represents stopping.

_abstract _get_run_type()


Brief:

Obtain the operating type of temperature control equipment

Returns:

res: execution result (error returns the corresponding error code) status: True represents constant, False represents program.

_abstract _get_target_temp()


Brief:

Get the target temperature value in the test chamber.

Returns:

res: execution result (error returns the corresponding error code) target_temp: Target test chamber temperature.

_abstract _oven_connect(_addr_ , _baudrate =115200_, _bytesize =8_, _parity ='N'_, _stopbits =1_, _timeout =0.5_, _xonxoff =False_, _rtscts =False_, _write_timeout =None_, _dsrdtr =False_, _inter_byte_timeout =None_, _exclusive =None_)


Breif:

Establishing a communication link with related oven device(s).

Param:

please reference <https://pyserial.readthedocs.io/en/latest/pyserial_api.html>

Returns:

Success returns 0, failure returns an error code

_abstract _oven_disconnect()


Breif:

Disconnect from temperature control equipment.

_abstract _pause_oven(_action_)


Brief:

Pause or resume the temperature control equipment.

Parameters:

**action** – 0 to pause, 1 to resume.

Returns:

0 indicates success, non-0 indicates failure.

_abstract _run_oven(_run_type =OvenMode.constant_, _response_timeout =None_)


Breif:

Running temperature control equipment.

Parameters:

  * **run_type** – OvenMode.constant: Constant; OvenMode.program: Program
  * **response_timeout** – Specifies the maximum amount of time the function waits for a response from the temperature control device before timing out. None represents the default value for using the relevant communication protocol.


Returns:

0 means that the temperature control device is ran successfully, and the error returns the corresponding error code.

_abstract _set_run_program_number(_program_number =0_, _response_timeout =None_)


Brief:

Set the running program number

Parameters:

  * **program_number** – The program number to be set defaults to 0
  * **response_timeout** – Specifies the maximum amount of time the function waits for a response from the temperature control device before timing out. None represents the default value for using the relevant communication protocol.


Returns:

res: execution result (error returns the corresponding error code)

_abstract _set_target_temp(_targettemperature_ , _slope =0_, _slopetime =None_, _waittemperaturearrive =0_, _timeout =None_, _response_timeout =None_)


Brief:

Setting the temperature, the temperature control device will regulate the temperature in the test chamber until the set target temperature is reached.

Parameters:

  * **targettemperature** – Target temperature
  * **slope** – Indicates whether ramp temperature control is performed, 0 means no, 1 means yes.
  * **slopetime** – In case of ramp rate temperature control, set this parameter to indicate how long it takes to reach the target temperature, if the time is too short and the temperature rise is not completed by the arrival time, the temperature rise will be carried out at the highest rate of the temperature control device.
  * **waittemperaturearrive** – Indicates whether to wait for the temperature to be reached, 0 means no, 1 means yes.
  * **timeout** – If you need to wait for the temperature to arrive before responding, set the temperature timeout period.
  * **response_timeout** – Specifies the maximum amount of time the function waits for a response from the temperature control device before timing out. None represents the default value for using the relevant communication protocol.


Returns:

0 indicates success in setting temperature, non-0 indicates failure in setting temperature.

_abstract _set_temperature_cycle()


_abstract _stop_oven(_response_timeout =None_)


Breif:

Stopping temperature control equipment.

Parameters:

**response_timeout** – Specifies the maximum amount of time the function waits for a response from the temperature control device before timing out. None represents the default value for using the relevant communication protocol.

Returns:

0 means that the temperature control device is stopped successfully, and the error returns the corresponding error code.

_class _ark.ark_oven.oven.ark_oven_interface.FunctionAddress(_value_)

Bases: `Enum`
An enumeration.

door_state _ = 5297_


measured_temperature _ = 1117_


preset_final_temperature _ = 1131_


preset_temperature _ = 1114_


run_allow _ = 1107_


run_program_number _ = 1121_


run_state _ = 1108_


run_type _ = 1109_


set_program_number _ = 1443_


stop_allow _ = 1106_


_class _ark.ark_oven.oven.ark_oven_interface.OvenMode(_value_)

Bases: `Enum`
An enumeration.

constant _ = 1_


program _ = 0_

## Module contents
