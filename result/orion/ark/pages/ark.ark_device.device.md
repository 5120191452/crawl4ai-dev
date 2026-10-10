---
title: "ark.ark_device.device package"
docname: "ark.ark_device.device"
source: "http://orion.longsys.com/ark.ark_device.device.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_device.device package
## Submodules
## ark.ark_device.device.ark_device_factory module

_class _ark.ark_device.device.ark_device_factory.ArkDeviceFactory

Bases: `object`
Responsible for controlling the ProtocolAdapt. it dynamically selects the appropriate adapter based on the type of ProtocolAdapt provided and delegates the Protocol type and other related operations to the selected adapter.

create_object(_device_type_)


Brief:

再想想是否需要

Returns:

Success returns the corresponding object, failure returns None.
## ark.ark_device.device.ark_device_interface module

_class _ark.ark_device.device.ark_device_interface.AccessMode(_value_)

Bases: `Enum`
An enumeration.

Auto _ = 'auto'_


Physical _ = 'physical'_


_class _ark.ark_device.device.ark_device_interface.ArkDeviceInterface(_device_)

Bases: `ABC`

_abstract _close(_handle_)


Brief:

Close the connection to the specified device.

Parameters:

**handle** – (obj) The device handle.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _cmdq_disable_rw(_handle_)


Brief:

Disable cmdq read/write.

Parameters:

**handle** – (obj) device handle.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _cmdq_enable_rw(_handle_ , _queue_depth =32_)


Brief:

Initializes a command queue read/write with the specified queue depth.

Parameters:

  * **handle** – (obj) device handle.
  * **queue_depth** – (int) The maximum number of commands that can be stored in the queue.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _cmdq_get_response(_handle_)


Brief:

Retrieves the response from the command queue.

Parameters:

**handle** – (obj) device handle.

Returns:

(tuple) A tuple containing:
error_code: (int) Error code (0 if successful, non-zero if an error occurred).
response: (list) List of completed command responses. Each response contains a unique id that corresponds to the one returned by the associated cmdq_send command, enabling accurate matching between requests and responses.
buffer: List[Union[ark_buffer, None]]:
>   * List length equals the number of completed commands.
>   * For READ commands: Contains the read buffer (ark_buffer).
>   * For WRITE commands: Contains None.
>


_abstract _cmdq_send(_handle_ , _address_ , _length_ , _buffer =None_, _is_read =True_, _priority =0_, _is_cache =True_, _is_optimize =True_, _rw_type ='DeviceRWType_Normal'_, _func_time_out_us =0_)


Brief:

Sends a command to the command queue with the specified parameter.

Parameters:

  * **handle** – (obj) device handle.
  * **address** – (int) The address from which to read the data.
  * **length** – (int) The number of bytes to read from the specified address.
  * **buffer** – (ark_buffer) Write buffer.
  * **is_read** – (bool) If it’s a read operation.
  * **is_cache** – (int) Whether to use caching, defaults to True.
  * **is_optimize** – (int) Whether perform reliable write, defaults to True.
  * **rw_type** –
(str) The type of transfer to use, defined by the DeviceRWType enum, defaults to DeviceRWType.Normal.value
class DeviceRWType(Enum):
> Single = “DeviceRWType_Single”
> Normal = “DeviceRWType_Normal”
> Multi = “DeviceRWType_Multi”
> More = “DeviceRWType_More”
  * **func_time_out_us** – (int) Timeout period of a single command, defaults to 0 (no timeout).


Returns:

(tuple) A tuple containing: error_code: (int) Error code (0 if successful, non-zero if an error occurred). id: (int) A unique id indicates this cmd.

_abstract _device_init(_handle_ , _mode ='DeviceInitModeType_normal'_, _transfer_type ='TransferType_Half_Duplex'_, _link_up_time_out_us =0_, _func_time_out_us =0_, _is_continue_when_error =False_)


Brief:

Initializes the device with the given settings.

Parameters:

  * **handle** – (obj) device handle.
  * **mode** –
(str) The initialization mode, defined by DeviceInitModeType enum, defaults to normal mode (DeviceInitModeType.normal.value).
class DeviceInitModeType(Enum):
> normal = “DeviceInitModeType_normal”
> boot = “DeviceInitModeType_boot”
  * **transfer_type** –
