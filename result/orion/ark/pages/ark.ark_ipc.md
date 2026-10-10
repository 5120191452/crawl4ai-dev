---
title: "ark.ark_ipc package"
docname: "ark.ark_ipc"
source: "http://orion.longsys.com/ark.ark_ipc.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_ipc package
## Subpackages
  * [ark.ark_ipc.ipc package](ark.ark_ipc.ipc.md)
    * [Subpackages](ark.ark_ipc.ipc.md#subpackages)
      * [ark.ark_ipc.ipc.ark_ipc package](ark.ark_ipc.ipc.ark_ipc.md)
        * [Module contents](ark.ark_ipc.ipc.ark_ipc.md#module-ark.ark_ipc.ipc.ark_ipc)
    * [Submodules](ark.ark_ipc.ipc.md#submodules)
    * [ark.ark_ipc.ipc.ark_ipc_factory module](ark.ark_ipc.ipc.md#module-ark.ark_ipc.ipc.ark_ipc_factory)
      * [`ArkIpcFactory`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_factory.ArkIpcFactory)
        * [`ArkIpcFactory.create_object()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_factory.ArkIpcFactory.create_object)
    * [ark.ark_ipc.ipc.ark_ipc_interface module](ark.ark_ipc.ipc.md#module-ark.ark_ipc.ipc.ark_ipc_interface)
      * [`ArkIpcInterface`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface)
        * [`ArkIpcInterface.capture_progress_bar_image()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.capture_progress_bar_image)
        * [`ArkIpcInterface.check_app_login_status()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.check_app_login_status)
        * [`ArkIpcInterface.check_ipc_device_status()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.check_ipc_device_status)
        * [`ArkIpcInterface.check_progress_bar_from_image()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.check_progress_bar_from_image)
        * [`ArkIpcInterface.check_sd_exist()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.check_sd_exist)
        * [`ArkIpcInterface.find_ipc_device()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.find_ipc_device)
        * [`ArkIpcInterface.find_ui_with_ad_ui_handle()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.find_ui_with_ad_ui_handle)
        * [`ArkIpcInterface.full_day_recording_set()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.full_day_recording_set)
        * [`ArkIpcInterface.get_ipc_brand()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.get_ipc_brand)
        * [`ArkIpcInterface.get_sd_capacity()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.get_sd_capacity)
        * [`ArkIpcInterface.is_video_available()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.is_video_available)
        * [`ArkIpcInterface.kill_port_process()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.kill_port_process)
        * [`ArkIpcInterface.screenshot_and_find_text()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.screenshot_and_find_text)
        * [`ArkIpcInterface.sd_format()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.sd_format)
        * [`ArkIpcInterface.set_ultra_hd_quality()`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface.set_ultra_hd_quality)
      * [`IpcType`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType)
        * [`IpcType.EZVIZ`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.EZVIZ)
        * [`IpcType.HIKVISION`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.HIKVISION)
        * [`IpcType.HUAWEI`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.HUAWEI)
        * [`IpcType.IMOU`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.IMOU)
        * [`IpcType.Q360`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.Q360)
        * [`IpcType.SKYWORTH`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.SKYWORTH)
        * [`IpcType.TP_LINK`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.TP_LINK)
        * [`IpcType.XIAOMI`](ark.ark_ipc.ipc.md#ark.ark_ipc.ipc.ark_ipc_interface.IpcType.XIAOMI)
    * [Module contents](ark.ark_ipc.ipc.md#module-ark.ark_ipc.ipc)


## Module contents
@Module : ark_ipc
@Date : 2025/06/4
@Version : V1.0.0
This module serves as the core component of a multi-brand camera automated testing system, designed for IPC (IP Camera) applications on the Android platform. It enables centralized control and intelligent testing of various camera apps. Key functions include: automatically launching specified brand apps and detecting login status; locating target camera devices and verifying proper binding; monitoring and managing SD card status, performing formatting operations, and recording execution time; configuring cameras for continuous recording mode and validating functionality through screenshot capture and progress bar analysis. The module offers strong configurability and scalability, making it suitable for diverse testing scenarios across multiple brands.
