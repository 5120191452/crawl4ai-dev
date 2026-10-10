---
title: "ark.ark_ssd package"
docname: "ark.ark_ssd"
source: "http://orion.longsys.com/ark.ark_ssd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_ssd package
## Subpackages
  * [ark.ark_ssd.ssd package](ark.ark_ssd.ssd.md)
    * [Submodules](ark.ark_ssd.ssd.md#submodules)
    * [ark.ark_ssd.ssd.ark_ssd_factory module](ark.ark_ssd.ssd.md#module-ark.ark_ssd.ssd.ark_ssd_factory)
      * [`ArkSSDFactory`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_factory.ArkSSDFactory)
        * [`ArkSSDFactory.create_object()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_factory.ArkSSDFactory.create_object)
    * [ark.ark_ssd.ssd.ark_ssd_interface module](ark.ark_ssd.ssd.md#module-ark.ark_ssd.ssd.ark_ssd_interface)
      * [`JudgeRule`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule)
        * [`JudgeRule.EQ`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule.EQ)
        * [`JudgeRule.GT`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule.GT)
        * [`JudgeRule.LT`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule.LT)
      * [`OutputFormat`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.OutputFormat)
        * [`OutputFormat.JSON`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.OutputFormat.JSON)
        * [`OutputFormat.TEXT`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.OutputFormat.TEXT)
      * [`SSDInterface`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface)
        * [`SSDInterface.nvme_dev_format()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_format)
        * [`SSDInterface.nvme_dev_get_all_nvme_list()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_all_nvme_list)
        * [`SSDInterface.nvme_dev_get_basic_info()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_basic_info)
        * [`SSDInterface.nvme_dev_get_controller_and_pci_address()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_controller_and_pci_address)
        * [`SSDInterface.nvme_dev_get_from_controller()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_from_controller)
        * [`SSDInterface.nvme_dev_get_identify_controller_info()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_identify_controller_info)
        * [`SSDInterface.nvme_dev_get_power_state()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_power_state)
        * [`SSDInterface.nvme_dev_get_sector_info()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_get_sector_info)
        * [`SSDInterface.nvme_dev_is_support_write_zeroes()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_is_support_write_zeroes)
        * [`SSDInterface.nvme_dev_set_power_state()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_dev_set_power_state)
        * [`SSDInterface.nvme_hw_device_remove()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_device_remove)
        * [`SSDInterface.nvme_hw_device_rescan()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_device_rescan)
        * [`SSDInterface.nvme_hw_disable_apst()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_disable_apst)
        * [`SSDInterface.nvme_hw_get_pcie_aspm()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_get_pcie_aspm)
        * [`SSDInterface.nvme_hw_get_pcie_l1pm_substates_cap()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_get_pcie_l1pm_substates_cap)
        * [`SSDInterface.nvme_hw_get_pcie_l1pm_substates_ctrl_l12()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_get_pcie_l1pm_substates_ctrl_l12)
        * [`SSDInterface.nvme_hw_get_pcie_link_info()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_get_pcie_link_info)
        * [`SSDInterface.nvme_hw_get_pcie_link_info_by_register()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_get_pcie_link_info_by_register)
        * [`SSDInterface.nvme_hw_is_support_flr()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_is_support_flr)
        * [`SSDInterface.nvme_hw_set_pcie_aspm()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_set_pcie_aspm)
        * [`SSDInterface.nvme_hw_set_pcie_l1pm_substates_ctrl_l12()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_hw_set_pcie_l1pm_substates_ctrl_l12)
        * [`SSDInterface.nvme_smart_check_batch()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_smart_check_batch)
        * [`SSDInterface.nvme_smart_check_single()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_smart_check_single)
        * [`SSDInterface.nvme_smart_get_batch()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_smart_get_batch)
        * [`SSDInterface.nvme_smart_get_full()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_smart_get_full)
        * [`SSDInterface.nvme_smart_get_single()`](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface.nvme_smart_get_single)
    * [Module contents](ark.ark_ssd.ssd.md#module-ark.ark_ssd.ssd)


## Module contents
@Module : ark_ssd
@Date : 2026/03/03 16:18
@Version : V1.0.0
Only for Lexar SSD team.

🐻@Version: 1.0.0 @update time: 2025/04/07 @Person Responsible: lu.zhang

ꔷ First release.
