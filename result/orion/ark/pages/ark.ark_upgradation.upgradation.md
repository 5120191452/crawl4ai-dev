---
title: "ark.ark_upgradation.upgradation package"
docname: "ark.ark_upgradation.upgradation"
source: "http://orion.longsys.com/ark.ark_upgradation.upgradation.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_upgradation.upgradation package
## Subpackages
  * [ark.ark_upgradation.upgradation.base package](ark.ark_upgradation.upgradation.base.md)
    * [Submodules](ark.ark_upgradation.upgradation.base.md#submodules)
    * [ark.ark_upgradation.upgradation.base.ark_upgradation_base module](ark.ark_upgradation.upgradation.base.md#module-ark.ark_upgradation.upgradation.base.ark_upgradation_base)
      * [`ArkUpgradationBase`](ark.ark_upgradation.upgradation.base.md#ark.ark_upgradation.upgradation.base.ark_upgradation_base.ArkUpgradationBase)
        * [`ArkUpgradationBase.get_current_version()`](ark.ark_upgradation.upgradation.base.md#ark.ark_upgradation.upgradation.base.ark_upgradation_base.ArkUpgradationBase.get_current_version)
        * [`ArkUpgradationBase.get_upgrade_log()`](ark.ark_upgradation.upgradation.base.md#ark.ark_upgradation.upgradation.base.ark_upgradation_base.ArkUpgradationBase.get_upgrade_log)
        * [`ArkUpgradationBase.start_local_upgrade()`](ark.ark_upgradation.upgradation.base.md#ark.ark_upgradation.upgradation.base.ark_upgradation_base.ArkUpgradationBase.start_local_upgrade)
    * [Module contents](ark.ark_upgradation.upgradation.base.md#module-ark.ark_upgradation.upgradation.base)


## Submodules
## ark.ark_upgradation.upgradation.ark_upgradation_factory module
@Project :Orion_ark @File :ark_gradation_factory.py @IDE :PyCharm @Author :厄运马马卡 @Date :2024/6/12 11:56

_class _ark.ark_upgradation.upgradation.ark_upgradation_factory.ArkUpgradationFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_upgrade_type_)


Brief:

Creates and returns an upgrade object based on the provided upgrade type.

Parameters:

**upgrade_type** – The type of upgrade to be performed. This should be an instance of UpgradeType.

Returns:

An instance of the corresponding upgrade class, or None if the upgrade type is invalid.

_class _ark.ark_upgradation.upgradation.ark_upgradation_factory.UpgradeType(_value_)

Bases: `Enum`
An enumeration.

stm32_firmware _ = 'UpgradeType_stm32_firmware'_


system_image _ = 'UpgradeType_system_image'_


test_device_fw _ = 'UpgradeType_test_device_fw'_

## ark.ark_upgradation.upgradation.ark_upgradation_interface module
@Project :Orion_ark @File :ark_gradation_interface.py @IDE :PyCharm @Author :厄运马马卡 @Date :2024/6/12 11:57

_class _ark.ark_upgradation.upgradation.ark_upgradation_interface.ArkUpgradationInterface

Bases: `ABC`

_abstract _get_current_version()


Brief:

Get the current version number.

Returns:

current version number, if obtain fails, return None

_abstract _get_upgrade_log()


Brief:

Getting the upgrade log.

Returns:

Upgrade log string, if get failed, return None.

_abstract _start_local_upgrade(_local_package_path_ , _* args_, _dst =None_, _timeout =0_, _** kwargs_)


Brief:

starts a local upgrade process using the specified package.

Parameters:

  * **local_package_path** – the file path to the local upgrade package
  * **args** – additional positional arguments
  * **dst** – this can be a serial port, disk drive, etc.
  * **timeout** – when the function runs longer than this time, it is considered a timeout
  * **kwargs** – additional keyword arguments


Returns:

corresponding error code.
## Module contents
@Project :Orion_ark @File :__init__.py.py @IDE :PyCharm @Author :厄运马马卡 @Date :2024/6/12 11:47
