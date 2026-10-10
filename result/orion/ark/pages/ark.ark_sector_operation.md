---
title: "ark.ark_sector_operation package"
docname: "ark.ark_sector_operation"
source: "http://orion.longsys.com/ark.ark_sector_operation.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_sector_operation package
## Subpackages
  * [ark.ark_sector_operation.sector_operation package](ark.ark_sector_operation.sector_operation.md)
    * [Subpackages](ark.ark_sector_operation.sector_operation.md#subpackages)
      * [ark.ark_sector_operation.sector_operation.base package](ark.ark_sector_operation.sector_operation.base.md)
        * [Submodules](ark.ark_sector_operation.sector_operation.base.md#submodules)
        * [ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base module](ark.ark_sector_operation.sector_operation.base.md#module-ark.ark_sector_operation.sector_operation.base.ark_sector_operation_base)
        * [Module contents](ark.ark_sector_operation.sector_operation.base.md#module-ark.ark_sector_operation.sector_operation.base)
      * [ark.ark_sector_operation.sector_operation.factory package](ark.ark_sector_operation.sector_operation.factory.md)
        * [Module contents](ark.ark_sector_operation.sector_operation.factory.md#module-ark.ark_sector_operation.sector_operation.factory)
    * [Submodules](ark.ark_sector_operation.sector_operation.md#submodules)
    * [ark.ark_sector_operation.sector_operation.ark_sector_operation_factory module](ark.ark_sector_operation.sector_operation.md#module-ark.ark_sector_operation.sector_operation.ark_sector_operation_factory)
      * [`ArkSectorOperationFactory`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_factory.ArkSectorOperationFactory)
        * [`ArkSectorOperationFactory.create_object()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_factory.ArkSectorOperationFactory.create_object)
    * [ark.ark_sector_operation.sector_operation.ark_sector_operation_interface module](ark.ark_sector_operation.sector_operation.md#module-ark.ark_sector_operation.sector_operation.ark_sector_operation_interface)
      * [`ArkSectorOperationInterface`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface)
        * [`ArkSectorOperationInterface.device_close()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.device_close)
        * [`ArkSectorOperationInterface.device_open()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.device_open)
        * [`ArkSectorOperationInterface.get_device_capacity()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.get_device_capacity)
        * [`ArkSectorOperationInterface.get_device_info()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.get_device_info)
        * [`ArkSectorOperationInterface.modify_operate_size_max()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.modify_operate_size_max)
        * [`ArkSectorOperationInterface.sector_read()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.sector_read)
        * [`ArkSectorOperationInterface.sector_verify_fixed_data()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.sector_verify_fixed_data)
        * [`ArkSectorOperationInterface.sector_write()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.sector_write)
        * [`ArkSectorOperationInterface.sector_write_fixed_data()`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.ArkSectorOperationInterface.sector_write_fixed_data)
      * [`OpenMode`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.OpenMode)
        * [`OpenMode.ONLY_READ`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.OpenMode.ONLY_READ)
        * [`OpenMode.ONLY_WRITE`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.OpenMode.ONLY_WRITE)
        * [`OpenMode.READ_WRITE`](ark.ark_sector_operation.sector_operation.md#ark.ark_sector_operation.sector_operation.ark_sector_operation_interface.OpenMode.READ_WRITE)
    * [Module contents](ark.ark_sector_operation.sector_operation.md#module-ark.ark_sector_operation.sector_operation)


## Module contents
@Module : ark_sector_operation
@Date : 2024/5/20 11:34
@Version : V1.0.2
The “ark_sector_operation” component is designed to provide a unified set of interfaces to perform operations on device sectors across different operating systems and platforms, including but not limited to writing, reading, erasing, matching, etc.; this module is located under the business logic layer and can interact with the disk by calling the operating system interfaces or by using the relevant protocol interfaces provided by the self-modifying driver. This module is located under the business logic layer and can interact with the disk by calling the operating system interface or according to the relevant protocol interface provided by the driver.
The “ark_sector_operation_interface” module is the base class that implements sector-related operations and defines the related operation interfaces.
The “ark_sector_operation_factory” module is a factory class for sector-related operations, which creates different objects according to the type of the driver, etc., so that it is easy for the user to call it.
Together, these modules form the backbone of the “ark_sector_operation” component, providing the user with powerful and flexible methods for sector operations.

🐻@Version: 1.0.1 @update time: 2025/04/07 @Person Responsible: lu.zhang

ꔷ Add get_device_capacity interface.
