---
title: "Release Note"
docname: "Release Note"
source: "http://orion.longsys.com/Release%20Note.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# Release Note
## V3.2.1 2026-09-22
>   *

更新组件

>     *

ark_camera:

>       * 新增消费级无线相机支持, 工厂接口新增 CameraType 配置项, 支持 Lexar 相机测试需求
>       * 新增视频画质检测能力, 支持视频损坏、丢帧、模糊与马赛克检测
>       * 文件操作接口新增主机端(Host)文件枚举、计数与删除支持
>     *

ark_common:

>       * 新增 ark_mobile 组件注册与错误码标识
>     *

ark_ipc:

>       * 接入 autoGLM 大模型, 新增 AI 自动识别并关闭弹窗能力, 替代原 Qwen VL 弹窗检测方案
>       * autoGLM 模型支持本地部署接入, 云端服务不可用时自动切换
>       * 优化录像进度条左右裁剪逻辑, 提升进度条识别准确性
>       * 更新小米 IPC 滑动坐标与像素阈值, 适配新版 UI
>     *

ark_mobile:

>       * 新增 ark_mobile 组件, 基于 ADB 提供设备连接、存储管理、文件操作、媒体文件检索、相机自动化与弹窗处理能力, 支持 Google、三星、小米、OPPO、vivo、荣耀、华为、联想、传音等品牌机型
>     *

ark_notify:

>       * 新增飞书群机器人通知支持, 通过 feishu: 前缀自动识别飞书接收者, 支持签名及无签名调用
>       * 新增飞书加签机器人通知支持, 支持 secret:webhook 加签调用方式
>       * 放宽飞书机器人 Webhook 校验规则
>   *

其他

>     * 新增 openai == 2.48.0、uiautomator2 == 3.7.0依赖库, 支持移动端自动化与 AI 大模型能力接入
>     * 配置模板新增 ark_camera 相机类型(CameraType)配置项, 支持有线/无线相机选择
>

## V3.2.0 2026-07-13
>   *

更新组件

>     *

ark_ape:

>       * 优化 APE 重放性能(ORION-1053)
>       * 更新ape组件单元测试
>       * 新增容量校验保护
>     *

ark_basic:

>       * 新增框架启动前自动清缓存, 提升初始化稳定性
>       * 更新 arkC 依赖版本号
>     *

arkC:

>       * 新增 set_driver_type 函数声明
>       * arkC 日志等级标识统一修改为 ARKC_LOG_LEVEL
>     *

ark_common:

>       * 新增安卓平台运行适配支持
>     *

ark_device:

>       * 主控识别修改为前缀匹配, 提升对新型号主控的兼容性(ETGTM-118)
>     *

ark_file_operation:

>       * 新增 file_operation 组件需求接口并补充单元测试用例
>       * 更新 Android 自动化接口 append 检查方式
>     *

ark_logging:

>       * 开放脚本日志等级设置接口, 支持通过日志级别配置调整运行时输出
>       * 新增 log 组件需求接口并补齐单元测试用例
>     *

ark_oven:

>       * 新增三木温箱控制接口, 支持 network_temp_chamber_sw 运行模式配置
>       * 修复三木温箱运行模式相关问题
>     *

ark_power:

>       * 新增 Lexar 掉电板适配需求支持
>       * 新增两个 power 组件工厂类, 增强串口功耗设备与继电器控制支持
>     *

ark_std_cmd:

>       * emmc handle 转换新增前置校验
>     *

ark_vu_cmd:

>       * sd vu 命令新增 0x81、0x80 私有命令支持, erase_blk 命令补充命令码与结构体改动
>       * sd 解密字符串输出修改为 bytearray
>     *

ark_visualsims:

>       * 优化二维码检测流程, 提高识别稳定性
>   *

解决BUG

>     *

ark_device:

>       * 修复返回码数量不一致的问题
>     *

ark_notify:

>       * 修复无法连续多次初始化接收者的问题
>     *

ark_vu_cmd:

>       * emmc CMD38 改为 R1 回复, 命令结束后自行监测 d0, 规避硬件超时限制(ORION-1489)
>   *

其他

>     * 新增测试平台 WIKI 文档
>     * 更新 install_packages 用法示例
>     * 网页首页新增 ark 代码解读链接
>     * 优化git_help分支屏蔽逻辑
>

