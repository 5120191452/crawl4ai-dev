---
title: "ark.ark_switch_system.switch_system package"
docname: "ark.ark_switch_system.switch_system"
source: "http://orion.longsys.com/ark.ark_switch_system.switch_system.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_switch_system.switch_system package
## Submodules
## ark.ark_switch_system.switch_system.ark_switch_system_factory module

_class _ark.ark_switch_system.switch_system.ark_switch_system_factory.ArkSwitchSystemFactory(_* args_, _** kwargs_)

Bases: `object`

create_object()

## ark.ark_switch_system.switch_system.ark_switch_system_interface module

_class _ark.ark_switch_system.switch_system.ark_switch_system_interface.ArkSwitchSystemInterface

Bases: `ABC`
Abstract class that declares interfaces for the switch system module.

_abstract _reboot_system()


Brief:

restart the computer

_abstract _switch_system(_system_type_)


Brief:

Switches the current operating system to xxx(such as linux) for the next boot.

Param:

system_type:Default system type for the next boot. example:
> SystemType.Windows SystemType.Linux

Returns:

int Returns 0 if successful operation of GRUB configuration file; otherwise, returns an error code.

_class _ark.ark_switch_system.switch_system.ark_switch_system_interface.SystemType(_value_)

Bases: `Enum`
An enumeration.

Linux _ = 'Linux'_


Windows _ = 'Windows'_

## Module contents
