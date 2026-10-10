---
title: "ark.ark_file_operation package"
docname: "ark.ark_file_operation"
source: "http://orion.longsys.com/ark.ark_file_operation.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_file_operation package
## Subpackages
  * [ark.ark_file_operation.file_operation package](ark.ark_file_operation.file_operation.md)
    * [Submodules](ark.ark_file_operation.file_operation.md#submodules)
    * [ark.ark_file_operation.file_operation.ark_file_operation_factory module](ark.ark_file_operation.file_operation.md#module-ark.ark_file_operation.file_operation.ark_file_operation_factory)
      * [`ArkFileOperationFactory`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_factory.ArkFileOperationFactory)
        * [`ArkFileOperationFactory.create_object()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_factory.ArkFileOperationFactory.create_object)
    * [ark.ark_file_operation.file_operation.ark_file_operation_interface module](ark.ark_file_operation.file_operation.md#module-ark.ark_file_operation.file_operation.ark_file_operation_interface)
      * [`FileOperationInterface`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface)
        * [`FileOperationInterface.compare_dir()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.compare_dir)
        * [`FileOperationInterface.compare_file()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.compare_file)
        * [`FileOperationInterface.copy_file()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.copy_file)
        * [`FileOperationInterface.delete_dir()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.delete_dir)
        * [`FileOperationInterface.delete_file()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.delete_file)
        * [`FileOperationInterface.device_clean_partition()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.device_clean_partition)
        * [`FileOperationInterface.device_format()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.device_format)
        * [`FileOperationInterface.device_partition()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.device_partition)
        * [`FileOperationInterface.dir_create()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.dir_create)
        * [`FileOperationInterface.file_close()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.file_close)
        * [`FileOperationInterface.file_open()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.file_open)
        * [`FileOperationInterface.file_read()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.file_read)
        * [`FileOperationInterface.file_rename()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.file_rename)
        * [`FileOperationInterface.file_seek()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.file_seek)
        * [`FileOperationInterface.file_write()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.file_write)
        * [`FileOperationInterface.get_capacity()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.get_capacity)
        * [`FileOperationInterface.get_mount_point()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.get_mount_point)
        * [`FileOperationInterface.mount()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.mount)
        * [`FileOperationInterface.umount()`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface.umount)
      * [`FileSystemType`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType)
        * [`FileSystemType.exfat`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType.exfat)
        * [`FileSystemType.ext2`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType.ext2)
        * [`FileSystemType.ext4`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType.ext4)
        * [`FileSystemType.fat32`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType.fat32)
        * [`FileSystemType.ntfs`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType.ntfs)
        * [`FileSystemType.xfs`](ark.ark_file_operation.file_operation.md#ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType.xfs)
    * [Module contents](ark.ark_file_operation.file_operation.md#module-ark.ark_file_operation.file_operation)


## Module contents
@Module : ark_file_operation
The ‘ark_file_operation’ component is a key channel for the interaction between the operating system and the file system, and between the file system and users. This component mainly provides the simplest interface for the rest of the system, so that users can easily perform various operations on files. At its core are two basic modules: ‘ark_file_operation_factory’ and ‘ark_file_operation_base’.
The ‘ark_file_operation_factory’ module implements the factory pattern. The factory is responsible for dynamically selecting the appropriate mode of operation based on the provided system type and returning the corresponding object.
On the other hand, ‘ark_file_operation_base’ module serves as the base class for implementing file-related operations and functions.This module establishes a standardized framework for the implementation of file operation functions in different systems.
Together, these modules form the backbone of the “ark_file_operation” component, providing users with a powerful and flexible solution for efficient file operation in a wider range of application environments.

🐻@Version: 1.0.9 @update time: 2025/12/26 @Person Responsible: lu.zhang

ꔷ Fallback to del /f /q command if Python’s native file removal fails on windows.

🐻@Version: 1.0.8 @update time: 2025/05/29 @Person Responsible: lu.zhang

ꔷ Added device_clean_partition interface, which can be used to remove the partition table (GPT/MBR) of a storage device under Windows. For detailed usage, refer to the interface documentation. ꔷ Enhanced device_partition and device_clean_partition to support passing logical drive letters (e.g., E:) as the device parameter.

🐻@Version: 1.0.7 @update time: 2025/05/16 @Person Responsible: lu.zhang

ꔷ Fixed the JIRA-795 issue, adaptations have been made for certain cases during partition.

🐻@Version: 1.0.6 @update time: 2025/03/20 @Person Responsible: lu.zhang

ꔷ Reverse the change in v1.0.5 so copy file function can work normally in linux system. ꔷ Optimize the starting address acquisition during partitioning.

🐻@Version: 1.0.5 @update time: 2025/02/26 @Person Responsible: xiaoze

ꔷ Copy the file by changing the common class’s copyFILE interface to not execute any content.

🐻@Version: 1.0.4 @update time: 2025/02/24 @Person Responsible: lu.zhang

ꔷ support more filesystem type in linux format

🐻@Version: 1.0.3 @update time: 2025/02/21 @Person Responsible: lu.zhang

ꔷ change format parameter to enum.

🐻@Version: 1.0.2 @update time: 2025/02/19 @Person Responsible: xiaoze

ꔷ Add a parameter to the copy file interface to set the sampling frequency under the premise of copying and returning performance data.

🐻@Version: 1.0.1 @update time: 2024/4/22 @Person Responsible: lu.zhang

ꔷ xxxxxxxxxxxxxxxx ꔷ xxxxxxxxxxxxx

🐻@Version: 1.0.x @update time: 2024/xx/xx @Person Responsible: lu.zhang

ꔷ xxxxxxxxxxxxxxxx ꔷ xxxxxxxxxxxxx
