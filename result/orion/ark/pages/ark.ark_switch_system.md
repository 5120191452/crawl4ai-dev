---
title: "ark.ark_switch_system package"
docname: "ark.ark_switch_system"
source: "http://orion.longsys.com/ark.ark_switch_system.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_switch_system package
## Subpackages
  * [ark.ark_switch_system.switch_system package](ark.ark_switch_system.switch_system.md)
    * [Submodules](ark.ark_switch_system.switch_system.md#submodules)
    * [ark.ark_switch_system.switch_system.ark_switch_system_factory module](ark.ark_switch_system.switch_system.md#module-ark.ark_switch_system.switch_system.ark_switch_system_factory)
      * [`ArkSwitchSystemFactory`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_factory.ArkSwitchSystemFactory)
        * [`ArkSwitchSystemFactory.create_object()`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_factory.ArkSwitchSystemFactory.create_object)
    * [ark.ark_switch_system.switch_system.ark_switch_system_interface module](ark.ark_switch_system.switch_system.md#module-ark.ark_switch_system.switch_system.ark_switch_system_interface)
      * [`ArkSwitchSystemInterface`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_interface.ArkSwitchSystemInterface)
        * [`ArkSwitchSystemInterface.reboot_system()`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_interface.ArkSwitchSystemInterface.reboot_system)
        * [`ArkSwitchSystemInterface.switch_system()`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_interface.ArkSwitchSystemInterface.switch_system)
      * [`SystemType`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_interface.SystemType)
        * [`SystemType.Linux`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_interface.SystemType.Linux)
        * [`SystemType.Windows`](ark.ark_switch_system.switch_system.md#ark.ark_switch_system.switch_system.ark_switch_system_interface.SystemType.Windows)
    * [Module contents](ark.ark_switch_system.switch_system.md#module-ark.ark_switch_system.switch_system)


## Module contents
@Module : ark_switch_system
@Date : 2024/11/12 13:51
@Version : V1.0.1
The ark_switch_system component is designed to facilitate seamless switching between multiple operating systems on a single machine. It operates by configuring boot settings—typically through modifications to the GRUB bootloader or similar boot manager—allowing users to specify a target operating system and reboot directly into it.