## V3.1.1 2026-05-08
>   *

更新组件

>     *

ark_basic:

>       * 新增 Longsys 准入账号的身份认证与基础鉴权功能, 使用 ldap3 连接 LDAP 服务器完成管理账号绑定、用户 DN 查询与身份验证
>     *

ark_device:

>       *

ark_device_emmc:

>         * 修复 emmc erase 前未等待卡状态的问题, 新增 emmc_wait_cardstatus 检查
>         * 修复错误码返回不规范问题, err_invalid_param 返回值加入模块错误标识
>     *

ark_ipc:

>       * 新增对小米新型号 336、TPLINK 新型号 338 的支持, 包含 TPLINK SD 卡设置页面滚动查找与 Xiaomi 异常状态提示的兼容性优化
>     *

ark_std_cmd:

>       *

ark_emmc_std_cmd:

>         * 优化 card status 判断逻辑, 遇到非正常 rsp 时提前退出
>     *

ark_vu_cmd:

>       *

ark_sd_vu_cmd & ark_emmc_vu_cmd:

>         * 优化不支持时的错误码返回
>     *

ark_visualsims:

>       * 新增图像方向校正接口, 支持 ONNX 模型识别图像朝向并自动旋转
>       * 修复第三方库 pyzbar 依赖缺失时的报错提示
>   *

解决BUG

>     *

ark_basic:

>       * 修复虚拟环境下安装依赖缺失的问题(ORION-1432)
>     *

ark_common:

>       * 修复 RK3566 创建文件夹失败问题(ORION-1433)
>     *

ark_ssd:

>       * 修复 Windows 下 SSD 组件获取 raw 容量的兼容性问题 (ORION-1288)
>

## V3.1.0 2026-04-22
>   *

更新组件

>     *

ark_basic:

>       * 新增install_packages函数, 用于安装依赖的第三方Python库
>     *

ark_device:

>       * 新增TL300与WM5000获取流程, 兼容新架构ECC信息读取
>     *

ark_vu_cmd:

>       *

ark_sd_vu_cmd:

>         * 新增SD A1命令解密逻辑
>     *

ark_visualsims:

>       * 优化二维码识别流程, 新增pyzbar模型支持
>   *

解决BUG

>     *

ark_file_operation:

>       * 修复Linux下格式化NVMe SSD失败问题(ORION-1231)
>

## V3.0.4 2026-04-03
>   *

更新组件

>     *

ark_visualsims:

>       * 新增索尼(Sony)相机适配支持拍照功能
>     *

ark_power:

>       * 解决PowerMeterAdapter中gpio_control函数调用失败的问题
>       * 修改gpio_control函数中接收返回值的列表
>       * 移除PowerMeterAdapter类中的冗余函数
>     *

ark_device:

>       *

ark_device_sd:

>         * 修复SD接口在执行读操作时触发的超时错误
>   *

解决BUG

>     *

ark_ipc:

>       * 修复小米、TPlink更新导致的异常问题(ORION-1126)
>     *

ark_std_cmd:

>       *

ark_sd_std_cmd:

>         * 修复模块初始化阶段出现的超时问题(ORION-1216)
>

## V3.0.3 2026-02-28
>   *

更新组件

>     *

ark_device:

>       *

ark_device_sd & ark_device_usb:

>         * 新增ECC接口中途停止功能
>       *

ark_device_usb:

>         * MAP1202主控标准smart兼容CDI9.7.0新增字段(ORION-1085)
>     *

ark_power:

>       * 新增控制GPIO引脚上拉/下拉状态的接口
>   *

其他

>     * 官网下载Orion_ark包时, 选择ark_device的DeviceType可自动同步至ark_std_cmd、ark_vu_cmd、ark_ape, 并禁用后三者手动选择DeviceType功能
>

## V3.0.2 2026-01-27
>   *

更新组件

>     *

ark_visualsims:

>       * 修复在空目录路径已存在的情况下, 未触发模型下载与更新的问题
>     *

ark_device:

>       *

ark_device_usb:

>         * 新增ECC信息获取接口, 支持TL300、WM5000、DM2320、DM2705、DM2706主控
>         * 修复因超时处理及主控识别逻辑异常, 导致MAP1202与MAS1102主控SMART信息获取失败的问题
>     *

ark_adaptation_tool:

