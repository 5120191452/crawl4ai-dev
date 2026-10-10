---
title: "Installation and Configuration"
docname: "Installation and Configuration"
source: "http://orion.longsys.com/Installation%20and%20Configuration.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# Installation and Configuration
To use this testing platform, users need to follow the steps below to install and configure the required software and plugins.
## Orion_ark下载
点击左侧Download, 进入下载页面。点击下载按钮, 在弹框中选择项目所需配置, 点击确定,等待下载完成 注: Orion_ark将强制使用下载时所选配置, 配置更新工具对Orion_ark进行的配置更改将失效
## Orion_ark安装
目前支持在线和离线两种方式进行Orion_ark安装
### 在线安装
  1. 下载Orion_ark更新工具: <http://orion.longsys.com/tools/download/Orion_ark_update_tool>
  2. 将Orion_ark更新工具上传到分布式系统
  3. 将从左侧Download页面下载的Orion_ark安装包压缩为zip文件，压缩方式为: 右键点击下载的Orion_ark-x.x.x.tar.gz安装包, 选择 “7-Zip”, 选择 “添加到”Orion_ark-x.x.x.tar.gz.zip”
  4. 将压缩后的zip文件作为Orion_ark更新工具的配置文件上传到分布式系统
  5. 创建任务、执行, 即可实现Orion_ark在测试机的安装/升级


### 离线安装
执行命令 pip install Orion_ark-x.x.x.tar.gz, 等待提示信息安装成功
## Orion_ark授权
目前支持在线和离线两种方式进行Orion_ark授权, 操作需使用Orion_ark V2.4.4及以上版本, 两种授权方式均需访问Orion官网授权管理系统: <http://orion.longsys.com/service_home/request_auth>
注: 授权管理系统目前仅限管理员账号操作, 如您非管理员, 请将相关信息(组织、IP/IP段、机器码等)提供给[任贵红]代为申请
### 在线授权
  1. 确保目标机器能访问 10.2.18.22:5000, 如网络受限需向信息部申请访问权限
  2. 在授权管理系统的”申请白名单”页面输入被授权机器所属组织, IP/IP段以及授权期限, 并提交申请
  3. 白名单申请通过后, 运行工具时可自动授权


### 离线授权
  1. 下载授权工具: <http://orion.longsys.com/tools/download/orion_auth>
  2. 运行授权工具 orion_auth.py, 若检测到无法进行在线授权, 工具会生成机器码并展示, 同时提示输入授权码
  3. 将生成的机器码复制, 在授权管理系统的”申请离线授权”页面输入所属组织, IP/IP段, 机器码及授权期限, 点击生成授权码
  4. 将生成的授权码复制到工具的授权码输入行, 即可完成授权


## Orion_ark依赖包安装
  1. 当测试机器能正常连接Orion服务器(10.2.18.22:5000), 进行测试时, Orion_ark将对环境进行检测, 自动安装所需依赖包
  2. 当测试机器无法正常访问Orion服务器时, 请通过Orion环境配置工具进行安装
