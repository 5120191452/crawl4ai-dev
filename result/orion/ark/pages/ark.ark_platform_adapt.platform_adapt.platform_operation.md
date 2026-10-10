---
title: "ark.ark_platform_adapt.platform_adapt.platform_operation package"
docname: "ark.ark_platform_adapt.platform_adapt.platform_operation"
source: "http://orion.longsys.com/ark.ark_platform_adapt.platform_adapt.platform_operation.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_platform_adapt.platform_adapt.platform_operation package
## Submodules
## ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common module

_class _ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common.ArkPlatformAdaptCommon(_* args_, _** kwargs_)

Bases: [`ArkPlatformAdaptInterface`](ark.ark_platform_adapt.platform_adapt.md#ark.ark_platform_adapt.platform_adapt.ark_platform_adapt_interface.ArkPlatformAdaptInterface "ark.ark_platform_adapt.platform_adapt.ark_platform_adapt_interface.ArkPlatformAdaptInterface")

download_artifact(_name_ , _version =None_, _save_dir =None_)


Brief:

Download a specific artifact from the Orion server according to its name and version, and save to the specified path.

Parameters:

  * **name** – str, Name of the artifact to download (e.g. “APE_Protocol_Parser”, “ppocr_v4”, “OrionMCU”).
  * **version** – str, Version nubmer of the artifact to download (e.g. “1.0.0”). If None, the client will request the latest release version of the specified artifact from the Orion server.
  * **save_dir** – str, Target directory to save the downloaded artifact. If None, the current working directory will be used.


Returns:

Error code. 0 indicates success, non-zero indicates failure. file_path: Absolute path of the downloaded artifact when the operation succeeds; None if the download fails.

download_ci_logs(_sample_id_ , _ci_log_)


download_dts_logs(_sample_id_)


Brief:

Download logs according to the specified SID.

Parm sample_id:

SID

Returns:

The directory where the downloaded logs are stored.

download_task_case_attachment(_attachment_id_)


finished()


Brief:

Notify the platform that the test is complete

Returns:

None

get_artifact_info(_name_) → Tuple[int, [ArtifactInfo](ark.ark_platform_adapt.platform_adapt.md#ark.ark_platform_adapt.platform_adapt.ark_platform_adapt_interface.ArtifactInfo "ark.ark_platform_adapt.platform_adapt.ark_platform_adapt_interface.ArtifactInfo") | None]


Brief:

Query detailed metadata of all available versions of a specific artifact (e.g. tool package, model file, or image) from the Orion server.

Parameters:

**name** – str, Name of the artifact to query (e.g. “APE_Protocol_Parser”, “ppocr_v4”, “OrionMCU”).

Returns:

Error code. 0 indicates success, non-zero indicates failure.
artifact_info: Optional[ArtifactInfo], Detailed information of the specified artifact, None if the query fails or the artifact does not exist.
> ArtifactInfo: {name: str, versions_info: list[ArtifactVersionInfo]}
> ArtifactVersionInfo: {version: str, status: Literal[“Release”,”EVT”,”Beta”], update_time: str, description: str}

get_case_list(_plan_task_id_)


Brief:

Get information about all test cases under the specified task.

Parm plan_task_id:

Task ID

Returns:

list[TaskCase]: Information about all test cases under the specified task.

get_case_result_description(_task_id_)


get_cases_jira(_task_ids_)


get_cfg_path()


Brief:

Obtain the configuration file path.

Returns:

str

get_device()


Brief:

This function is to get device path.

Returns:

str

get_plan_task_list()


Brief:

Get information about all tasks under the plan.

Returns:

list[PlanTask]: Task list.

get_plugin_info()


get_project_info()


Brief:

Get information about the project.

Returns:

list[ProjectInfo]: Project Information.

get_project_product_info()


get_sample_results(_task_case_id_ , _pipeline_map_)


Brief:

Getting information about the execution of a specified test case.

Parm task_case_id:

Case ID

Parm pipeline_map:

PipelineInfo

Returns:

list[SampleResult] Test Case Information.

get_standard()


init(_tool_name_)


Brief:

Initialize the module according to the configuration parameters and connect the module to the corresponding external platform clients

Parm:

tool_name:The default is None. If the tool name is passed and there is a feature in the configuration file to display the tool testing progress, the name will be displayed in this UI.

Returns:

errcode

is_started_by_platform()


Brief:

Checks if the current instance or process was started by the platform.

Returns:

Bool - Returns True if started by the platform, False otherwise.

is_stop()


Brief:

Checks if a stop request has been received from the platform.

Returns:

Bool - Returns True if a stop request has been received, False otherwise.

restart()


Brief:

Restarts the current instance or process.

Returns:

None - It simply tells the platform that it is about to restart, but does not perform the restart operation

show_window()


update_extraInfo(_key_ , _value_)


Brief:

Update additional information with a specified key-value pair

Parm key:

The key for the extra information to be updated

Parm value:

The value associated with the provided key

Returns:

None

update_progress(_cur_cycle_ , _cur_progress_ , _total_progress_ , _speed =''_)


Brief:

Update the progress information

Parm cur_cycle:

Current cycle or iteration number

Parm cur_progress:

Current progress within the current cycle

Parm total_progress:

Total progress across all cycles

Parm speed:

Progress speed or rate

Returns:

None

update_progress_text(_cur_cycle_ , _cur_progress_ , _total_progress_ , _speed =''_)


update_report_file(_report_file_path_)


Brief:

Checks if the current instance or process was started by the platform.

Parm report_file_path:

Path to the final test report file generated by the script execution, if there are more than one, please compress it in zip format.

update_runtime()


update_status(_status_ , _err_code_ , _err_count_)


Brief:

Update the status information

Parm status:

The new status to be updated

Parm err_code:

The error code associated with the status update

Parm err_count:

The count of errors encountered during the status update

Returns:

None

update_text(_info_)


_class _ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common.ShowWindowType(_value_)

Bases: `Enum`
An enumeration.

close_when_finished _ = 'ShowWindowType_close_when_finished'_

## ark.ark_platform_adapt.platform_adapt.platform_operation.longsys_ci_system module

_class _ark.ark_platform_adapt.platform_adapt.platform_operation.longsys_ci_system.LongsysCiSystem(_* args_, _** kwargs_)

Bases: [`ArkPlatformAdaptCommon`](ark.ark_platform_adapt.platform_adapt.platform_operation.md#ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common.ArkPlatformAdaptCommon "ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common.ArkPlatformAdaptCommon")

download_ci_logs(_sample_id_ , _ci_log_)


download_dts_logs(_sample_id_)


Brief:

Download logs according to the specified SID.

Parm sample_id:

SID

Returns:

The directory where the downloaded logs are stored.

download_task_case_attachment(_attachment_id_)


finished()


Brief:

Notify the platform that the test is complete

Returns:

None

get_case_list(_plan_task_id_)


Brief:

Get information about all test cases under the specified task.

Parm plan_task_id:

Task ID

Returns:

list[TaskCase]: Information about all test cases under the specified task.

get_case_result_description(_task_id_)


get_cases_jira(_task_ids_)


get_plan_task_list()


Brief:

Get information about all tasks under the plan.

Returns:

list[PlanTask]: Task list.

get_plugin_info()


get_project_info()


Brief:

Get information about the project.

Returns:

list[ProjectInfo]: Project Information.

get_sample_results(_task_case_id_ , _pipeline_map_)


Brief:

Getting information about the execution of a specified test case.

Parm task_case_id:

Case ID

Parm pipeline_map:

PipelineInfo

Returns:

list[SampleResult] Test Case Information.

init(_tool_name =None_)


Brief:

Initialize the module according to the configuration parameters and connect the module to the corresponding external platform clients

Parm:

tool_name:The default is None. If the tool name is passed and there is a feature in the configuration file to display the tool testing progress, the name will be displayed in this UI.

Returns:

errcode

update_report_file(_report_file_path : str_)


Brief:

Checks if the current instance or process was started by the platform.

Parm report_file_path:

Path to the final test report file generated by the script execution, if there are more than one, please compress it in zip format.
## ark.ark_platform_adapt.platform_adapt.platform_operation.longsys_distributed_system module

_class _ark.ark_platform_adapt.platform_adapt.platform_operation.longsys_distributed_system.LongsysDistributedSystem(_* args_, _** kwargs_)

Bases: [`ArkPlatformAdaptCommon`](ark.ark_platform_adapt.platform_adapt.platform_operation.md#ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common.ArkPlatformAdaptCommon "ark.ark_platform_adapt.platform_adapt.platform_operation.ark_platform_adapt_common.ArkPlatformAdaptCommon")

finished()


Brief:

Notify the platform that the test is complete

Returns:

None

get_cfg_path()


Brief:

Obtain the configuration file path.

Returns:

str

get_device()


Brief:

This function is to get device path.

Returns:

str

get_standard()


init(_tool_name =None_)


Brief:

Initialize the module according to the configuration parameters and connect the module to the corresponding external platform clients

Parm:

tool_name:The default is None. If the tool name is passed and there is a feature in the configuration file to display the tool testing progress, the name will be displayed in this UI.

Returns:

errcode

is_started_by_platform()


Brief:

Checks if the current instance or process was started by the platform.

Returns:

Bool - Returns True if started by the platform, False otherwise.

is_stop()


Brief:

Checks if a stop request has been received from the platform.

Returns:

Bool - Returns True if a stop request has been received, False otherwise.

restart()


Brief:

Restarts the current instance or process.

Returns:

None - It simply tells the platform that it is about to restart, but does not perform the restart operation

update_extraInfo(_key_ , _value_)


Brief:

Update additional information with a specified key-value pair

Parm key:

The key for the extra information to be updated

Parm value:

The value associated with the provided key

Returns:

None

update_progress(_cur_cycle_ , _cur_progress_ , _total_progress_ , _speed =''_)


Brief:

Update the progress information

Parm cur_cycle:

Current cycle or iteration number

Parm cur_progress:

Current progress within the current cycle

Parm total_progress:

Total progress across all cycles

Parm speed:

Progress speed or rate

Returns:

None

update_status(_status_ , _err_code_ , _err_count_)


Brief:

Update the status information

Parm status:

The new status to be updated

Parm err_code:

The error code associated with the status update

Parm err_count:

The count of errors encountered during the status update

Returns:

None

write_extraInfo(_text_)

## Module contents