>       * 支持准备函数中返回错误码
>       * 适配VTE工具
>   *

解决BUG

>     *

ark_device:

>       * 修复read_capacity16命令数据长度未正确设置, 导致容量信息获取异常的问题(ORION-1060)
>

## V3.0.1 2025-01-07
>   * 紧急修复：解决纯净系统下, 脚本运行失败问题
>

## V3.0.0 2025-12-30
>   * 本次为3.0.0大版本发布。该版本在架构与能力上进行了重要升级, SD、eMMC产品适配与通用接口体系得到进一步完善并通过DVT验收, 实现跨产品测试能力的标准化与一致性。
>   * 使用本版本时, 请配合平台部提供的OrionPlat_V1.0.8镜像版本及MCU版本1.7.7, 以确保功能兼容与运行稳定。
>   *

更新组件

>     *

ark_std_cmd:

>       *

ark_sd_std_cmd & ark_emmc_std_cmd:

>         * 对SD与eMMC卡片标准命令进行全面完善与稳定化处理, 标志着该能力正式发布, 覆盖主要控制与数据传输场景
>     *

ark_device:

>       *

ark_device_sd & ark_device_emmc & ark_device_usb:

>         * 统一接口体系正式发布, 全面支持SD与eMMC卡片的读、写、擦除、切速、复位等通用操作
>         * 测试用例可在不同产品形态间复用, 显著提升跨产品一致性与可维护性
>       *

ark_device_usb:

>         * 修复获取遥测信息接口数据返回不一致的问题
>     *

ark_visualsims:

>       * 新增visualsims组件, ark_visualsims作为统一的视觉自动化执行组件, 提供图像采集、视觉感知、目标元素识别及键鼠模拟等端到端控制能力
>     *

ark_adaptation_tool:

>       * 修复VTE自动化工具相关问题(CT、A1日志解析缺失、主控替换异常等)
>     *

ark_oven:

>       * 修改设置温度函数set_target_temp默认不等待完成; 若选择等待, 则默认超时时间为300s
>       * 修复获取当前温度get_current_temp与获取目标温度get_target_temp返回值异常的问题
>     *

ark_file_operation:

>       * delete_file接口在Windows系统下, 当删除只读文件失败时, 新增使用del命令进行强制删除的补偿逻辑
>     *

ark_camera:

>       * camera组件依赖的dll文件已上传至制品库, 不再随安装包分发
>   *

其他

>     * arkC更新至1.1.9版本
>

## V2.4.6 2025-12-10
>   *

更新组件

>     *

ark_device:

>       *

ark_device_usb:

>         * get_info接口新增主控识别功能, 使用方式参考示例程序。目前支持TL300、CFE(DM5216_F、DM5220)、DM2320、MAP1202、MAS1102主控
>         * 适配CFE(DM5216_F、DM5220)的NVMe标准SMART获取
>         * 新增get_device_log接口, 使用方式参考示例程序。目前在log type为DeviceLogType.Telemetry时, 支持WM3000、CFE(DM5216_F、DM5220)、DM2320主控产品的遥测数据获取
>       *

ark_device_emmc:

>         * 内部创建buffer的类型由BufferType.ARKC_BUFFER优化为BufferType.ORION_BUFFER, 减少不必要的数据转换
>     *

ark_ipc:

>       * 新增适配华为品牌ipc
>   *

解决BUG

>     *

ark_device:

>       * 修复VID、PID不兼容导致MAS1102主控识别异常, 无法获取SMART的问题(ORION-996)
>     *

ark_sector_operatiion:

>       * 去掉遗漏的调试打印(ORION-1036)
>     * 修复导包异常导致脚本运行结束后卡死的问题(ORION-1020)
>     * 修复导包异常导致SD卡读卡器模式下获取SMART异常的问题
>   *

其他

>     * Ark初始化时会自动按需调整frag_size, EMMC和SD产品在测试时无需再手动配置
>

## V2.4.5 2025-11-04
>   *

更新组件

>     *

ark_ipc:

>       * ipc组件代码合入主干, 配置可在下载Orion_ark包时选择, 默认为EZVIZ
>       * 新增适配360品牌ipc
>       * 修复小米UI更新导致的异常问题
>     *

ark_power:

>       * 新增continuous_current_acquisition接口, 支持精密电流仪连续采集电流
>       * 精密电流仪自适应最大容量, 增加DMM模式测量电流
>       * 完善接口描述与说明
>     *

