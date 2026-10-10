---
title: "ark.ark_platform_adapt.third_party.longsys_ci_system package"
docname: "ark.ark_platform_adapt.third_party.longsys_ci_system"
source: "http://orion.longsys.com/ark.ark_platform_adapt.third_party.longsys_ci_system.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_platform_adapt.third_party.longsys_ci_system package
## Submodules
## ark.ark_platform_adapt.third_party.longsys_ci_system.orion_ci module

_class _ark.ark_platform_adapt.third_party.longsys_ci_system.orion_ci.OrionCIClient

Bases: `object`

Init()


download_ci_logs(_sample_id : int_, _ci_log_) → str

_summary_

Args:

url (str): log_url

Returns:

str: 下载后的日志存放的目录

download_dts_logs(_sample_id : int_) → str

_summary_

Args:

sample_id (int): _description_

Returns:

str: 下载后的日志存放的目录

download_task_case_attachment(_attachment_id : int_) → str


get_case_list(_plan_task_id : int_) → list[TaskCase]

_summary_

Returns:

list[TaskCase]: _description_

get_case_result_description(_task_id : int_)


get_cases_jira(_task_ids : list[int]_) → dict[int, list[int]]


get_plan_task_list() → list[PlanTask]


get_plugin_info()


get_project_info() → ProjectInfo


get_project_product_info()


get_sample_results(_task_case_id : int_, _pipeline_map_) → list[SampleResult]

_summary_

Args:

task_case_id (int): 任务中用例id

Returns:

list[SampleResult]: _description_

update_report_file(_report_file_path : str_)

_summary_

Args:

report_file_path (str): 脚本执行最终生成的测试报告文件路径，如有多个，请用zip格式压缩

Exceptions:

保存失败时，抛出的异常
## ark.ark_platform_adapt.third_party.longsys_ci_system.orion_ci_mock module

_class _ark.ark_platform_adapt.third_party.longsys_ci_system.orion_ci_mock.OrionCIMockClient

Bases: `object`

_async _download_sample_logs(_sample_id : int_) → str

_summary_

Args:

sample_id (int): _description_

Returns:

str: 下载后的日志存放的目录

_async _get_case_list(_plan_task_id : int_) → list[TaskCase]

_summary_

Returns:

list[TaskCase]: _description_

_async _get_plan_task_list() → list[PlanTask]

_summary_ Returns: list[PlanTask]:_description_

_async _get_project_info() → ProjectInfo


_async _get_sample_results(_task_case_id : int_) → list[SampleResult]

_summary_

Args:

task_case_id (int): 任务中用例id

Returns:

list[SampleResult]: _description_

_async _update_report_file(_report_file_path : str_)

_summary_

Args:

report_file_path (str): 脚本执行最终生成的测试报告文件路径，如有多个，请用zip格式压缩

Exceptions:

保存失败时，抛出的异常
## ark.ark_platform_adapt.third_party.longsys_ci_system.tmss_plan_task module

_class _ark.ark_platform_adapt.third_party.longsys_ci_system.tmss_plan_task.TmssPlanTask

Bases: `object`

_async _download_ci_logs(_sample_id : int_, _ci_log : list[CILogItem]_) → str

_summary_

Args:

url (str): log_url

Returns:

str: 下载后的日志存放的目录

_async _download_sample_logs(_sample_id : int_) → str

_summary_

Args:

sample_id (int): _description_

Returns:

str: 下载后的日志存放的目录

_async _download_task_case_attachment(_attachment_id : int_) → str


_async _get_case_list(_plan_task_id : int_) → list[TaskCase]

_summary_

Returns:

list[TaskCase]: _description_

_async _get_case_result_description(_task_id : int_) → TaskCaseResultDescription

_summary_

Args:

task_id (int): _description_

Returns:

str: 下载后的日志存放的目录

_async _get_cases_jira(_task_ids : list[int]_) → dict[int, list[int]]


_async _get_plan_task_list() → list[PlanTask]

_summary_

Returns:

list[PlanTask]: _description_

_async _get_plugin_info() → ReportPlugin


_async _get_project_info() → ProjectInfo


_async _get_project_product_info()


_async _get_sample_results(_task_case_id : int_, _pipeline_map : dict[str, PipelineInfo]_) → list[SampleResult]

_summary_

Args:

task_case_id (int): 任务中用例id

Returns:

list[SampleResult]: _description_

_async _init_tmss() → bool


_async _update_report_file(_report_file_path : str_)

_summary_

Args:

report_file_path (str): 脚本插件最终生成的测试报告文件路径，如有多个，请用zip格式压缩
Returns:

Exception:

保存失败时，抛出的异常
## Module contents
