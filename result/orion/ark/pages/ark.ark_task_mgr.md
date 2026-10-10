---
title: "ark.ark_task_mgr package"
docname: "ark.ark_task_mgr"
source: "http://orion.longsys.com/ark.ark_task_mgr.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_task_mgr package
## Subpackages
  * [ark.ark_task_mgr.task_mgr package](ark.ark_task_mgr.task_mgr.md)
    * [Submodules](ark.ark_task_mgr.task_mgr.md#submodules)
    * [ark.ark_task_mgr.task_mgr.ark_task_mgr_factory module](ark.ark_task_mgr.task_mgr.md#module-ark.ark_task_mgr.task_mgr.ark_task_mgr_factory)
      * [`ArkTaskMgrFactory`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_factory.ArkTaskMgrFactory)
        * [`ArkTaskMgrFactory.create_object()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_factory.ArkTaskMgrFactory.create_object)
    * [ark.ark_task_mgr.task_mgr.ark_task_mgr_interface module](ark.ark_task_mgr.task_mgr.md#module-ark.ark_task_mgr.task_mgr.ark_task_mgr_interface)
      * [`ArkTaskMgrInterface`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface)
        * [`ArkTaskMgrInterface.dispatch_init()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.dispatch_init)
        * [`ArkTaskMgrInterface.max_thread_cnt_change()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.max_thread_cnt_change)
        * [`ArkTaskMgrInterface.package_complete()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.package_complete)
        * [`ArkTaskMgrInterface.package_create()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.package_create)
        * [`ArkTaskMgrInterface.package_member_add()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.package_member_add)
        * [`ArkTaskMgrInterface.package_member_clear()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.package_member_clear)
        * [`ArkTaskMgrInterface.package_member_remove()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.package_member_remove)
        * [`ArkTaskMgrInterface.stop()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.stop)
        * [`ArkTaskMgrInterface.task_add()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.task_add)
        * [`ArkTaskMgrInterface.task_delete()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.task_delete)
        * [`ArkTaskMgrInterface.task_move()`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.ArkTaskMgrInterface.task_move)
      * [`DispatchType`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.DispatchType)
        * [`DispatchType.basic_dispatch`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.DispatchType.basic_dispatch)
      * [`PackageType`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.PackageType)
        * [`PackageType.file_Package`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.PackageType.file_Package)
        * [`PackageType.function_Package`](ark.ark_task_mgr.task_mgr.md#ark.ark_task_mgr.task_mgr.ark_task_mgr_interface.PackageType.function_Package)
    * [Module contents](ark.ark_task_mgr.task_mgr.md#module-ark.ark_task_mgr.task_mgr)


## Module contents
@Module : ark_task_mgr
@Date : 2024/08/18
@Version : V1.0.0
The main function of the task scheduling module is to manage and allocate system resources to ensure that tasks are executed according to priority and scheduling policies. Stores the tasks to be executed, sorting them by priority or other scheduling policies.