(str) The transfer type, defined by TransferType enum, defaults to Half_Duplex mode (TransferType.Half_Duplex.value).
class TransferType(Enum):
> Half_Duplex = “TransferType_Half_Duplex”
> Full_Duplex = “TransferType_Full_Duplex”
  * **link_up_time_out_us** – (int) The timeout duration for communication with the upstream device (up).
  * **func_time_out_us** – (int) The timeout duration for function execution, defaults to 0 (no timeout).
  * **is_continue_when_error** – Whether to continue execution when an error occurs.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _erase(_handle_ , _Multisegment_data_ , _erase_type ='DeviceEraseType_Erase'_, _func_time_out_us =0_, _is_continue_when_error =False_)


Brief:

Erases data from the device based on the provided segment data.

Parameters:

  * **handle** – (obj) device handle.
  * **Multisegment_data** – (list) The multi-segment data list that specifies the regions to be erased, the list contains one or more tuple: [(address, length), ].
  * **erase_type** –
(str) The type of erase operation to perform, defined by the DeviceEraseType enum, defaults to DeviceEraseType.Erase.value
DeviceEraseType(Enum):
> Erase = “DeviceEraseType_Erase”
> Discard = “DeviceEraseType_Discard”
> SecureErase = “DeviceEraseType_SecureErase”
> Trim = “DeviceEraseType_Trim”
  * **func_time_out_us** – (int) Timeout for the read function, defaults to 0 (no timeout).
  * **is_continue_when_error** – (int) Whether to continue execution when an error occurs, defaults to False.


