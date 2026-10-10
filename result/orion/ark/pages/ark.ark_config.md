---
title: "ark.ark_config package"
docname: "ark.ark_config"
source: "http://orion.longsys.com/ark.ark_config.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_config package
## Subpackages
  * [ark.ark_config.config package](ark.ark_config.config.md)
    * [Subpackages](ark.ark_config.config.md#subpackages)
      * [ark.ark_config.config.ark_config package](ark.ark_config.config.ark_config.md)
        * [Submodules](ark.ark_config.config.ark_config.md#submodules)
        * [ark.ark_config.config.ark_config.config module](ark.ark_config.config.ark_config.md#module-ark.ark_config.config.ark_config.config)
        * [Module contents](ark.ark_config.config.ark_config.md#module-ark.ark_config.config.ark_config)
    * [Submodules](ark.ark_config.config.md#submodules)
    * [ark.ark_config.config.ark_config_interface module](ark.ark_config.config.md#module-ark.ark_config.config.ark_config_interface)
      * [`ArkConfigInterface`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface)
        * [`ArkConfigInterface.get_parameter()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.get_parameter)
        * [`ArkConfigInterface.init()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.init)
        * [`ArkConfigInterface.update_config()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.update_config)
        * [`ArkConfigInterface.update_config_from_file()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.update_config_from_file)
        * [`ArkConfigInterface.update_config_from_key_value()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.update_config_from_key_value)
        * [`ArkConfigInterface.update_config_from_string()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.update_config_from_string)
        * [`ArkConfigInterface.update_missing_config()`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface.update_missing_config)
      * [`UpdateType`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.UpdateType)
        * [`UpdateType.config_dict`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.UpdateType.config_dict)
        * [`UpdateType.config_string`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.UpdateType.config_string)
        * [`UpdateType.file_path`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.UpdateType.file_path)
    * [Module contents](ark.ark_config.config.md#module-ark.ark_config.config)


## Module contents
@Module : ark_config
The “ark_config” module is a module responsible for centralised management and provision of configuration data, with the aim of setting the appropriate parameters for the Orion_ark project according to the user’s needs.
Through the use of this module, Orion_ark components do not need to pass parameters or read or modify configuration files during instantiation or other parameter-required operations, but rather use the public interface provided by the “ark_config” module to carry out the corresponding operations.
The module supports getting and returning parameters from YAML files and modifying parameter values: 1. Support getting or modifying configurations through the provided interfaces; 2. Support getting or modifying configurations from the command line.
The parameter configuration module achieves centralised management and controlled access to configuration data, ensuring consistency and maintainability of configuration data.

🐻@Version: 1.0.6 @update time: 2025/06/13 @Person Responsible: lu.zhang

ꔷ get_parameter函数parameter_name增加默认值(“”), 传入空字符串返回所有配置.

🐻@Version: 1.0.5 @update time: 2025/05/30 @Person Responsible: lu.zhang

ꔷ 为兼容以前配置, config组件init会从本地文件加载后再由安装配置更新. ꔷ ini文件加载大小写敏感.

🐻@Version: 1.0.4 @update time: 2025/05/29 @Person Responsible: lu.zhang

ꔷ config组件init不再从本地文件加载/保存文件至本地.

🐻@Version: 1.0.3 @update time: 2025/05/26 @Person Responsible: lu.zhang

ꔷ 解析ini文件时指定编码方式. ꔷ 支持py文件.

🐻@Version: 1.0.2 @update time: 2025/04/16 @Person Responsible: yaosen.bian

ꔷ 支持json、ini文件.

🐻@Version: 1.0.1 @update time: 2025/03/10 @Person Responsible: yaosen.bian

ꔷ Modify it to be a singleton class.
