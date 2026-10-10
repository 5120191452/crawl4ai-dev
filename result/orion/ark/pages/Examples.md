---
title: "Examples"
docname: "Examples"
source: "http://orion.longsys.com/Examples.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# Examples
[下载](Examples.md)
  * 点击右侧按钮, 下载Orion_ark所有示例代码


## 「Ark 框架示例程序使用说明」
>   * 此代码基于 Ark 框架开发，您可通过以下步骤快速运行：
>   * 复制代码: 将鼠标移动到代码框，点击右上角「复制」按钮获取完整代码；
>   * 环境要求: 确保电脑已安装 Orion_ark 开发环境；
>   * 运行方式: 将代码粘贴至开发工具中，按常规流程编译运行即可。
>


```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import importlib.util
import shutil

# 通过此方式，无需安装Orion_ark，通过调用本地代码运行，方便调试
module_spec = importlib.util.find_spec('Orion_ark')
if module_spec and (not module_spec.origin or not importlib.util.find_spec('Orion_ark.basic') or not importlib.util.find_spec('Orion_ark.basic.ark_func')):
    shutil.rmtree(module_spec.submodule_search_locations[0]) # 删除安装的Orion_ark
    module_spec = None
if module_spec is None:
    project_root = os.path.dirname(os.path.abspath(__file__))
    while project_root != os.path.dirname(project_root):
        if os.path.isdir(os.path.join(project_root, 'Orion_ark')):
            sys.path.append(project_root)
            break
        project_root = os.path.dirname(project_root)

# 对于已安装Orion_ark的环境，如下import TestBase即可
from Orion_ark.basic.test_base import TestBase


# 请修改为所写用例/工具的名称，与配置中user字段下用例/工具名称保持一致
case_name = "case_demo"
# 请修改为本地运行时，期待使用的当前文件夹中的配置文件名
local_config_file = "demo_cfg.yaml"
# 请修改为当前版本号，版本号共3位
case_version = "1.0.1"
# 请修改为当前版本的改动点
modification_point = "add modification_point"
# 请修改为开发者英文名
author = "you name"

class test(TestBase):
    def pre_test(self):
        res = self.ark.error_list.err_ok
        # 进行测试前准备工作

        # 测试开始前，安装工具依赖的第三方库，这里仅作为演示，实际应根据需要安装
        required_packages = [
        "numpy==1.26.4",        # 精确版本号
        "PyYAML>=6.0",          # 最低版本号
        "pandas"                # 最新版本
        ]
        self.ark.install_packages(required_packages)

        return res

    def testing(self):
        res = self.ark.error_list.err_ok
        # do testing

        # import工具依赖的第三方库或者自己开发的库/文件，用于测试用例中使用，这里仅作为演示，实际应根据需要import
        import numpy as np
        import yaml
        import pandas as pd

        src_buf = self.ark.create_module(self.ark.module_list.module_buffer, 40)
        dst_buf = self.ark.create_module(self.ark.module_list.module_buffer, 50)
        from Orion_ark.ark.ark_buffer.buffer.ark_buffer_interface import DataType
        src_buf.fill_data(0, 5, DataType.DATA_ALL_ONE.value)
        dst_buf.fill_data(0, 5, DataType.DATA_ALL_ONE.value)

        # 对于只返回错误码的函数，可以考虑采用方法1使代码更简洁
        # 对于返回多个值或者需要用到错误码的函数，建议采用方法2
        # 此处仅用 compare 作为演示，实际应该把check_result运用到返回错误码的函数
        self.check_result(src_buf.compare(0, dst_buf, 0, 5))    # 方法1
        res = src_buf.compare(0, dst_buf, 0, 5)                 # 方法2
        self.check_result(res)

```
Copy to clipboard

<<<<<<< HEAD

required_packages = [ “numpy==1.26.4”, # 精确版本号 “PyYAML>=6.0”, # 最低版本号 “pandas” # 最新版本 ] self.ark.install_packages(required_packages)
> > > return res

def clean_up(self):

>> res = self.ark.error_list.err_ok # 进行测试后清理工作
>> return res

if __name__ == ‘__main__’:

> config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), local_config_file) if local_config_file else None test().do_test(case_name, local_config_path=config_path, case_version=case_version, modification_point=modification_point, author=author)
