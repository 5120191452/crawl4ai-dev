---
title: "ark.ark_common.auxiliary_function package"
docname: "ark.ark_common.auxiliary_function"
source: "http://orion.longsys.com/ark.ark_common.auxiliary_function.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_common.auxiliary_function package
## Submodules
## ark.ark_common.auxiliary_function.common_function module

ark.ark_common.auxiliary_function.common_function.get_enum_member_by_value(_enum_value_ , _enum_class_ , _logger_)

## ark.ark_common.auxiliary_function.system_auxiliary module
@Project ：OrionProject @File ：system_auxiliary.py @IDE ：PyCharm @Author ：lu @Date ：2024/5/20 16:01

_class _ark.ark_common.auxiliary_function.system_auxiliary.Direction(_value_)

Bases: `Enum`
An enumeration.

read _ = 'read'_


write _ = 'Write'_


_class _ark.ark_common.auxiliary_function.system_auxiliary.DriverType(_value_)

Bases: `Enum`
Supported driver types

ark_driver _ = 'ark_driver'_


original_driver _ = 'original_driver'_


orion_driver _ = 'orion_driver'_


_class _ark.ark_common.auxiliary_function.system_auxiliary.LocalPlatformType

Bases: `object`

Android _ = 'Android'_


DM3720 _ = 'aarch64'_


Linux _ = 'Linux'_


Unknown _ = 'Unknown'_


Windows _ = 'Windows'_


_class _ark.ark_common.auxiliary_function.system_auxiliary.OperateType(_value_)

Bases: `Enum`
Supported driver types

protocol_based _ = 'protocol_based'_


system_based _ = 'system_based'_


_class _ark.ark_common.auxiliary_function.system_auxiliary.SystemAuxiliary(_* args_, _** kwargs_)

Bases: `object`

get_capacity(_device : str_) → Tuple[int | None, int | None]


get_device_speed(_device : str_) → dict | None


get_device_vid_pid(_device_)


get_driver_type()


get_local_platform_type()


get_logical_device(_device : str_) → List[str] | None


get_phy_device(_device : str_) → str | None


get_serial_number(_device : str_) → str | None


get_system_type()


normalize_device(_device : str_) → str | None


_class _ark.ark_common.auxiliary_function.system_auxiliary.SystemType(_value_)

Bases: `Enum`
Supported system types

Linux _ = 'Linux'_


Mac _ = 'Mac'_


Windows _ = 'Windows'_

## Module contents
