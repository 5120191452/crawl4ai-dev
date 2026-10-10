---
title: "ark.ark_file_operation.file_operation package"
docname: "ark.ark_file_operation.file_operation"
source: "http://orion.longsys.com/ark.ark_file_operation.file_operation.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_file_operation.file_operation package
## Submodules
## ark.ark_file_operation.file_operation.ark_file_operation_factory module

_class _ark.ark_file_operation.file_operation.ark_file_operation_factory.ArkFileOperationFactory(_* args_, _** kwargs_)

Bases: `object`

create_object()


Brief:

Accepts the system_type parameter and creates the corresponding file operation object.

Parameters:

**system_type** – (str)type of the system

Returns:

file operation object
## ark.ark_file_operation.file_operation.ark_file_operation_interface module

_class _ark.ark_file_operation.file_operation.ark_file_operation_interface.FileOperationInterface

Bases: `object`

compare_dir(_src_ , _dst_)


Brief:

compare directory

Parameters:

  * **src** – path to source directory
  * **dst** – path to destination directory


Returns:

error code

compare_file(_src_ , _dst_)


Brief:

compare file

Parameters:

  * **src** – path to source file
  * **dst** – path to destination file


Returns:

error code

copy_file(_src_ , _dst_ , _callback =False_, _sampling_frequency =1_)


Brief:

Copy the file from the source file path to the target file path

Parameters:

  * **src** – Source file path.
  * **dst** – Target file path.
  * **callback** – This parameter is currently only effective under window! The callback defaults to False. If True, it will return a set of dictionaries at the end of the copy, including average performance, maximum performance, minimum performance, copy size, and copy time.
  * **dst** – sampling_frequency


Returns:

Error code and copied array or error code and None

delete_dir(_path_)


Brief:

delete directory recursively

Parameters:

**path** – path to the directory

Returns:

error code

delete_file(_path_)


Brief:

delete file

Parameters:

**path** – path to the file

Returns:

error code

device_clean_partition(_device_)


Brief:

clear the GPT/MBR partition table on a Windows device to allow raw sector access. Not required on Linux.

Parameters:

**device** –
(str) device to be cleaned. example:
> On windows:
>> device = ‘1’, device = ‘2’, device = ‘.PHYSICALDRIVE1’, device = ‘E:’, device = ‘E:' …

Returns:

error code

device_format(_device_ , _filesystem_type_ , _mount_point =''_)


Brief:

format device

Parameters:

  * **device** –
(str) device to be formatted
example:
> On windows:
>> device = ‘D:’, device = ‘F:’ …
> On Linux:
>> device = ‘/dev/sdb1’, device = ‘/dev/sdc2’…
  * **filesystem_type** – (FileSystemType) File system type, defined by the FileSystemType enum.
  * **mount_point** – (str, optional) Mount points after linux formatting, not required for windows


Returns:

error code

device_partition(_device_ , _param_dict_)


Brief:

partition device

Parameters:

**device** –
(str) device to be partitioned example:
> On windows:
>> device = ‘1’, device = ‘2’, device = ‘.PHYSICALDRIVE1’, device = ‘E:’, device = ‘E:' …
> On Linux:
>> device = ‘/dev/sdb’, device = ‘/dev/sdc’…

:param param_dict:(dict)the key value is the corresponding partition capacity in MB;

> if it is 0 (and 0 should be the last one), it is all the unpartitioned capacity of the device.
> In windows and linux, there are up to 4 primary partitions.
example:
> param_dict =
> {
>> partition_capacity0: 1024,
>> partition_capacity1: 2048,
>> partition_capacity2: 0
> }
> In this example, the device is divided into three partitions. The first partition is
> 1024MB, the second partition is 2048MB, and the third partition is the remaining
> capacity.

Returns:

error code

dir_create(_path_ , _exist_ok =True_)


Brief:

create directory recursively

Parameters:

  * **path** – directory full path
  * **exist_ok** – ignore if directory already exists (default: True)


Returns:

error code

file_close()


Brief:

Closes the currently opened file.

Returns:

0 if the file is successfully closed, otherwise returns the corresponding error code.

file_open(_file_ , _mode_)


Brief:

Opens a specified file with the given mode.

Parameters:

  * **file** – The path of the device to be opened.
  * **mode** –
The mode in which to open the device.
example:
> os.O_RDONLY
> os.O_WRONLY | os.O_CREAT | os.O_DIRECT
> …


