---
title: "ark.ark_sector_operation.sector_operation package"
docname: "ark.ark_sector_operation.sector_operation"
source: "http://orion.longsys.com/ark.ark_sector_operation.sector_operation.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_sector_operation.sector_operation package
## Subpackages
  * [ark.ark_sector_operation.sector_operation.base package](ark.ark_sector_operation.sector_operation.base.md)
    * [Submodules](ark.ark_sector_operation.sector_operation.base.md#submodules)
    * [ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base module](ark.ark_sector_operation.sector_operation.base.md#module-ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base)
      * [`ArkSectorOperationBase`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase)
        * [`ArkSectorOperationBase.device_close()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.device_close)
        * [`ArkSectorOperationBase.device_open()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.device_open)
        * [`ArkSectorOperationBase.modify_operate_size_max()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.modify_operate_size_max)
        * [`ArkSectorOperationBase.sector_erase()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.sector_erase)
        * [`ArkSectorOperationBase.sector_read()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.sector_read)
        * [`ArkSectorOperationBase.sector_verify()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.sector_verify)
        * [`ArkSectorOperationBase.sector_verify_fixed_data()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.sector_verify_fixed_data)
        * [`ArkSectorOperationBase.sector_write()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.sector_write)
        * [`ArkSectorOperationBase.sector_write_fixed_data()`](ark.ark_sector_operation.sector_operation.base.md#ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase.sector_write_fixed_data)
    * [Module contents](ark.ark_sector_operation.sector_operation.base.md#module-ark.ark_sector_operation.sector_operation.base)
  * [ark.ark_sector_operation.sector_operation.factory package](ark.ark_sector_operation.sector_operation.factory.md)
    * [Module contents](ark.ark_sector_operation.sector_operation.factory.md#module-ark.ark_sector_operation.sector_operation.factory)


## Submodules
## ark.ark_sector_operation.sector_operation.ark_sector_operation_factory module
@Project ：OrionProject @File ：ark_sector_operation_factory.py @IDE ：PyCharm @Author ：lu @Date ：2024/5/20 11:37

_class _ark.ark_sector_operation.sector_operation.ark_sector_operation_factory.ArkSectorOperationFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_operate_type_)

## ark.ark_sector_operation.sector_operation.ark_sector_operation_interface module

_class _ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface

Bases: `ABC`
Abstract class that declares interfaces for the operation of sector.

_abstract _device_close()


Brief:

Closes the currently opened device.

Returns:

bool Error code (0 if successful, non-zero if an error occurred).

_abstract _device_open(_device_ , _mode_ , _direct_)


Brief:

Opens a specified device with the given mode and direct access option.

Parameters:

  * **device** –
str The path of the device to be opened. example:
> On Windows:
>> device = ‘1’, device = ‘2’, device = ‘.PHYSICALDRIVE1’, device = ‘E:’, device = ‘E:' …
> On Linux:
>> device = ‘/dev/sdb’ …
  * **mode** –
str The mode in which to open the device
> example:
>> On Windows:
>>> mode = 2(GENERIC_READ and GENERIC_WRITE),
>>> mode = 0(GENERIC_READ),
>>> mode = 1(GENERIC_WRITE).
>> On Linux:
>>> mode = 2(os.O_RDWR),
>>> mode = 0(os.O_RDONLY),
>>> mode = 1(os.O_WRONLY).
  * **direct** –
bool
Whether to open the device with direct access (no buffering) or not.
>     * True: No buffering (direct access).
>     * False: Buffering (indirect access).


Returns:

bool Error code (0 if successful, non-zero if an error occurred).

_abstract _get_device_capacity()


Brief:

Get device’s capacity (in sectors) and sector size.

Returns:

tuple A tuple containing: - int: Error code (0 if successful, non-zero if an error occurred). - int: Device’s capacity (in sectors) if no error, else None. - int: Device’s sector size if no error, else None.

_abstract _get_device_info()


Brief:

Retrieves the sector size and capacity of the device.No need to explicitly call it, it will be called automatically when reading or writing without information such as sector size.

Returns:

bool Error code (0 if successful, non-zero if an error occurred).

_abstract _modify_operate_size_max(_operate_size_max_)


Brief:

Modifies the maximum operation size for the device.

Parameters:

**operate_size_max** – int The new maximum operation size to be set (KB).

Returns:

bool Error code (0 if successful, non-zero if an error occurred).

_abstract _sector_read(_sector_address_ , _read_length_ , _buffer_ , _max_chunk_size =4194304_, _buffer_offset =0_)


Brief:

Reads a specified number of sectors from a given sector address on the device.

Parameters:

  * **sector_address** – int The address of the sector to start reading from.
  * **read_length** – int The number of sectors to read from the specified sector address.
  * **buffer** – buffer object The read data will be put in this buffer, start at the buffer offset position
  * **max_chunk_size** – int Max read length per read.
  * **buffer_offset** – int The read data will be put in buffer start at the buffer_offset position.


Returns:

tuple A tuple containing: - int: Error code (0 if successful, non-zero if an error occurred). - int: Error offset if error, else sector_address + read_length.

_abstract _sector_verify_fixed_data(_sector_address_ , _verify_length_ , _verify_data_type_ , _max_chunk_size_)


Brief:

Verifies fixed-type data at a specified sector address on the device.

Parameters:

  * **sector_address** – int The address of the sector to verify.
  * **verify_length** – int The number of sectors to verify starting from the specified sector address.
  * **verify_data_type** –
DataType The type of data to be verify. Should be one of the members of the DataType enum.
class DataType(Enum):
> DATA_ALL_ZERO = 0
> DATA_ALL_ONE = 1
> DATA_ALL_AA = 2
> DATA_ALL_55 = 3
> DATA_INCREMENTAL = 4
> DATA_RANDOM = 5
> DATA_55AA = 6
> DATA_SECTOR_NUMBER = 7


Returns:

tuple A tuple containing: - int: Error code (0 if successful, non-zero if an error occurred). - int: Error offset if error, else sector_address + verify_length.

_abstract _sector_write(_sector_address_ , _write_length_ , _buffer_ , _max_chunk_size =4194304_, _buffer_offset =0_)


Brief:

Writes a specified number of sectors from a given sector address on the device.

Parameters:

  * **sector_address** – int The address of the sector to start writing to.
  * **write_length** – int The number of sectors to write to the specified sector address.
  * **buffer** – buffer object The data to be written to the device. The length of this data should match the specified write length.
  * **max_chunk_size** – int Max write length per write
  * **buffer_offset** – int The data written to the device will be start from the buffer_offset position of the buffer


Returns:

tuple A tuple containing: - int: Error code (0 if successful, non-zero if an error occurred). - int: Error offset if error, else sector_address + write_length.

_abstract _sector_write_fixed_data(_sector_address_ , _write_length_ , _write_data_type_ , _max_chunk_size_)


Brief:

Writes a specified number of sectors of fixed-type data to a given sector address on the device.

Parameters:

  * **sector_address** – int The address of the sector to start writing to.
  * **write_length** – int The number of sectors to write to the specified sector address.
  * **write_data_type** –
DataType The type of data to be written. Should be one of the members of the DataType enum.
class DataType(Enum):
> DATA_ALL_ZERO = 0
> DATA_ALL_ONE = 1
> DATA_ALL_AA = 2
> DATA_ALL_55 = 3
> DATA_INCREMENTAL = 4
> DATA_RANDOM = 5
> DATA_55AA = 6
> DATA_SECTOR_NUMBER = 7
  * **max_chunk_size** – int Max write length per write


Returns:

tuple A tuple containing: - int: Error code (0 if successful, non-zero if an error occurred). - int: Error offset if error, else sector_address + write_length.

_class _ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.OpenMode(_value_)

Bases: `Enum`
An enumeration.

ONLY_READ _ = 0_


ONLY_WRITE _ = 1_


READ_WRITE _ = 2_

## Module contents
