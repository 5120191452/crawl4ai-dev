---
title: "Problems and Solutions"
docname: "Problems and Solutions"
source: "http://orion.longsys.com/Problems%20and%20Solutions.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# Problems and Solutions
Table of Contents
  * [Orion_ark 安装与授权失败](Problems%20and%20Solutions.md#orion-ark)
    * [Orion_ark 安装失败, 提示 setuptools 版本过低](Problems%20and%20Solutions.md#orion-ark-setuptools)
    * [Orion_ark 安装失败，提示 invalid command ‘bdist_wheel’](Problems%20and%20Solutions.md#orion-ark-invalid-command-bdist-wheel)
    * [授权工具运行失败, 提示 urllib3 v2 only supports OpenSSL 1.1.1+](Problems%20and%20Solutions.md#urllib3-v2-only-supports-openssl-1-1-1)
  * [使用中常见报错自查](Problems%20and%20Solutions.md#id1)
    * [语法与拼写错误](Problems%20and%20Solutions.md#id2)
    * [参数传递问题](Problems%20and%20Solutions.md#id3)
    * [初始化失败问题](Problems%20and%20Solutions.md#id4)
    * [路径与依赖问题](Problems%20and%20Solutions.md#id5)
  * [Orion_ark 错误码说明](Problems%20and%20Solutions.md#id6)
    * [层级错误码](Problems%20and%20Solutions.md#id7)
    * [组件错误码](Problems%20and%20Solutions.md#id8)
    * [具体错误码](Problems%20and%20Solutions.md#id9)


## [Orion_ark 安装与授权失败](Problems%20and%20Solutions.md#id24)
本节涵盖了Orion_ark安装与授权过程中可能遇到的问题及相应解决方案。
* * *
### [Orion_ark 安装失败, 提示 setuptools 版本过低](Problems%20and%20Solutions.md#id25)
**错误信息：**
版本不兼容错误

```
ERROR: Could not find a version that satisfies the requirement setuptools>=40.8.0 (from version: none)

```
Copy to clipboard
**解决方案：**
**步骤 1. 检查当前setuptools版本（若版本高于40.8.0，可直接跳转至步骤 4）：**
> 检查setuptools版本
>
```
pip show setuptools

```
Copy to clipboard
**步骤 2. 升级setuptools至最新版：**
从setuptools下载页：<https://pypi.org/project/setuptools/#files> 下载后缀为.whl的安装包，然后执行：
> 安装setuptools
>
```
pip install setuptools-xx.x.x-py3-none-any.whl

```
Copy to clipboard
**步骤 3. 重新安装Orion_ark：**
> 安装Orion_ark
>
```
pip install Orion_ark-x.x.x.tar.gz

```
Copy to clipboard
**步骤 4. 若仍然安装失败，可尝试以下任一方法：**
> **方法1：降级pip至21.3.1版本**
> 从 pip 21.3.1 下载页：<https://pypi.org/project/pip/21.3.1/#files> 下载后缀为.whl的安装包，然后执行：
>> 降级pip版本
>>
```
python -m pip install --force-reinstall --no-index pip-21.3.1-py3-none-any.whl

```
Copy to clipboard
> 完成后，按照步骤3重新安装Orion_ark。
> **方法2：使用–no-build-isolation选项重新安装**
>> 使用特殊选项安装
>>
```
pip install Orion_ark-x.x.x.tar.gz --no-build-isolation

```
Copy to clipboard
* * *
### [Orion_ark 安装失败，提示 invalid command ‘bdist_wheel’](Problems%20and%20Solutions.md#id26)
**错误信息：**
安装失败错误

```
error: subprocess-exited-with-error

*****

note: This error originates from a subprocess, and is likely not a problem with pip.

```
Copy to clipboard
**解决方案：**
**步骤 1. 升级setuptools至最新版：**
从setuptools下载页：<https://pypi.org/project/setuptools/#files> 下载后缀为.whl的安装包，然后执行：
> 安装setuptools
>
```
pip install setuptools-xx.x.x-py3-none-any.whl

```
Copy to clipboard
**步骤 2. 使用–no-build-isolation选项重新安装Orion_ark：**
> 重新安装Orion_ark
>
```
pip install Orion_ark-x.x.x.tar.gz --no-build-isolation

```
Copy to clipboard
* * *
### [授权工具运行失败, 提示 urllib3 v2 only supports OpenSSL 1.1.1+](Problems%20and%20Solutions.md#id27)
**错误信息：**
版本不兼容错误

```
ImportError: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2 22 Jan 2015'

```
Copy to clipboard
**解决方案：**
**步骤 1. 卸载urllib3旧版本：**
> 卸载urllib3
>
```
pip uninstall urllib3

```
Copy to clipboard
**步骤 2. 运行Orion_ark示例程序，让系统自动下载安装兼容版本：**
**步骤 3. 重新运行授权工具：**
## [使用中常见报错自查](Problems%20and%20Solutions.md#id28)
在调用 Orion_ark 接口或运行相关程序时，若出现 AttributeError、TypeError、初始化失败 等报错，建议先按以下步骤检查自身代码，多数问题可通过自查解决。
### [语法与拼写错误](Problems%20and%20Solutions.md#id29)
检查关键字、接口名、方法名的拼写及格式是否准确（区分大小写），如：
>   1. 检查脚本类的初始化方法 __init__ 是否被误写为 _init_(缺少一个下划线)、__int__(字母错误) 或 __Init__(大小写错误);
>   2. 检查包中导出的接口名是否被误写（如 set_sel()）被误写（如 set_sl() 少字母、set_Sel() 大小写错误）。
>

### [参数传递问题](Problems%20and%20Solutions.md#id30)
确认调用接口时的参数是否符合要求：
>   1. 检查是否传入了所有必传参数;
>   2. 检查参数类型是否匹配;
>   3. 检查参数范围是否合法。
>

### [初始化失败问题](Problems%20and%20Solutions.md#id31)
确认 Orion_ark 是否成功初始化：
>   1. 检查是否正确导包 (如 from Orion_ark.basic.test_base import TestBase);
>   2. 确认是否调用了初始化方法 (如继承 TestBase 类, 却不调用init方法时, 需调用 self.ark.init(), 才能正常使用其余组件接口);
>   3. 检查是否传入了正确的参数 (如 power 组件的 power_connect 接口, 需传入正确的 device 盘符, 而不是句柄)。
>

### [路径与依赖问题](Problems%20and%20Solutions.md#id32)
若涉及文件或外部依赖操作：
>   1. 检查文件路径是否存在且有访问权限;
>   2. 确认项目中无与包名冲突的文件;
>   3. 检查依赖库版本是否兼容 (如 numpy 版本过高, 2.x 版本, 可能触发兼容性问题，需降级至 1.26.4 版本)。
>

若自查后问题仍未解决，可结合下一节「错误码说明」进一步定位问题根源。
## [Orion_ark 错误码说明](Problems%20and%20Solutions.md#id33)
本节定义了 Orion_ark 的错误码体系，包括层级错误码、组件错误码及具体错误码，用于问题定位与排查。
### [层级错误码](Problems%20and%20Solutions.md#id34)
层级错误码对照表
| 错误码  | 常量名  | 描述  |
| --- | --- | --- |
| 0xFF000000  | err_hierarchy_case  | 工具/用例报错（来自测试用例或外部工具的错误）  |
| 0xEF000000  | err_hierarchy_ark  | Orion_ark 核心模块报错（来自框架内部的错误）  |
### [组件错误码](Problems%20and%20Solutions.md#id35)
组件错误码对照表
| 错误码  | 常量名  | 描述  |
| --- | --- | --- |
| 0x00A10000  | err_ark_common  | 公共功能模块  |
| 0x00AF0000  | err_ark_authorizations  | 授权组件  |
| 0x00B10000  | err_ark_task_mgr  | 任务管理组件  |
| 0x00B20000  | err_ark_buffer  | 缓存组件  |
| 0x00B30000  | err_ark_logging  | 日志组件  |
| 0x00B40000  | err_ark_config  | 配置组件  |
| 0x00B50000  | err_ark_switch_system  | 切换系统组件  |
| 0x00C10000  | err_ark_oven  | oven组件  |
| 0x00C20000  | err_ark_power  | 电源组件  |
| 0x00C30000  | err_ark_platform_adapt  | 平台适配组件  |
| 0x00C40000  | err_ark_upgradation  | 升级组件  |
| 0x00C50000  | err_ark_camera  | 相机组件  |
| 0x00C60000  | err_ark_tool_to_platform_adapt  | 工具-平台适配组件  |
| 0x00C70000  | err_ark_dvr  | DVR 组件  |
| 0x00C80000  | err_ark_ipc  | IPC 组件  |
| 0x00D10000  | err_ark_adb  | ADB 组件  |
| 0x00D20000  | err_ark_appium  | Appium 组件  |
| 0x00D30000  | err_ark_recorder  | 记录器组件  |
| 0x00D40000  | err_ark_notify  | 通知组件  |
| 0x00F10000  | err_ark_file_operation  | 文件操作组件  |
| 0x00F20000  | err_ark_sector_operation  | 扇区操作组件  |
| 0x00F30000  | err_ark_device  | 设备组件  |
| 0x00F40000  | err_ark_std_cmd  | 标准命令组件  |
| 0x00F50000  | err_ark_vu_cmd  | 私有命令组件  |
| 0x00F60000  | err_ark_ape  | APE 组件  |
### [具体错误码](Problems%20and%20Solutions.md#id36)
具体错误码对照表
| 错误码  | 常量名  | 描述  |
| --- | --- | --- |
| 0x0000  | err_ok  | 操作成功  |
| 0x0001  | err_authorization  | 授权验证失败  |
| 0x0002  | err_env  | 环境异常  |
| 0x0003  | err_state  | 设备/模块状态异常  |
| 0x0004  | err_config_data  | 配置数据错误  |
| 0x0005  | err_start_server  | 服务启动失败  |
| 0x0006  | err_init  | 初始化失败  |
| 0x000C  | err_process_already_exists  | 进程已存在  |
| 0x000D  | err_exec_function  | 功能执行失败（具体参考调用的函数名）  |
| 0x000E  | err_exec_cmd  | 命令执行失败（外部命令返回非零状态）  |
| 0x000F  | err_function_not_supported  | 功能不支持（当前版本未实现该功能）  |
| 0x0011  | err_invalid_data  | 数据无效（输入数据格式或内容错误）  |
| 0x0012  | err_invalid_param  | 参数无效（函数参数超出合法范围）  |
| 0x0021  | err_open  | 打开失败  |
| 0x0022  | err_read  | 读取失败  |
| 0x0023  | err_write  | 写入失败  |
| 0x0024  | err_seek  | 偏移失败  |
| 0x0025  | err_close  | 关闭失败  |
| 0x0026  | err_rename  | 重命名失败  |
| 0x0027  | err_not_exist  | 资源不存在  |
| 0x0028  | err_create  | 创建失败  |
| 0x0029  | err_delete  | 删除失败  |
| 0x002A  | err_no_space  | 空间不足  |
| 0x0031  | err_connect  | 连接失败  |
| 0x0032  | err_transfer  | 传输失败  |
| 0x0033  | err_response  | 回复错误  |
| 0x0034  | err_timeout  | 操作超时  |
| 0x0035  | err_busy  | 繁忙  |
| 0x0036  | err_abnormal_interruption  | 异常中断  |
| 0x0041  | err_check  | 检查失败  |
| 0x0042  | err_compare  | 匹配失败  |
| 0x0043  | err_parse  | 解析失败  |
| 0x0051  | err_mount  | 挂载失败  |
| 0x0052  | err_unmount  | 取消挂载失败  |