Returns:

0 if the file is successfully opened, otherwise returns the corresponding error code.

file_read(_buffer_ , _read_size_ , _max_chunk_size =4194304_, _buffer_offset =0_)


Brief:

Read data from a file into a buffer with optional chunking.

Parameters:

  * **buffer** –
The buffer into which the data will be read.
This is where the data read from the file will be stored.
  * **read_size** –
The total number of bytes to read from the file.
Specifies the amount of data to be read into the buffer.
  * **max_chunk_size** –
The maximum size (in bytes) of each chunk to read in one operation.
Defaults to 4 MB (4 * 1024 * 1024 bytes). Useful for reading large files in smaller, manageable chunks.


:param buffer_offset : The read data will be put in buffer start at the buffer_offset position.
> Defaults to 0, meaning it starts from the beginning of the buffer.

Returns:

Operational results(Success returns 0, failure returns an error code) and the total number of bytes successfully read from the file.

file_rename(_src_ , _dst_ , _overwrite =False_)


Brief:

rename (move) file from src to dst

Parameters:

  * **src** – source file full path
  * **dst** – destination file full path
  * **overwrite** – whether overwrite destination if exists (default: False)


Returns:

error code

file_seek(_offset_ , _whence =0_)


Brief:

Move the file pointer to a specific position.

Parameters:

  * **offset** – The position to move the file pointer to.
  * **whence** –
This is optional and defaults to 0. It indicates from which position the offset is applied:
    * os.SEEK_SET: from the start of the file (default).
    * os.SEEK_CUR: from the current file pointer position.
    * os.SEEK_END: from the end of the file.


Returns:

Success returns the new file position, failure returns None.

file_write(_buffer_ , _write_size_ , _max_chunk_size =4194304_, _buffer_offset =0_)


Brief:

Write data from a buffer to a file with optional chunking.

Parameters:

  * **buffer** –
The data to be written to the file.
This is the source of the data that will be written.
  * **write_size** –
The total number of bytes to write from the buffer.
Specifies the amount of data to be written to the file.
  * **max_chunk_size** –
The maximum size (in bytes) of each chunk to write in one operation.
Defaults to 4 MB (4 * 1024 * 1024 bytes). Useful for writing large files in smaller, manageable chunks.


:param buffer_offset : The starting point in the buffer from where to begin writing.
> Defaults to 0, meaning it starts from the beginning of the buffer.

Returns:

Operational results(Success returns 0, failure returns an error code) and the total number of bytes successfully written to the file.

get_capacity(_device_)


Breif:

get total and free capacity of the device in bytes

Parameters:

**device** –
(str) Devices that need access to capacity example:
> On windows:
>> device = “F:”, device = “E:”…
> On Linux, it would be the correspondent mount point of the device:
>> device = “/mnt/sdb1”, device = “/mnt/sdb2”…

Returns:

total_capacity: total capacity of the device in bytes
free_capacity: free capacity of the device in bytes

get_mount_point(_device_)


Brief:

Get the mount point of a specified device on a Linux system.

Parameters:

**(****str****)** (_device_) – The path to the device (e.g., ‘/dev/sdb1’).

Returns:

The mount point of the device if it is mounted, or an empty string if not mounted. or None if occurs ‘CalledProcessError’

mount(_device_ , _mount_point_)


Brief:

Mount a device to a specified mount point on a Linux system.

Parameters:

  * **(****str****)** (_mount_point_) – The path to the device to be mounted (e.g., ‘/dev/sda1’).
  * **(****str****)** – The directory where the device will be mounted (e.g., ‘/mnt/mydrive’).


Returns:

A successful operation returns 0 and the mount path, a failed operation returns an error code and None.

umount(_device_)


Brief:

Unmount a device from its mount point on a Linux system.

Parameters:

**(****str****)** (_device_) – The path to the device to be unmounted (e.g., ‘/dev/sda1’) or the mount point (e.g., ‘/mnt/mydrive’).

Returns:

0 if the unmount operation was successful, an error code otherwise.

_class _ark.ark_file_operation.file_operation.ark_file_operation_interface.FileSystemType(_value_)

Bases: `Enum`
An enumeration.

exfat _ = 'exfat'_


ext2 _ = 'ext2'_


ext4 _ = 'ext4'_


fat32 _ = 'fat32'_


ntfs _ = 'ntfs'_


xfs _ = 'xfs'_

## Module contents
