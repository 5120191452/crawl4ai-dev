---
title: "ark.ark_buffer package"
docname: "ark.ark_buffer"
source: "http://orion.longsys.com/ark.ark_buffer.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_buffer package
## Subpackages
  * [ark.ark_buffer.buffer package](ark.ark_buffer.buffer.md)
    * [Submodules](ark.ark_buffer.buffer.md#submodules)
    * [ark.ark_buffer.buffer.ark_buffer_factory module](ark.ark_buffer.buffer.md#module-ark.ark_buffer.buffer.ark_buffer_factory)
      * [`ArkBufferFactory`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_factory.ArkBufferFactory)
        * [`ArkBufferFactory.create_object()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_factory.ArkBufferFactory.create_object)
    * [ark.ark_buffer.buffer.ark_buffer_interface module](ark.ark_buffer.buffer.md#module-ark.ark_buffer.buffer.ark_buffer_interface)
      * [`ArkBufferInterface`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface)
        * [`ArkBufferInterface.compare()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.compare)
        * [`ArkBufferInterface.copy()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.copy)
        * [`ArkBufferInterface.fill_data()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.fill_data)
        * [`ArkBufferInterface.get_buf_addr()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_buf_addr)
        * [`ArkBufferInterface.get_byte()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_byte)
        * [`ArkBufferInterface.get_data()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_data)
        * [`ArkBufferInterface.get_ddword()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_ddword)
        * [`ArkBufferInterface.get_dword()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_dword)
        * [`ArkBufferInterface.get_size()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_size)
        * [`ArkBufferInterface.get_word()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.get_word)
        * [`ArkBufferInterface.print()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.print)
        * [`ArkBufferInterface.set_byte()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.set_byte)
        * [`ArkBufferInterface.set_ddword()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.set_ddword)
        * [`ArkBufferInterface.set_dword()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.set_dword)
        * [`ArkBufferInterface.set_word()`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.ArkBufferInterface.set_word)
      * [`BufferType`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.BufferType)
        * [`BufferType.ARKC_BUFFER`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.BufferType.ARKC_BUFFER)
        * [`BufferType.ORION_BUFFER`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.BufferType.ORION_BUFFER)
      * [`DataType`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType)
        * [`DataType.DATA_55AA`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_55AA)
        * [`DataType.DATA_ALL_55`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_ALL_55)
        * [`DataType.DATA_ALL_AA`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_ALL_AA)
        * [`DataType.DATA_ALL_ONE`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_ALL_ONE)
        * [`DataType.DATA_ALL_ZERO`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_ALL_ZERO)
        * [`DataType.DATA_DECREMENTAL`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_DECREMENTAL)
        * [`DataType.DATA_EXCEED`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_EXCEED)
        * [`DataType.DATA_FIXED`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_FIXED)
        * [`DataType.DATA_H2`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_H2)
        * [`DataType.DATA_INCREMENTAL`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_INCREMENTAL)
        * [`DataType.DATA_RANDOM`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_RANDOM)
        * [`DataType.DATA_SECTOR_ADDR`](ark.ark_buffer.buffer.md#ark.ark_buffer.buffer.ark_buffer_interface.DataType.DATA_SECTOR_ADDR)
    * [Module contents](ark.ark_buffer.buffer.md#module-ark.ark_buffer.buffer)


## Module contents
@Module : ark_buffer
@Date : 2024/06/27
@Version : V1.0.0
The “ark_buffer” module is responsible for buffer data operations. It allows users to fill data into specified areas of the buffer in a flexible manner, supporting random or fixed pattern data generation. In addition, it also provides data comparison, copying, and printing functions, as well as the ability to modify byte, word, and double-word data in the buffer.
