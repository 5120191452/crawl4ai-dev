---
title: "ark.ark_oven package"
docname: "ark.ark_oven"
source: "http://orion.longsys.com/ark.ark_oven.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_oven package
## Subpackages
  * [ark.ark_oven.oven package](ark.ark_oven.oven.md)
    * [Submodules](ark.ark_oven.oven.md#submodules)
    * [ark.ark_oven.oven.ark_oven_factory module](ark.ark_oven.oven.md#module-ark.ark_oven.oven.ark_oven_factory)
      * [`ArkOvenFactory`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.ArkOvenFactory)
        * [`ArkOvenFactory.create_object()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.ArkOvenFactory.create_object)
      * [`OvenType`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.OvenType)
        * [`OvenType.mock_temp_chamber`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.OvenType.mock_temp_chamber)
        * [`OvenType.network_temp_chamber_sw`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.OvenType.network_temp_chamber_sw)
        * [`OvenType.network_temp_chamber_zz`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.OvenType.network_temp_chamber_zz)
        * [`OvenType.serial_3720`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_factory.OvenType.serial_3720)
    * [ark.ark_oven.oven.ark_oven_interface module](ark.ark_oven.oven.md#module-ark.ark_oven.oven.ark_oven_interface)
      * [`ArkOvenInterface`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface)
        * [`ArkOvenInterface.get_current_temp()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_current_temp)
        * [`ArkOvenInterface.get_door_state()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_door_state)
        * [`ArkOvenInterface.get_fault_state()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_fault_state)
        * [`ArkOvenInterface.get_programs_temperature_data()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_programs_temperature_data)
        * [`ArkOvenInterface.get_run_program_number()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_run_program_number)
        * [`ArkOvenInterface.get_run_state()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_run_state)
        * [`ArkOvenInterface.get_run_type()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_run_type)
        * [`ArkOvenInterface.get_target_temp()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.get_target_temp)
        * [`ArkOvenInterface.oven_connect()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.oven_connect)
        * [`ArkOvenInterface.oven_disconnect()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.oven_disconnect)
        * [`ArkOvenInterface.pause_oven()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.pause_oven)
        * [`ArkOvenInterface.run_oven()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.run_oven)
        * [`ArkOvenInterface.set_run_program_number()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.set_run_program_number)
        * [`ArkOvenInterface.set_target_temp()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.set_target_temp)
        * [`ArkOvenInterface.set_temperature_cycle()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.set_temperature_cycle)
        * [`ArkOvenInterface.stop_oven()`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.ArkOvenInterface.stop_oven)
      * [`FunctionAddress`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress)
        * [`FunctionAddress.door_state`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.door_state)
        * [`FunctionAddress.measured_temperature`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.measured_temperature)
        * [`FunctionAddress.preset_final_temperature`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.preset_final_temperature)
        * [`FunctionAddress.preset_temperature`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.preset_temperature)
        * [`FunctionAddress.run_allow`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.run_allow)
        * [`FunctionAddress.run_program_number`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.run_program_number)
        * [`FunctionAddress.run_state`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.run_state)
        * [`FunctionAddress.run_type`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.run_type)
        * [`FunctionAddress.set_program_number`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.set_program_number)
        * [`FunctionAddress.stop_allow`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.FunctionAddress.stop_allow)
      * [`OvenMode`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.OvenMode)
        * [`OvenMode.constant`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.OvenMode.constant)
        * [`OvenMode.program`](ark.ark_oven.oven.md#ark.ark_oven.oven.ark_oven_interface.OvenMode.program)
    * [Module contents](ark.ark_oven.oven.md#module-ark.ark_oven.oven)


## Module contents
@Module : ark_oven
@Date : 2024/4/01 11:06
@Version : V1.0.0
The ‘ark_oven’ component encapsulates a comprehensive system for managing oven functionality within a broader application framework. At its core are two essential modules: ‘ark_oven_factory’ and ‘ark_oven_base’.
The ‘ark_oven_factory’ module embodies the Factory Pattern, serving as a central orchestrator for controlling oven operations dynamically. Its primary responsibility lies in selecting the appropriate adapter based on the type of oven provided.
On the other hand, the ‘ark_oven_base’ module functions as an abstract base class, laying down a standardized blueprint for implementing oven-related operations and functionalities. By encapsulating common interfaces for oven operations, it establishes a consistent framework for managing oven functionality across different implementations or subclasses.
Together, these modules form the backbone of the ‘ark_oven’ component, providing a robust and flexible solution for effectively managing oven operations within the broader application context.
