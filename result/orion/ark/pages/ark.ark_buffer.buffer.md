---
title: "ark.ark_buffer.buffer package"
docname: "ark.ark_buffer.buffer"
source: "http://orion.longsys.com/ark.ark_buffer.buffer.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_buffer.buffer package
## Submodules
## ark.ark_buffer.buffer.ark_buffer_factory module

_class _ark.ark_buffer.buffer.ark_buffer_factory.ArkBufferFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_size_ , _buffer_type =BufferType.ARKC_BUFFER_)

## ark.ark_buffer.buffer.ark_buffer_interface module

_class _ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface(_size_)

Bases: `ABC`

_abstract _compare(_offset_ , _buf_ , _src_offset_ , _size_ , _record_data =False_)

@brief: Compares the data in a specified region with a given buffer.
@param offset: The starting offset (in bytes) of the region to compare. @param buf: The destination buffer to compare against. @param src_offset: The offset (in bytes) within the destination buffer to start comparison. @param size: The size (in bytes) of the region to compare. @param record_data: Whether to record buf data when the comparison fails
@return: 0 is Pass, other is Failed

_abstract _copy(_offset_ , _buf_ , _src_offset_ , _size_)

@brief: Copies data from the given buffer into this object.
@param offset: The starting offset (in bytes) in this object where data will be written. @param buf: The source buffer to copy data from. @param src_offset: The starting offset (in bytes) in the source buffer from which to copy data. @param size: The length of data (in bytes) to copy.
@return: 0 is Pass, other is Failed

_abstract _fill_data(_dw_offset_ , _dw_length_ , _b_type_ , _w_blk_size =512_, _b_cycle =0_, _dw_cycle =0_, _ddw_addr =0_, _ddw_random_seed =1_, _fixed_data =0_)

@brief: Fill buffer with data of the specified type.
Note: Parameter name prefixes (dw_, ddw_, b_, w_) are residual from C code and do not impose type constraints in Python.
@param dw_offset: Start offset (in bytes) of filling in the buffer. @param dw_length: Length (in bytes) of the buffer region to fill. @param b_type: Data type to fill, defined by the DataType enumeration:
>
```
class DataType(Enum):
    DATA_ALL_ZERO = 0
    DATA_ALL_ONE = 1
    DATA_ALL_AA = 2
    DATA_ALL_55 = 3
    DATA_INCREMENTAL = 4
    DATA_RANDOM = 5
    DATA_55AA = 6
    DATA_SECTOR_ADDR = 7
    DATA_FIXED = 8
    DATA_DECREMENTAL = 9
    DATA_H2 = 10
    DATA_EXCEED = auto()

```
Copy to clipboard
@param w_blk_size: (Optional) Sector size. Default is 512.
>   * When b_type is DATA_SECTOR_ADDR, each w_blk_size region is filled with the corresponding sector address data.
>   * When b_cycle is set, cycle count filling is performed in repeated chunks of size w_blk_size. In each chunk, the first 8 bytes are filled with dw_cycle, and the remaining bytes are filled according to b_type.
>

@param b_cycle: (Optional) Enable cycle count filling by w_blk_size. Default is 0 (disabled). @param dw_cycle: (Optional) Value used when b_cycle is enabled; placed in the first 8 bytes of each w_blk_size chunk. Default is 0. @param ddw_addr: (Optional) Starting address when filling DATA_SECTOR_ADDR type data. Default is 0. @param ddw_random_seed: (Optional) Seed used when filling DATA_RANDOM type data. Default is 1. @param fixed_data: (Optional) Value used when filling DATA_FIXED type data. Must be within 8 bytes. Default is 0.
@return: Error code.

_abstract _get_buf_addr()

@brief: Retrieves the address of the internal buffer or data storage used by the object.

@return: The address of the internal buffer or data storage, typically as an integer.

Note: Direct access to this address may not be safe or appropriate for all objects.

_abstract _get_byte(_offset_ , _is_little_endian =True_)

@brief: Retrieves a byte from a specified offset in the object.
@param offset: The offset (in bytes) from which to retrieve the byte. @param is_little_endian: (Optional) Indicates whether the data should be interpreted as little-endian, default is True. False indicates big-endian format.
@return: The byte retrieved from the specified offset.

_abstract _get_data(_offset =0_, _size =0_)

