# Orion Ark MCP

`orion-ark-mcp` 是一个只读的 Orion Ark 接口检索与选型服务。它把 Crawl4AI
生成的 103 页 Markdown 快照转换成结构化 SQLite 索引，并通过 MCP 提供接口
搜索、接口详情、场景推荐、示例检索和原始文档资源。

项目目录使用标准的 kebab-case 名称 `orion-ark-mcp`，Python 包名为
`orion_ark_mcp`。

## 能力

- 校验抓取快照完整性后再构建索引；
- 提取类、枚举、函数、普通/抽象/静态/类方法；
- 精确接口名搜索及 SQLite FTS5 中英文检索；
- 按设备读写、Buffer、文件、电源、移动端、相机、Appium、协议命令等场景推荐；
- 返回签名、参数、返回值、可见性、平台、版本和原始来源；
- 折叠 Sphinx 导出别名，避免推荐重复接口；
- 所有 MCP Tool 均标记为只读、closed-world。

服务不会导入或执行 Orion Ark，不连接设备，也不会执行写入、擦除、上下电或
升级操作。

## 项目结构

```text
orion-ark-mcp/
├── data/                       # 生成的 SQLite 索引
├── docs/ARCHITECTURE.md
├── examples/mcp-client.json
├── src/orion_ark_mcp/
│   ├── parser.py               # Sphinx Markdown 结构化解析
│   ├── store.py                # 原子构建及只读 SQLite/FTS 查询
│   ├── service.py              # 检索、详情和场景推荐
│   ├── scenarios.json          # 可审查的场景知识
│   ├── server.py               # MCP Tools 和 Resources
│   └── cli.py
└── tests/
```

## 安装

在仓库根目录执行：

```bash
.venv/bin/pip install -e './orion-ark-mcp[dev]'
```

也可以在 `orion-ark-mcp` 目录中使用独立的 `uv` 环境：

```bash
uv sync --extra dev
```

要求 Python 3.10+，并依赖官方 `mcp` Python SDK 2.x。

## 构建索引

现有抓取结果位于 `result/orion/ark`：

```bash
orion-ark-mcp build-index --docs result/orion/ark
orion-ark-mcp status
```

如果从 `orion-ark-mcp` 目录执行，使用 `../result/orion/ark`。默认数据库为
`orion-ark-mcp/data/orion_ark.db`。也可通过全局参数 `--db` 或环境变量
`ORION_ARK_MCP_DB` 指定。

文档更新流程：

```bash
.venv/bin/python orion/ark.py
orion-ark-mcp build-index --docs result/orion/ark
```

构建过程先写临时数据库，完成完整性检查后再原子替换当前索引。

## 本地查询

```bash
orion-ark-mcp search cmdq_send
orion-ark-mcp get ark.ark_device.device.ark_device_interface.ArkDeviceInterface.cmdq_send
orion-ark-mcp recommend '对存储设备进行随机读写并校验数据' \
  --platform emmc --device-type storage
orion-ark-mcp recommend 'Android手机拍照后统计新增图片' \
  --platform android --device-type phone
```

## MCP Tools

| Tool | 说明 |
| --- | --- |
| `ark_status` | 查看索引版本、快照时间和数量 |
| `list_ark_components` | 列出组件及接口数量 |
| `search_ark_interfaces` | 搜索接口和能力 |
| `get_ark_interface` | 获取接口完整详情和来源 |
| `recommend_ark_interfaces` | 根据任务推荐接口、前置条件和调用阶段 |
| `get_ark_examples` | 查找接口示例与相关文档片段 |

MCP Resources：

- `ark://docs/<docname>`：103 个预注册的完整 Markdown 文档；
- `ark://catalog/components`：组件目录。

接口结构化详情由 `get_ark_interface` 提供，避免把 1,800 多条 API 全部加入
Resource 列表。

服务会在 MCP 初始化时向客户端提供调用说明：当问题实质涉及 Orion Ark（包括
Orion、Ark、Ark SDK/API）的接口、用法、参数或版本核对、接口选型、示例或相关开发时，
优先使用最相关的工具；只在无关语境里顺带出现这些词时不触发。这是客户端的工具选择提示，
是否调用仍由客户端决定。

## 启动 MCP

本地客户端推荐 stdio：

```bash
orion-ark-mcp serve --transport stdio
```

客户端配置模板见 [examples/mcp-client.json](examples/mcp-client.json)。将其中的
可执行文件和数据库改为绝对路径。

同一局域网内的其他电脑访问时，服务端必须监听所有网卡，而不是只监听
`127.0.0.1`：

```bash
.venv/bin/orion-ark-mcp \
  --db orion-ark-mcp/data/orion_ark.db \
  serve --transport streamable-http \
  --host 0.0.0.0 --path /mcp
```

HTTP 默认端口是 `9000`；需要临时使用其他端口时再传入 `--port`。

`0.0.0.0` 只用于服务端监听，客户端不能把它当作连接地址。客户端应填写
服务端的实际局域网 IP，例如：

```json
{
  "mcpServers": {
    "orion-ark": {
      "type": "http",
      "url": "http://10.2.18.39:9000/mcp"
    }
  }
}
```

不同 MCP 客户端的配置字段可能不同；有些客户端只需要 `url`，不接受
`type`。可移植模板见
[examples/mcp-client-remote.json](examples/mcp-client-remote.json)。远程客户端不再
填写服务端的 `command`、`args`、虚拟环境路径或数据库路径。

如果服务器 IP 由 DHCP 分配，它以后可能发生变化。长期使用时应给服务器配置
固定地址或局域网 DNS 名称。该 HTTP 服务目前没有身份认证，只应在可信内网中
使用；不要把 9000 端口直接映射到公网。

## 测试

```bash
.venv/bin/python -m pytest orion-ark-mcp/tests -q
```

测试覆盖真实 103 页快照构建、接口解析、精确搜索、场景推荐、版本提示和
MCP Tools/Resources 的进程内调用。

## 安全说明

文档包含内部地址、授权流程和设备操作接口：

- 不要将数据库或 HTTP 服务暴露到公网；
- 远程部署必须放在带身份认证、访问控制和审计的内网网关后；
- Tool annotations 只是客户端提示，不是安全边界；
- 推荐结果是文档证据驱动的候选方案，破坏性操作前必须人工核对参数、设备和版本。

更详细的边界与数据流见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。
