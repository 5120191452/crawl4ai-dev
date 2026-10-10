---
title: "ark.ark_task_mgr.task_mgr package"
docname: "ark.ark_task_mgr.task_mgr"
source: "http://orion.longsys.com/ark.ark_task_mgr.task_mgr.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_task_mgr.task_mgr package
## Submodules
## ark.ark_task_mgr.task_mgr.ark_task_mgr_factory module

_class _ark.ark_task_mgr.task_mgr.ark_task_mgr_factory.ArkTaskMgrFactory(_* args_, _** kwargs_)

Bases: `object`
Responsible for controlling the ArkTaskMgr. it dynamically selects the appropriate adapter based on the type of oven provided and delegates the temperature control and other related operations to the selected adapter.

create_object()


Brief:

Initialising objects(based on temperature control equipment types)

Returns:

Success returns the corresponding object, failure returns None.
## ark.ark_task_mgr.task_mgr.ark_task_mgr_interface module

_class _ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface

Bases: `ABC`

_abstract _dispatch_init(_max_thread_cnt_ , _dispatch_type_)

:brief:Initialize the object with maximum thread count and dispatch type. :param max_thread_cnt: The maximum number of threads that can be used for dispatching tasks. :param dispatch_type: The type of dispatch mechanism to be used, which determines how tasks are distributed. :return: None

_abstract _max_thread_cnt_change(_max_thread_cnt_)


Brief:

modify the number of tasks that can be performed in parallel in the current running queue

Parameters:

**max_thread_cnt** – type: (int) The number of tasks that can be parallel

Returns:

errcode

_abstract _package_complete(_package_)


Brief:

Add the combined commands and corresponding parameters to the command execution queue

Parameters:

**package** – The package object to which the member will be added.

Returns:

task_package

_abstract _package_create(_package_type_)

:brief:Merge the corresponding module with the task to be run to form the corresponding task member and store it in the task list :param package_type: package type :return: package

_abstract _package_member_add(_package_ , _** packet_member_)


Brief:

Adds a member to the package.

Parameters:

  * **package** – The package object to which the member will be added.
  * **packet_member** – The member object that will be added to the package.


Returns:

err_code

_abstract _package_member_clear(_package_)


Brief:

Clears the members of the package. This method is responsible for clearing or resetting the members of the package.

Parameters:

**package** – The package object to which the member will be added.

Returns:

errcode

_abstract _package_member_remove(_package_ , _packet_member_)


Brief:

Delete the task to task_id from the execution queue, return the execution status, and log the related information

Parameters:

  * **package** – The package object to which the member will be added.
  * **packet_member** – TThe member object that will be delete to the package.


Returns:

errcode

_abstract _stop()


Brief:

modify the number of tasks that can be performed in parallel in the current running queue

Returns:

errcode

_abstract _task_add(_task_package_ , _task_latency =None_)


Brief:

Add a task to the dispatch

Parameters:

  * **task_package** – The package containing the details and data of the task to be added
  * **task_latency** – Optional. The expected latency for the task to be completed. Defaults to None.


Returns:

errcode

_abstract _task_delete(_task_id_)


Brief:

Delete the task to task_id from the execution queue, return the execution status, and log the related information

Returns:

errcode

_abstract _task_move(_move_forward_ , _step_length_ , _task_id_)


:brief:Change the position of the target task in the queue.

If the task moves forward more than the last bit in the queue, the task is placed at the last bit in the queue. If the task moves forward more than the 0th bit in the queue, the Task is placed at the 0th bit in the queue

Parameters:

  * **move_forward** – target task Select the operation that moves the task forward or backward
  * **step_length** – target task move step length
  * **task_id** – target task ID num


Returns:

errcode

_class _ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.DispatchType(_value_)

Bases: `Enum`
Supported types are DispatchType

basic_dispatch _ = 1_


_class _ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.PackageType(_value_)

Bases: `Enum`
Supported types are sample Function Pack

file_Package _ = 2_


function_Package _ = 1_

## Module contents
@Module : ark_task_mgr
@Date : 2024/06/27
@Version : V1.0.0
ark_task_mgr main function of the task scheduling module is to manage and allocate system resources to ensure that tasks are executed according to priority and scheduling policies. Stores the tasks to be executed, sorting them by priority or other scheduling policies.