ark_platform_adapt:

>       * 调用update_extrainfo接口后, 更新的额外信息会被写入运行脚本同目录下extra_info.txt文件
>     *

ark_buffer:

>       * 新增支持创建Orion DMABuffer, 在创建对象时通过buffer_type指定类型, 默认为BufferType.ARKC_BUFFER(即之前版本所用buffer)
>     *

ark_std_cmd:

>       *

ark_emmc_std_cmd:

>         * 与buffer组件变动适应, 支持传入BufferType.ARKC_BUFFER和BufferType.ORION_BUFFER
>       *

ark_usb_std_cmd:

>         * 新增get_cmd_exec_info接口, 用于获取命令执行时间
>     *

ark_device:

>       *

ark_device_usb:

>         * 新增支持DM5216F, DM5220主控获取私有smart信息
>       *

ark_device_sd:

>         * 修复速度切换异常问题
>   *

解决BUG

>     *

ark_platform_adapt:

>       * 解决热启动case分布式执行中节点异常重启的问题(ORION-1006)
>     *

ark_recorder:

>       * 新增适配GL860记录仪(ORION-992)
>   *

其他

>     * 更新环境部署文档中在线安装部分Orion_ark工具下载地址以及步骤3细节
>     * 环境部署时指定numpy依赖库版本号, 避免兼容性问题
>

## V2.4.4 2025-09-15
>   *

更新组件

>     *

ark_oven:

>       * 移除套接字setsockopt的过早调用, 防止AttributeError异常
>     *

ark_logging:

>       * 将pack_logs接口的超时时间延长至120s, 提升大日志量等环境下的兼容性
>   *

解决BUG

>     *

ark_usb_std_cmd:

>       * 修复link reset相关异常(ORION-927)
>     *

ark_buffer:

>       * 修复fill_data函数在填充圈数信息时出现的数据异常问题(ORION-944)
>     *

ark_platform_adapt:

>       * 解决环境包安装时间超过10min导致分布式执行超时的问题
>   *

其他

>     * arkC更新至1.1.8版本
>     * 优化框架环境部署流程, 修复config组件初始化异常问题
>     * 增加自动在线授权流程, 可参考ORION官网安装配置页面的授权部分
>

## V2.4.3 2025-09-03
>   *

更新组件

>     *

ark_adaptation_tool:

>       * 增加VTE和混合超稳自动化工具的代码适配
>     *

ark_buffer:

>       * 更新组件接口注释, 描述更加详细
>     *

ark_logging:

>       * 废弃record_comparison_data接口, 改用record_buffer接口记录二进制源数据和目标数据, 详细说明见接口文档, 若有使用旧接口请尽快迁移
>     *

ark_std_cmd:

>       *

ark_usb_std_cmd:

>         * 废弃set_stl函数, 改为使用set_sel接口, 请尽快更新现有用例
>         * 新增ata_pass_through12/16命令, 支持与ATA桥接设备交互(ORION-929)
>       *

ark_emmc_std_cmd:

>         * 新增支持get_info接口获取vu smart(0x63)信息(ORION-933)
>     *

ark_power:

>       * 修复pwrtest接口睡眠功能的兼容性问题
>   *

解决BUG

>     *

ark_usb_std_cmd:

>       * 修复ark_driver下request命令异常打印问题(ORION-935)
>

## V2.4.2 2025-08-19
>   *

更新组件

>     *

ark_std_cmd:

>       * ark_usb_cmd修改read32、synchronize_cache10命令结构体以与协议保持一致, 新增synchronize_cache10接口
>     *

ark_platform_adapt:

>       * 修改与新增由平台部提供的ATMS对接相关接口, 具体使用方式可参照接口文档
>     *

ark_oven:

>       * 新增工厂类network_temp_chamber_zz(众志温箱TCP通信)和mock_temp_chamber(模拟温箱数据), oven组件配置新增对上述两类温箱的支持
>     *

ark_device:

>       *

ark_device_usb:

>         * 新增get_info接口basic和speed的实现, 可获取USB设备(USB、PSSD)的基本信息与速度信息(ORION-842)
>         * 新增get_info接口std_smart和vu_smart的实现, 目前支持TL300、DM2320AB、MAP1202、MAS1102主控PSSD的标准及私有SMART获取, 具体使用方式可参照device组件示例程序(ORION-846)
>       *

