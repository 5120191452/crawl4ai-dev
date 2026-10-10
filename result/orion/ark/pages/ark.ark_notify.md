---
title: "ark.ark_notify package"
docname: "ark.ark_notify"
source: "http://orion.longsys.com/ark.ark_notify.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_notify package
## Module contents
@Module : ark_notify
@Date : 2026/09/7
@Version : V1.1.0
Orion Notify supports DingTalk work and group notifications, signed Feishu group bot notifications, and email notifications. It provides message levels, multi-channel routing, message rendering, error handling, and automatic retry.
Updates: - Added signed Feishu group bot notifications. - Added automatic Feishu Webhook detection and signature generation. - Supported DingTalk, Feishu, and email notifications in the same request. - Preserved compatibility with existing interfaces and DingTalk formats. - Reserved a TODO interface for Feishu personal notifications. - Added Feishu and multi-channel dispatch tests.
Note: The component guarantees only that requests are successfully sent to the service endpoint, not that messages are delivered to recipients.
Feishu receivers must use the following signed Webhook format:
> secret:https://open.feishu.cn/xxx
