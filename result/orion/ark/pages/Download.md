---
title: "Download"
docname: "Download"
source: "http://orion.longsys.com/Download.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# Download
[下载](Download.md)
  * 点击右侧按钮, 下载Orion_ark最新版本
  * 可选配置详细说明如下：


## ark_device:
>   *

**DeviceType** 用户根据需要测试的产品类型进行配置, 各类型说明如下:

>     * `DeviceType_SD`: SD产品
>     * `DeviceType_EMMC`: EMMC产品
>     * `DeviceType_UDisk`: USB产品
>   *

**TransferType** 用户根据测试需要选择采用全双工还是半双工模式，各类型说明如下:

>     * `TransferType_Half_Duplex`: 半双工模式。对于DeviceType_UDisk产品, 该模式为BOT
>     * `TransferType_Full_Duplex`: 全双工模式。对于DeviceType_UDisk产品, 该模式为UAS
>

## ark_std_cmd:
>   * **DeviceType** 请参考ark_device中DeviceType
>

## ark_vu_cmd:
>   * **DeviceType** 请参考ark_device中DeviceType
>   *

**TransferCMDType** 可选类型 read_card_cmd、std_protocol_cmd, 用户根据测试需要选择读卡器命令还是标准协议命令，各类型说明如下:

>     * `read_card_cmd`: 读卡器命令
>     * `std_protocol_cmd`: 标准协议命令
>

## ark_ape:
>   * **DeviceType** 请参考ark_device中DeviceType
>

## ark_camera:
>   *

**CameraType** 用户可根据测试需要选择消费级有线相机还是消费级无线相机，各类型说明如下:

>     * `consumer_wired`: 消费级有线相机
>     * `consumer_wireless`: 消费级无线相机
>

## ark_oven:
>   *

**OvenType** 用户可根据需要控制的温箱类型进行配置, 各类型说明如下:

>     * `serial_3720`: 3720平台通过串口进行通信的mcu
>     * `network_temp_chamber_zz`: 众志温箱通过网络进行TCP通信
>     * `network_temp_chamber_sw`: 三木温箱通过网络进行TCP通信
>     * `mock_temp_chamber`: 模拟温箱数据
>

## ark_power:
>   *

**PowerType** 用户可根据需要控制的电源仪器/方式进行配置, 各类型说明如下:

>     * `serial_3720`: 3720平台通过串口进行通信的mcu
>     * `serial_1296`: 1296平台通过串口进行通信的mcu
>     * `power_win`: win平台(主要是针对休眠、睡眠的测试)
>     * `scsi_speed_spor`: 超稳高速板(目前只实现上断电相关)
>     * `power_meter`: 功耗仪
>   *

**InterfaceType**

>     * `USB_3720_and_1296`: 3720和1296上的USB接口
>     * `SD_3720_and_1296`: 3720和1296上的SD接口
>     * `EMMC_3720_and_1296`: 3720和1296上的EMMC接口
>

## ark_upgradation:
>   *

**UpgradeType** 用户可根据需要升级的对象进行配置, 各类型说明如下:

>     * `UpgradeType_system_image`: 更新系统镜像
>     * `UpgradeType_stm32_firmware`: 更新mcu固件
>     * `UpgradeType_test_device_fw`: 保留字段, 暂未实现
>

## ark_sector_operation:
>   *

**OperateType** 用户可根据测试方式/目的进行配置，各类型说明如下:

>     * `system_based`: 通过系统接口发送扇区读写命令
>     * `protocol_based`: 通过协议命令发送读写命令
>

## ark_driver:
>   *

**DriverType** 用户可根据测试目的/需求进行配置，各类型说明如下:

>     * `original_driver`: 系统原生驱动
>     * `orion_driver`: 平台部开发的驱动, 详情请参考驱动说明文档
>     * `ark_driver`: 测试部基于libusb二次开发的驱动
>

## ark_platform_adapt:
>   *

**PlatformType** 用户可根据测试平台进行配置, 各类型说明如下:

>     * `PlatformType_longsys_distributed_system`: 对接江波龙分布式测试系统, 通过配置此字段后, 继承test base的工具/用例可通过分布式自动化运行
>     * `PlatformType_longsys_ci_system`: 保留字段
>   *

**ShowWindowType** 当为None时, 该字段失效

>     * `ShowWindowType_close_when_finished`: 当平台启动时, 开始时弹框, 测试结束后自动关闭窗口, 目前仅支持Windows
>

## ark_ipc:
>   *

**IpcType** 用户可根据测试目的/需求进行配置，各类型说明如下:

>     * `EZVIZ`: 萤石品牌
>     * `IMOU`: 乐橙品牌
>     * `TP_LINK`: TP_LINK品牌
>     * `XIAOMI`: 小米品牌
>     * `SKYWORTH`: 创维小湃品牌
>     * `Q360`: 360品牌
>     * `HUAWEI`: 华为品牌
>

## ark_recorder:
>   *

**RecorderType** 用户可根据测试目的/需求进行配置, 各类型说明如下:

>     * `GL840`: 对接GL840品牌记录仪, 可一拖多进行测试
>     * `GL860`: 对接GL860品牌记录仪, 可一拖一进行测试
>