ark_device_emmc:

>         * 新增get_info接口basic和speed的实现, 支持获取扇区数、扇区大小及连接速度
>         * reset接口新增硬件复位(hard reset)支持
>         * 新增cmdq相关接口实现
>     *

ark_std_cmd:

>       * ark_emmc_cmd: 新增boot信息获取接口, 具体使用方式可参照示例程序
>     *

ark_camera:

>       * 适配相机辅助UI工具, 支持其所需功能
>   *

解决BUG

>     *

ark_std_cmd:

>       * ark_usb_cmd: 修复UDisk重复SET INTERFACE后发送命令失败(error code: -1)的问题(ORION-871)
>     *

ark_file_operation:

>       * 修复物理设备获取逻辑, 支持mmc与nvme格式(ORION-876)
>     *

ark_oven:

>       * 修复interface中get_run_state接口的非法实现问题
>     *

ark_logging:

>       * 修复多独立进程写入轮换日志时出现权限不足的问题
>     *

ark_power:

>       * 修复功耗仪连接、断连等接口导致的功耗工具异常问题
>   *

其他

>     * arkC更新至1.1.7版本。
>     * 完善ORION网页帮助文档, 更新ORION网页授权工具网址
>

## V2.4.1 2025-06-30
>   *

更新组件

>     *

ark_ape, ark_ipc, ark_dvr:

>       * ark_ape、ark_ipc 和 ark_dvr组件正式发布, 具体使用方式请参阅接口文档及示例程序
>     *

ark_notify:

>       * 新增通知组件, 支持钉钉工作通知、群聊通知及邮件通知等多种方式, 具备消息分级处理、超链接支持、模板渲染与自动重试功能, 适用于多种业务场景
>     *

ark_buffer, ark_sector_operation:

>       * ark_buffer与ark_sector_operation组件现统一基于arkC实现, Windows系统不再使用Python版本, 性能提升80%
>     *

ark_std_cmd:

>       * ark_sd_cmd: 新增SD标准命令适配接口, 支持SD卡相关测试, 具体接口请参阅接口文档
>       * ark_usb_cmd: 修复bulk_only_read函数返回值数量不一致的问题, 统一超时时间单位为微秒(us)
>     *

ark_config:

>       * get_parameter接口的parameter_name参数新增默认值None, 未传参时可返回全部配置信息
>     *

ark_device:

>       * switch_driver_type接口的driver_type参数和switch_transfer_type接口的transfer_type参数新增默认值None, 支持省略传参, 同时兼容旧的传参方式
>       * 新增SD卡的device相关接口实现, 完善对SD设备的支持
>     * beta版本功能纳入正式版本
>

  *

beta-V2.4.0.1 2025.06.11

    * 修复device组件工厂导入方式不当导致脚本运行过程中卡死的问题(ORION-835)


## V2.4.0 2025-06-06
>   *

更新组件

>     *

ark_std_cmd:

>       * emmc_std_cmd新增RPMB相关操作接口, 并对cmd01_till_ready、emmc_switch、emmc_set_blocklen接口进行了修改, 具体使用方式可参阅接口文档
>       * usb_std_cmd的write_and_verify接口更名为write_and_verify10, 原接口仍保留, 建议切换使用
>     *

ark_config:

>       * 配置组件新增适配Python配置文件, 同时保持向前兼容以支持本地配置读取, 具体使用方式可参照示例程序
>     *

ark_logging:

>       * 日志文件命名中的时间戳精度提升至毫秒(ms)级, pack_logs函数新增线程锁机制, 提升多线程环境下的稳定性
>     *

ark_file_operation:

>       * device_partition接口现支持传入逻辑盘符, 增强分区操作的灵活性
>   *

解决BUG

>     *

ark_buffer:

>       * 修复fill_data函数在填充数据类型为DataType.DATA_DECREMENTAL.value时出现的数据异常问题
>     *

ark_device:

>       * 修复switch_driver_type接口切换驱动类型为orion_driver时, 因未加载相应模块导致的切换失败问题(ORION-818)
>     *

ark_power:

>       * 修复power_connect接口中的驱动切换逻辑异常, 导致power组件使用异常的问题(ORION-785)
>     *

ark_file_operation:

>       * 修复device_partition接口在特定情况下分区结果判断存在的不兼容问题(ORION-795)
>   * beta版本功能纳入正式版本
>

  *

beta-V2.3.0.1 2025.05.30

    * files_operation组件添加device_clean_partition接口
    * config组件不再具有本地配置概念


## V2.3.0 2025-05-14
>   *

更新组件

>     *

ark_std_cmd:

>       * usb_std_cmd新增send_cmd衍生接口: send_cmd_write、send_cmd_read、send_cmd_execute_without_data, 具体接口定义与使用方式请参阅接口文档
>       * 新增sd_std_cmd模块, 支持对SD卡的标准命令操作
>     * ark_camera: 适配尼康相机
>     * ark_logging: 优化日志打包接口pack_logs的时间精度, 提升至微秒(µs)级别
>

## V2.2.1 2025-04-30
>   *

更新组件

>     *

ark_std_cmd:

>       * emmc_std_cmd针对emmc测试需求进行功能完善, 具体接口及使用方式可参阅接口文档
>     * ark_device: 新增open, close, device_init, read, write, erase, erase_all, speed接口实现, 上述接口适用于 USB 与 eMMC 产品, 具备通用性, 详细使用方式可参考组件示例程序
>

## V2.2.0 2025-04-17
>   *

更新组件

>     * ark_config: 通过文件更新配置接口新增支持ini和json格式文件
>     * ark_camera: 适配索尼相机
>     *

ark_std_cmd:

>       * emmc_std_cmd新增open和close函数, open函数用于初始化相关资源并返回操作句柄, close函数用于释放句柄
>       * emmc_std_cmd其余函数的参数进行了调整, 需要传入句柄, 需注意接口不兼容问题
>   *

解决BUG

>     * ark_buffer: 修复copy函数异常问题, arkC更新至V1.1.5可解决(该版本支持自动从服务器拉取包进行arkC更新)
>

## V2.1.0 2025-04-14
>   *

新增功能：

