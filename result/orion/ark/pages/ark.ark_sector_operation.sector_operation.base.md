---
title: "ark.ark_sector_operation.sector_operation.base package"
docname: "ark.ark_sector_operation.sector_operation.base"
source: "http://orion.longsys.com/ark.ark_sector_operation.sector_operation.base.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_sector_operation.sector_operation.base package
## Submodules
## ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base module
@Project ：OrionProject @File ：ark_sector_operation_base.py @IDE ：PyCharm @Author ：lu @Date ：2024/5/20 11:37

_class _ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base.ArkSectorOperationBase(_* args_, _** kwargs_)

Bases: [`ArkSectorOperationInterface`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface "ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface")
Abstract class that declares interfaces for the operation of sector.

device_close()


Brief:

Closes the currently opened device.

Returns:

bool Error code (0 if successful, non-zero if an error occurred).

device_open(_device_ , _mode_ , _direct_)


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

modify_operate_size_max(_operate_size_max_)


Brief:

Modifies the maximum operation size for the device.

Parameters:

**operate_size_max** – int The new maximum operation size to be set (KB).

Returns:

bool Error code (0 if successful, non-zero if an error occurred).

sector_erase(_sector_address_ , _erase_length_)


sector_read(_sector_address_ , _read_length_ , _buffer_)


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

sector_verify(_sector_address_ , _verify_length_ , _verify_data_)


sector_verify_fixed_data(_sector_address_ , _verify_length_ , _verify_data_type_)


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

sector_write(_sector_address_ , _write_length_ , _buffer_)


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

sector_write_fixed_data(_sector_address_ , _write_length_ , _write_data_type_)


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
## Module contents
@Project ：OrionProject @File ：__init__.py.py @IDE ：PyCharm @Author ：lu @Date ：2024/5/20 15:40