@brief: Retrieves the data currently stored in the object.
@param offset: (Optional) The starting offset (in bytes) of the region to get, default is 0. @param size: (Optional) The size (in bytes) of the region to get, default is 0 (get until end).
@return: The data or a representation of the data stored within the object.

_abstract _get_ddword(_offset_ , _is_little_endian =True_)

@brief: Retrieves a ddword (multi-byte value) from a specified offset in the object.
@param offset: The offset (in bytes) from which to retrieve the ddword. @param is_little_endian: (Optional) Indicates whether the data should be interpreted as little-endian, default is True. False indicates big-endian format.
@return: The ddword (multi-byte value) retrieved from the specified offset.

_abstract _get_dword(_offset_ , _is_little_endian =True_)

@brief: Retrieves a dword (multi-byte value) from a specified offset in the object.
@param offset: The offset (in bytes) from which to retrieve the dword. @param is_little_endian: (Optional) Indicates whether the data should be interpreted as little-endian, default is True. False indicates big-endian format.
@return: The dword (multi-byte value) retrieved from the specified offset.

_abstract _get_size()

@brief: Get the size of the buffer.
@return: size (in bytes)

_abstract _get_word(_offset_ , _is_little_endian =True_)

@brief: Retrieves a word (multi-byte value) from a specified offset in the object.
@param offset: The offset (in bytes) from which to retrieve the word. @param is_little_endian: (Optional) Indicates whether the data should be interpreted as little-endian, default is True. False indicates big-endian format.
@return: The word (multi-byte value) retrieved from the specified offset.

_abstract _print(_offset =0_, _size =0_)

@brief: Prints the data in a specified region.
@param offset: (Optional) The starting offset (in bytes) of the region to print, default is 0. @param size: (Optional) The size (in bytes) of the region to print, default is 0 (prints until end).
@return: None (Abstract method, prints directly)

_abstract _set_byte(_offset_ , _data_ , _is_little_endian =True_)

@brief: Sets a byte at a specified offset in the object.
@param offset: The offset (in bytes) where the byte will be set. @param data: The byte to set. @param is_little_endian: (Optional) Indicates whether the data should be stored in little-endian format, default is True. False indicates big-endian format.
@return: 0 is Pass, other is Failed

_abstract _set_ddword(_offset_ , _data_ , _is_little_endian =True_)

@brief: Sets a ddword (multi-byte value) at a specified offset in the object.
@param offset: The offset (in bytes) where the ddword will be set. @param data: The ddword (multi-byte value) to set. @param is_little_endian: (Optional) Indicates whether the data should be stored in little-endian format, default is True. False indicates big-endian format.
@return: 0 is Pass, other is Failed

_abstract _set_dword(_offset_ , _data_ , _is_little_endian =True_)

@brief: Sets a dword (multi-byte value) at a specified offset in the object.
@param offset: The offset (in bytes) where the dword will be set. @param data: The dword (multi-byte value) to set. @param is_little_endian: (Optional) Indicates whether the data should be stored in little-endian format, default is True. False indicates big-endian format.
@return: 0 is Pass, other is Failed

_abstract _set_word(_offset_ , _data_ , _is_little_endian =True_)

@brief: Sets a word (multi-byte value) at a specified offset in the object.
@param offset: The offset (in bytes) where the word will be set. @param data: The word (multi-byte value) to set. @param is_little_endian: (Optional) Indicates whether the data should be stored in little-endian format, default is True. False indicates big-endian format.
@return: 0 is Pass, other is Failed

_class _ark.ark_buffer.buffer.ark_buffer_interface.BufferType(_value_)

Bases: `Enum`
An enumeration.

ARKC_BUFFER _ = 0_


ORION_BUFFER _ = 1_


_class _ark.ark_buffer.buffer.ark_buffer_interface.DataType(_value_)

Bases: `Enum`
An enumeration.

DATA_55AA _ = 6_


DATA_ALL_55 _ = 3_


DATA_ALL_AA _ = 2_


DATA_ALL_ONE _ = 1_


DATA_ALL_ZERO _ = 0_


DATA_DECREMENTAL _ = 9_


DATA_EXCEED _ = 11_


DATA_FIXED _ = 8_


DATA_H2 _ = 10_


DATA_INCREMENTAL _ = 4_


DATA_RANDOM _ = 5_


DATA_SECTOR_ADDR _ = 7_

## Module contents