:return:(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _erase_all(_handle_ , _erase_type ='DeviceEraseType_Erase'_)


Brief:

Erases all data from the device.

Parameters:

  * **handle** – (obj) device handle.
  * **erase_type** –
(str) The type of erase operation to perform, defined by the DeviceEraseType enum, defaults to DeviceEraseType.Erase.value
DeviceEraseType(Enum):
> Erase = “DeviceEraseType_Erase”
> Discard = “DeviceEraseType_Discard”
> SecureErase = “DeviceEraseType_SecureErase”
> Trim = “DeviceEraseType_Trim”


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _get_device_log(_handle_ , _log_type_ , _output_dir =None_)


Brief:

Retrieve specific type of device log.

Parameters:

  * **handle** – (obj) Device handle.
  * **log_type** –
(DeviceLogType) Type of device log to retrieve. Defined by the DeviceLogType enum.
class DeviceLogType(Enum):
> Telemetry = “DeviceLogType_Telemetry”
  * **output_dir** –
(str) Optional output directory.
    * If provided:
> Must be an absolute directory path.
> The method generates a file name automatically based on the log type
> and timestamp.
    * If not provided:
> A dedicated directory named after the log type will be created under
> the current working directory.
The file extension of the generated log depends on the log type
(e.g., telemetry may produce .bin or .txt depending on device and format).


Returns:

(tuple) A tuple containing:
error_code: (int) 0 if successful, non-zero if an error occurred.
file_path: (str) Full path to the generated device log file.

_abstract _get_ecc_info(_handle_ , _block_start =0_, _block_end =0_, _page_step =0_, _mode =0_, _re_read =False_, _max_ecc_error_bit =41_, _skip_block =None_, _status_callback =None_)


Brief:

Reads ECC (Error Correction Code) data from the device.

Parameters:

  * **handle** – (obj) Device handle.
  * **block_start** – (int, optional) The starting block number for the ECC scan. Defaults to 0.
  * **block_end** – (int, optional) The ending block number for the ECC scan. Defaults to 0, which means scanning until the last block of the device.
  * **page_step** – (int, optional) The number of pages to read in each step. Defaults to 0 (uses the default step).
  * **mode** – (int, optional) Block-level scan mode: 0: Full Read (reads SLC and TLC block). 1: Only SLC. 2: Only TLC.
  * **re_read** – (bool, optional) Whether to enable re-read logic; this parameter is passed to the underlying interface.
  * **max_ecc_error_bit** – (int, optional) The ECC error bit threshold; this parameter is passed to the underlying interface. Defaults to 41.
  * **skip_block** – (list, optional) A list of block numbers to be skipped during the process.
  * **status_callback** – (callable, optional) Callback invoked during execution to report the current execution status.The callback receives an ExecutionStatus instance, which currently contains progress information and may be extended in the future. When the callback returns False, the library will stop the current task and exit gracefully. The callback should be non-blocking and lightweight.


Returns:

(tuple) A tuple containing: (int) Error code (0 if successful, non-zero if an error occurred). (bytearray) ECC data.

_abstract _get_info(_handle_ , _info_type =None_)


Brief:

Retrieve specific type of information from the device.

Parameters:

  * **handle** – (obj) Device handle.
  * **info_type** –
(DeviceInfoType, optional) Type of information to retrieve, defined by the DeviceInfoType enum.
Defaults to None, which returns all available information.
DeviceInfoType(Enum):
> Basic = “DeviceInfoType_Basic”
> Speed = “DeviceInfoType_Speed”
> FW = “DeviceInfoType_FW”
> STDSmart = “DeviceInfoType_STDSmart”
> VUSmart = “DeviceInfoType_VUSmart”
Usage example: DeviceInfoType.Basic.value


Returns:

(dataclass) Dataclass containing device information structured according to the specified info_type:
  * When info_type is DeviceInfoType.Basic.value:
> {
>> “physical_drive”: str, # Physical drive path (e.g., ‘\\.PHYSICALDRIVE1’ or ‘/dev/sdb’)
>> ”logical_drives”: List[str], # Logical drive paths (e.g., [‘C:’, ‘D:’] or [‘/dev/sdb1’])
>> ”sector_size”: int, # Sector size in bytes
>> ”total_sectors”: int, # Total number of sectors
>> ”serial_number”: str # Device serial number
> }
  * When info_type is DeviceInfoType.Speed.value:
> {
>> “port_speed”: str, # Port speed information
>> ”device_speed”: str, # Device speed information
>> ”connection_speed”: str # Connection speed information
> }
  * When info_type is DeviceInfoType.FW.value:
> {
>> “ctrl_name”: str, # Controller name
> }
  * When info_type is DeviceInfoType.STDSmart.value or DeviceInfoType.VUSmart.value:


Returns real-time device-specific SMART data structures (content varies by product model).
  * When info_type is None:


Returns all supported info_types.

_abstract _init(_power_obj =None_)


Brief:

Pass the corresponding component of the device to the device component.

Parameters:

**power_obj** – (obj): power object corresponding to the device

Returns:

None

_abstract _open(_device_ , _access_mode ='physical'_)


Brief:

Opens a connection to the specified device.

Parameters:

  * **device** – device (str): The identifier or path of the device to be opened.
  * **access_mode** – (str) The access mode to use, defined by enum AccessMode. Defaults to AccessMode.Physical.value. Physical: always normalize to physical device. Auto: keep the input device format.


Returns:

(obj) The handle of the device.

_abstract _read(_handle_ , _address_ , _length_ , _rw_type ='DeviceRWType_Normal'_, _is_cache =True_, _is_optimize =True_, _func_time_out_us =0_, _is_continue_when_error =False_, _* args_, _** kwargs_)


Brief:

Reads data from the device at the specified address and length.

Parameters:

  * **handle** – (obj) device handle.
  * **address** – (int) The address from which to read the data.
  * **length** – (int) The number of bytes to read from the specified address.
  * **rw_type** –
(str) The type of transfer to use, defined by the DeviceRWType enum, defaults to DeviceRWType.Normal.value
class DeviceRWType(Enum):
> Single = “DeviceRWType_Single”
> Normal = “DeviceRWType_Normal”
> Multi = “DeviceRWType_Multi”
> More = “DeviceRWType_More”
  * **is_cache** – (int) Whether to cache the read data, defaults to True.
  * **is_optimize** – (int) Whether to optimize the read operation, defaults to True.
  * **func_time_out_us** – (int) Timeout for the read function, defaults to 0 (no timeout).
  * **is_continue_when_error** – (int) Whether to continue execution when an error occurs, defaults to False.
  * **args** – Additional positional arguments.
  * **kwargs** – Additional keyword arguments.


Returns:

(tuple) A tuple containing: error_code: (int) Error code (0 if successful, non-zero if an error occurred). read_buffer: (ark_buffer) Read buffer. exec_time_us: (int) Transfer time.

_abstract _reset(_handle_ , _reset_type_)


Brief:

Resets the device to a known state based on the reset type.

Parameters:

  * **handle** – (obj) Device handle.
  * **reset_type** –
(str) The type of reset to perform, defined by DeviceResetType Enum:
DeviceResetType(Enum):
> PowerOnReset = “DeviceResetType_PowerOnReset”
> SoftwareReset = “DeviceResetType_SoftwareReset”
> HardwareReset = “DeviceResetType_HardwareReset”
> LinkReset = “DeviceResetType_LinkReset”
> LogicalUnitReset = “DeviceResetType_LogicalUnitReset”
Supported Reset Types by Product:
>     * UDisk:
>>       * PowerOnReset
>>       * LinkReset
>     * eMMC:
>>       * PowerOnReset
>>       * SoftwareReset (CMD0)
>>       * HardwareReset


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

Note:

  * Not all devices support all reset types.
  * Attempting an unsupported reset type may result in an error.


_abstract _sleep(_handle_ , _sleep_type_)


Brief:

Puts the device into a specified sleep or wake state based on power management settings.

Parameters:

  * **handle** – (obj) Device handle.
  * **sleep_type** –
(str) The target power management state, defined by DeviceSleepType Enum.
class DeviceSleepType(Enum):
> WakeUp = “DeviceSleepType_WakeUp”
> First = “DeviceSleepType_First”
> Second = “DeviceSleepType_Second”
> Third = “DeviceSleepType_Third”
> Fourth = “DeviceSleepType_Fourth”
> Fifth = “DeviceSleepType_Fifth”
> Sixth = “DeviceSleepType_Sixth”
Supported Sleep Types by Product:
>     * UDisk:
>>       * WakeUp (U0)
>>       * First (U1)
>>       * Second (U2)
>     * eMMC:
>>       * WakeUp
>>       * All other sleep types will be treated as CMD5 Sleep.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

Note:

  * Not all devices support all sleep types.


_abstract _speed(_handle_ , _speed_type_ , _bus_width ='DeviceBusWidth_8'_, _reference_clock =None_)


Brief:

Sets the device or system speed based on the specified speed type.

Parameters:

  * **handle** – (obj) Device handle.
  * **speed_type** –
(str) The gear or speed level to set, defined by DeviceSpeedType Enum:
class DeviceSpeedType(Enum):
> First = “DeviceSpeedType_First”
> Second = “DeviceSpeedType_Second”
> Third = “DeviceSpeedType_Third”
> Fourth = “DeviceSpeedType_Fourth”
> Fifth = “DeviceSpeedType_Fifth”
> Sixth = “DeviceSpeedType_Sixth”
> Seventh = “DeviceSpeedType_Seventh”
> Eighth = “DeviceSpeedType_Eighth”
> Ninth = “DeviceSpeedType_Ninth”
Supported Speed Types by Product:
>     * UDisk:
>>       * Speed switching is currently not supported.
>     * eMMC:
>>       * Supports the following speed types:
>>>         * First (HS_SDR)
>>>         * Second (HS_DDR)
>>>         * Third (HS200)
>>>         * Fourth (HS400)
>>       * Any other SpeedType value will be automatically mapped to “Fourth”.
  * **bus_width** –
(int) The bus width to use, defined by DeviceBusWidth Enum:
class DeviceBusWidth(Enum):
> BUS_WIDTH_1 = “DeviceBusWidth_1”
> BUS_WIDTH_2 = “DeviceBusWidth_2”
> BUS_WIDTH_4 = “DeviceBusWidth_4”
> BUS_WIDTH_8 = “DeviceBusWidth_8”
> BUS_WIDTH_16 = “DeviceBusWidth_16”
> BUS_WIDTH_32 = “DeviceBusWidth_32”
Supported Bus Width by Product:
>     * UDisk:
>>       * Bus width switching is currently not supported.
>     * eMMC:
>>       * Supports:
>>>         * BUS_WIDTH_1
>>>         * BUS_WIDTH_4
>>>         * BUS_WIDTH_8
>>       * If the selected bus width is incompatible with the chosen speed type, it will be automatically set to BUS_WIDTH_8.
  * **reference_clock** – (int) Reference clock frequency (in MHz). Optional.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

Note:

  * Not all devices support all speed types or bus widths.
  * Using unsupported settings may result in an error.


_abstract _switch_driver_type(_handle_ , _driver_type =None_)


Brief:

Switches the driver type for the specified device.

Parameters:

  * **handle** – (obj) Device handle.
  * **driver_type** – (str or None) The type of driver to switch to. If None, the driver type will be read from ark config.


Returns:

(obj) The handle of the device.

_abstract _switch_transfer_type(_handle_ , _transfer_type =None_)


Brief:

Switches the transfer type for the specified device.

Parameters:

  * **handle** – (obj) Device handle.
  * **transfer_type** – (str or None) The type of transfer to switch to. It should be a valid transfer type identifier. If None, the transfer type will be read from ark config.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _update_fireware(_handle_ , _file_path_)


Brief:

Updates the firmware of the device using the provided file path.

Parameters:

  * **handle** – (obj) device handle.
  * **file_path** – The path to the firmware file that needs to be updated.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

_abstract _write(_handle_ , _address_ , _length_ , _buffer =None_, _rw_type ='DeviceRWType_Normal'_, _is_cache =True_, _is_optimize =True_, _func_time_out_us =0_, _is_continue_when_error =False_, _* args_, _** kwargs_)


Brief:

Writes data to the device at the specified address.

Parameters:

  * **handle** – (obj) device handle.
  * **address** – (int) The address from which to read the data.
  * **length** – (int) The number of bytes to read from the specified address.
  * **buffer** – (ark_buffer) Write buffer.
  * **rw_type** –
(str) The type of transfer to use, defined by the DeviceRWType enum, defaults to DeviceRWType.Normal.value
class DeviceRWType(Enum):
> Single = “DeviceRWType_Single”
> Normal = “DeviceRWType_Normal”
> Multi = “DeviceRWType_Multi”
> More = “DeviceRWType_More”
  * **is_cache** – (int) Whether to cache the read data, defaults to True.
  * **is_optimize** – (int) Whether to optimize the read operation, defaults to True.
  * **func_time_out_us** – (int) Timeout for the read function, defaults to 0 (no timeout).
  * **is_continue_when_error** – (int) Whether to continue execution when an error occurs, defaults to False.
  * **args** – Additional positional arguments.
  * **kwargs** – Additional keyword arguments.


Returns:

(tuple) A tuple containing: error_code: (int) Error code (0 if successful, non-zero if an error occurred). exec_time_us: (int) Transfer time.

_class _ark.ark_device.device.ark_device_interface.DeviceBusWidth(_value_)

Bases: `Enum`
An enumeration.

BUS_WIDTH_1 _ = 'DeviceBusWidth_1'_


BUS_WIDTH_16 _ = 'DeviceBusWidth_16'_


BUS_WIDTH_2 _ = 'DeviceBusWidth_2'_


BUS_WIDTH_32 _ = 'DeviceBusWidth_32'_


BUS_WIDTH_4 _ = 'DeviceBusWidth_4'_


BUS_WIDTH_8 _ = 'DeviceBusWidth_8'_


_class _ark.ark_device.device.ark_device_interface.DeviceEraseType(_value_)

Bases: `Enum`
An enumeration.

Discard _ = 'DeviceEraseType_Discard'_


Erase _ = 'DeviceEraseType_Erase'_


SecureErase _ = 'DeviceEraseType_SecureErase'_


Trim _ = 'DeviceEraseType_Trim'_


_class _ark.ark_device.device.ark_device_interface.DeviceInfo(_basic: ark.ark_device.device.ark_device_interface.DeviceInfo_Basic = <factory>_, _speed: ark.ark_device.device.ark_device_interface.DeviceInfo_Speed = <factory>_, _fw: ark.ark_device.device.ark_device_interface.DeviceInfo_FW = <factory>_, _std_smart: Optional[Any] = None_, _vu_smart: Optional[Any] = None_)

Bases: `object`

basic _: [DeviceInfo_Basic](ark.ark_device.device.md#ark.ark_device.device.ark_device_interface.DeviceInfo_Basic "ark.ark_device.device.ark_device_interface.DeviceInfo_Basic")_


fw _: [DeviceInfo_FW](ark.ark_device.device.md#ark.ark_device.device.ark_device_interface.DeviceInfo_FW "ark.ark_device.device.ark_device_interface.DeviceInfo_FW")_


speed _: [DeviceInfo_Speed](ark.ark_device.device.md#ark.ark_device.device.ark_device_interface.DeviceInfo_Speed "ark.ark_device.device.ark_device_interface.DeviceInfo_Speed")_


std_smart _: Any | None_ _ = None_


vu_smart _: Any | None_ _ = None_


_class _ark.ark_device.device.ark_device_interface.DeviceInfoType(_value_)

Bases: `Enum`
An enumeration.

Basic _ = 'DeviceInfoType_Basic'_


FW _ = 'DeviceInfoType_FW'_


STDSmart _ = 'DeviceInfoType_STDSmart'_


Speed _ = 'DeviceInfoType_Speed'_


VUSmart _ = 'DeviceInfoType_VUSmart'_


_class _ark.ark_device.device.ark_device_interface.DeviceInfo_Basic(_physical_drive: Optional[str] = None_, _logical_drives: List[str] = <factory>_, _sector_size: Optional[int] = None_, _total_sectors: Optional[int] = None_, _serial_number: Optional[str] = None_)

Bases: `object`

logical_drives _: List[str]_


physical_drive _: str | None_ _ = None_


sector_size _: int | None_ _ = None_


serial_number _: str | None_ _ = None_


total_sectors _: int | None_ _ = None_


_class _ark.ark_device.device.ark_device_interface.DeviceInfo_FW(_ctrl_name : str | None = None_)

Bases: `object`

ctrl_name _: str | None_ _ = None_


_class _ark.ark_device.device.ark_device_interface.DeviceInfo_Speed(_port_maximum_speed : str | None = None_, _device_maximum_speed : str | None = None_, _device_connection_speed : str | None = None_, _raw_speed : dict | None = None_)

Bases: `object`

device_connection_speed _: str | None_ _ = None_


device_maximum_speed _: str | None_ _ = None_


port_maximum_speed _: str | None_ _ = None_


raw_speed _: dict | None_ _ = None_


_class _ark.ark_device.device.ark_device_interface.DeviceInitModeType(_value_)

Bases: `Enum`
An enumeration.

boot _ = 'DeviceInitModeType_boot'_


normal _ = 'DeviceInitModeType_normal'_


_class _ark.ark_device.device.ark_device_interface.DeviceLogType(_value_)

Bases: `Enum`
An enumeration.

Telemetry _ = 'DeviceLogType_Telemetry'_


_class _ark.ark_device.device.ark_device_interface.DeviceRWType(_value_)

Bases: `Enum`
An enumeration.

More _ = 'DeviceRWType_More'_


Multi _ = 'DeviceRWType_Multi'_


Normal _ = 'DeviceRWType_Normal'_


Single _ = 'DeviceRWType_Single'_


_class _ark.ark_device.device.ark_device_interface.DeviceResetType(_value_)

Bases: `Enum`
An enumeration.

HardwareReset _ = 'DeviceResetType_HardwareReset'_


LinkReset _ = 'DeviceResetType_LinkReset'_


LogicalUnitReset _ = 'DeviceResetType_LogicalUnitReset'_


PowerOnReset _ = 'DeviceResetType_PowerOnReset'_


SoftwareReset _ = 'DeviceResetType_SoftwareReset'_


_class _ark.ark_device.device.ark_device_interface.DeviceSleepType(_value_)

Bases: `Enum`
An enumeration.

Fifth _ = 'DeviceSleepType_Fifth'_


First _ = 'DeviceSleepType_First'_


Fourth _ = 'DeviceSleepType_Fourth'_


Second _ = 'DeviceSleepType_Second'_


Sixth _ = 'DeviceSleepType_Sixth'_


Third _ = 'DeviceSleepType_Third'_


WakeUp _ = 'DeviceSleepType_WakeUp'_


_class _ark.ark_device.device.ark_device_interface.DeviceSpeedType(_value_)

Bases: `Enum`
An enumeration.

Eighth _ = 'DeviceSpeedType_Eighth'_


Fifth _ = 'DeviceSpeedType_Fifth'_


First _ = 'DeviceSpeedType_First'_


Fourth _ = 'DeviceSpeedType_Fourth'_


Ninth _ = 'DeviceSpeedType_Ninth'_


Second _ = 'DeviceSpeedType_Second'_


Seventh _ = 'DeviceSpeedType_Seventh'_


Sixth _ = 'DeviceSpeedType_Sixth'_


Third _ = 'DeviceSpeedType_Third'_


_class _ark.ark_device.device.ark_device_interface.DeviceType(_value_)

Bases: `Enum`
An enumeration.

EMMC _ = 'DeviceType_EMMC'_


SD _ = 'DeviceType_SD'_


Udisk _ = 'DeviceType_UDisk'_


_class _ark.ark_device.device.ark_device_interface.ExecutionStatus(_progress : int_)

Bases: `object`

progress _: int_


_class _ark.ark_device.device.ark_device_interface.Hibernation_level(_value_)

Bases: `Enum`
An enumeration.

Level_1 _ = 'Level_1'_


Level_2 _ = 'Level_2'_


Level_3 _ = 'Level_3'_


_class _ark.ark_device.device.ark_device_interface.TransferType(_value_)

Bases: `Enum`
An enumeration.

Full_Duplex _ = 'TransferType_Full_Duplex'_


Half_Duplex _ = 'TransferType_Half_Duplex'_

## Module contents