>     * ark.init接口支持从Orion服务器拉取Orion_ark运行环境依赖包, 并进行安装
>     * Orion网站正式上线, 支持在线查看Orion_ark文档
>     * 后续采用通过Orion网站(<http://orion.longsys.com>)下载Orion_ark包, 用户下载时选择使用的ark配置, 运行过程中将强制使用所选配置
>     * 更新安装和指导文档, 详情请在Orion网站查看
>   *

更新组件：

>     * ark_sector_operation: 新增get_device_capacity接口, 可用来获取设备容量和扇区大小
>     * ark_power: 修改超稳高速板power_connect函数, 新增power_disconnect函数实现, 需注意接口兼容性问题
>     * ark_std_cmd: emmc接口修改参数, 去掉blk_len和is_high_capacity字段, 需注意接口兼容性问题
>   *

解决BUG:

>     * ark_platform_adapt: 解决分布式显示持续测试时间到达24小时会重置问题
>     * ark_driver: 解决Ubuntu环境无法正常使用问题, 注: 支持ubuntu16.8及其以后版本
>   * beta版本功能纳入正式版本
>

  *

beta-v2.0.2.1 2025.04.01

    * ark.init接口返回err_ok
    * scsi命令format unit原接口变更为format_unit_ufi, 接口参数有变动; 增加SBC协议接口format_unit
    * camera组件适配富士相机


## V2.0.2 2025-03-21
>   * Orion_ark由开发框架升级为测试框架且向前兼容, 用户可参考demo使用新用法或者维持之前用法。注: 升级后用例不再需要test_base.py文件
>   * beta版本功能纳入正式版本
>

  *

beta-v2.0.1.25 2025.03.19

    * Resolve requirement: emmc标准命令接口优化
  *

beta-v2.0.1.24 2025.03.15

    *

Resolve requirement: 佳能相机半自动化交付

      * 完成camera组件重构
      * 支持用例接入分布式
      * 支持格式化、设置图片格式、拍照、录像、文件处理、视频检测等功能
  *

beta-v2.0.1.23 2025.03.11

    * Resolve requirement: ark_platform_adapt组件适配CI
    * Resolve requirement: ORION-637 “【移动存储】+【需求】Orion自动化工具运行界面提示”
  *

beta-v2.0.1.22 2025.03.07

    * Resolve issues: ORION-648 “Orion测试 执行卸载操作后, 卸载成功后脚本就一直卡住了”
  *

beta-v2.0.1.21 2025.02.25

    * Resolve issues: ORION-627 “重复实例化ark对象打开设备切换驱动后driver_fd为None”
    * Resolve issues: ORION-632 “执行打开device并切换驱动后会导致终端出现重复打印”
    *

The following components are update

      * ark_appium: V1.0.1、V1.0.2
      * ark_file_operation: V1.0.3、V1.0.4
  *

beta-v2.0.1.20 2025.02.19

    * Resolve issues: ORION-616
    * Resolve issues: ORION-617
    * Resolve issues: ORION-619


## V2.0.1 2025-01-03
  * Resolve issues with abnormal usage of the std_cmd component in a native driver environment
  * Resolve issues related to abnormal power-on and power-off in a native driver environment
  *

The following components are optimized in this version:

    * ark_drive: UASP supports streams
  *

The following optimization is realized

    * The structure of integration test cases has been optimized, and users can refer to read10 for case development


## V2.0.0 2024-12-07
  * Warning: Due to architectural adjustments, the current version is not forward-compatible
  * Add an authorization verification feature, allowing users to choose between offline or online authorization
  * Added Ark Drive, when users select Ark Drive, it supports the execution of integrated test cases via the UAS protocol on the 3720, 1296, and Ubuntu platforms
  *

The following components are optimized in this version:

    * ark_power: aAdapt to power analyzer
    * ark_camera: The functions have been re-examined and the design has undergone refactoring
  *

The following components are added

    * ark_appium
    * ark_adb
    * ark_adaptation_tool
  *

The following optimization is realized

    * The error codes have been reviewed, with a reduction in their number and clearer definitions of their meanings


## V1.2.2 2024-10-29
  *

The following components are perfected in this version:

    * ark_std_cmd: all SCSI protocol interfaces in the PRD are encapsulated
    * ark_buffer: Added the set_ddword and get_ddword interfaces
  *

The following test cases are added

    * Complete all the use case development of this Stage goal
  *

The following optimization is realized

    * if the Ark configuration field is added in the version iteration, the system is automatically updated


## V1.2.1 2024-10-15
  *

The following components are optimized in this version:

    * ark_std_cmd
  *

The following test cases are added

    * bulk only protocol test cases
    * some read6 test cases
  *

The following bug are fixed

    * Fixed the request sense length error


## V1.2.0 2024-10-07
  *

The following components are optimized in this version:

    * ark_file_operation
    * ark_power
    * ark_sector_operation
    * ark_std_cmd
    * ackC
  *

181 test cases were developed based on this version

    * There are 131 SCSI M cases
    * There are 50 SCSI O cases
  *

Output the following integration test case report

    * Completed the SCSI M type protocol test report of 4 competing products
    * Completed the SCSI O type protocol test report of 2 competing products


## V1.1.2 2024-08-31
  *

The following components are added in this version:

    * ark_std_cmd
  *

The following Orion_ark’s developer accessibility features are supported

    * Pack exe executables with pyinstall in one click
    * Package Orion ark so it can be used directly as a python plugin
  *

Fixed the following bugs

    * Repeated calls to init interface trigger the program to exit abnormally


## V1.1.1 2024-08-20
  *

The following components are added in this version:

    * ark_device
    * ark_vu_cmd
    * ark_camera
    * arkC
  * Implement the requirements of buffer component for TL300 project
  * Optimize the test base class, format logging and record ark and ark component versions
  *

The following Orion_ark’s developer accessibility features are supported

    * Automatically update test base files in all applications


## V1.1.0 2024-07-29
  *

The following components are added in this version:

    * ark_buffer
    * ark_config
    * ark_power
    * ark_sector_operatiion
    * ark_task_mgr
    * ark_upgradation
  *

The following Orion_ark’s developer accessibility features are supported

    * Supports automatic run unit testing
    * Supports automatic run interface testing
    * Supports automatic package script


## V1.0.0 2024-05-14
  *

The initial version supports the following components:

    * ark_common
    * ark_file_operation
    * ark_logging
    * ark_oven
    * ark_platform_adapt
    * ark_protocol_adapt
  *

The following orion_ark’s developer accessibility features are supported

    * Supports automatic generation/delete of description documents
    * Supports automatic generation/delete of unit test reports and code coverage
    * Supports automatic delete all logs
