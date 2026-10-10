---
title: "ark.ark_vu_cmd package"
docname: "ark.ark_vu_cmd"
source: "http://orion.longsys.com/ark.ark_vu_cmd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_vu_cmd package
## Subpackages
  * [ark.ark_vu_cmd.vu_cmd package](ark.ark_vu_cmd.vu_cmd.md)
    * [Submodules](ark.ark_vu_cmd.vu_cmd.md#submodules)
    * [ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_factory module](ark.ark_vu_cmd.vu_cmd.md#module-ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_factory)
      * [`ArkVuCmdFactory`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_factory.ArkVuCmdFactory)
        * [`ArkVuCmdFactory.create_object()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_factory.ArkVuCmdFactory.create_object)
    * [ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface module](ark.ark_vu_cmd.vu_cmd.md#module-ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface)
      * [`TransferCMDType`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.TransferCMDType)
        * [`TransferCMDType.read_card_cmd`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.TransferCMDType.read_card_cmd)
        * [`TransferCMDType.std_protocol_cmd`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.TransferCMDType.std_protocol_cmd)
      * [`VuCmdInterface`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface)
        * [`VuCmdInterface.erase_blk()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.erase_blk)
        * [`VuCmdInterface.get_dev_smart_info()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.get_dev_smart_info)
        * [`VuCmdInterface.get_dft_info()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.get_dft_info)
        * [`VuCmdInterface.get_firmware_info()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.get_firmware_info)
        * [`VuCmdInterface.get_flash_id()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.get_flash_id)
        * [`VuCmdInterface.get_flash_param()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.get_flash_param)
        * [`VuCmdInterface.get_smart_info()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.get_smart_info)
        * [`VuCmdInterface.read_bit_info()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.read_bit_info)
        * [`VuCmdInterface.read_common_info()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.read_common_info)
        * [`VuCmdInterface.read_flash_page()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.read_flash_page)
        * [`VuCmdInterface.read_iir()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.read_iir)
        * [`VuCmdInterface.read_ram()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.read_ram)
        * [`VuCmdInterface.rebuild_bit()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.rebuild_bit)
        * [`VuCmdInterface.set_bad_blk()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.set_bad_blk)
        * [`VuCmdInterface.user_cmd_authorize()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.user_cmd_authorize)
        * [`VuCmdInterface.write_flash_page()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.write_flash_page)
        * [`VuCmdInterface.write_ram()`](ark.ark_vu_cmd.vu_cmd.md#ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface.write_ram)
    * [Module contents](ark.ark_vu_cmd.vu_cmd.md#module-ark.ark_vu_cmd.vu_cmd)


## Module contents
@Module : ark_vu_cmd
@Date : 2024/08/16
@Version : V1.0.0
The “ark_vu_cmd” module is a module responsible for executing TL300 private commands
