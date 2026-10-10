---
title: "ark.ark_upgradation.upgradation.base package"
docname: "ark.ark_upgradation.upgradation.base"
source: "http://orion.longsys.com/ark.ark_upgradation.upgradation.base.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_upgradation.upgradation.base package
## Submodules
## ark.ark_upgradation.upgradation.base.ark_upgradation_base module
@Project :Orion_ark @File :ark_upgradation_base.py @IDE :PyCharm @Author :厄运马马卡 @Date :2024/6/12 11:55

_class _ark.ark_upgradation.upgradation.base.ark_upgradation_base.ArkUpgradationBase(_* args_, _** kwargs_)

Bases: [`ArkUpgradationInterface`](ark.ark_upgradation.upgradation.md#ark.ark_upgradation.upgradation.ark_upgradation_interface.ArkUpgradationInterface "ark.ark_upgradation.upgradation.ark_upgradation_interface.ArkUpgradationInterface")

get_current_version()


Brief:

Get the current version number.

Returns:

current version number, if obtain fails, return None

get_upgrade_log()


Brief:

Getting the upgrade log.

Returns:

Upgrade log string, if get failed, return None.

start_local_upgrade(_local_package_path_ , _* args_, _** kwargs_)


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
@Project :Orion_ark @File :__init__.py.py @IDE :PyCharm @Author :厄运马马卡 @Date :2024/6/12 11:54
