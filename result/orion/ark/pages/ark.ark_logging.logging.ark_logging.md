---
title: "ark.ark_logging.logging.ark_logging package"
docname: "ark.ark_logging.logging.ark_logging"
source: "http://orion.longsys.com/ark.ark_logging.logging.ark_logging.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_logging.logging.ark_logging package
## Submodules
## ark.ark_logging.logging.ark_logging.administrator module

_class _ark.ark_logging.logging.ark_logging.administrator.Administrator

Bases: `object`
Have super administrator privileges

delete_logs(_log_path_ , _days_to_keep_)


Brief:

Keep the last m days of logs, delete others.

Parameters:

  * **log_path** – Path to the storage log file.
  * **days_to_keep** – Keeps the logs with the most recent days_to_keep (in days), deletes the other logs, and deletes all logs in the disk when the days_to_keep value is 0.


Returns:

0 means the operation is successful, failure to return the corresponding error code.

update_config(_modifications_ , _path =None_)


Brief:

Modify the configuration file based on the provided modifications.

Parameters:

  * **modifications** –
modifications (dict): Dictionary containing the field-value pairs to be modified.
example:
> modifications =
>> {
>>> ‘Maximum_Bytes_of_Rotation_log’: 498,
>>> ’BackupLogCount’: 5,
>>> ’DiskSpaceThreshold’: 20,
>>> ’OutputConsole’: 1,
>>> ’DaytoKeep’: 90
>>> ’ImmediateFlushHandler’: True
>> }
  * **path** – (str, optional) path to the directory containing rotation log files


Returns:

None
## ark.ark_logging.logging.ark_logging.ark_logging module

_class _ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging(_* args_, _** kwargs_)

Bases: `Logger`
Custom logger class with handler, filters, formatters.

add_extra_file(_file_ , _remove_after_pack =False_)


debug(_* args_, _** kwargs_)

Log ‘msg % args’ with severity ‘DEBUG’.
To pass exception information, use the keyword argument exc_info with a true value, e.g.
logger.debug(“Houston, we have a %s”, “thorny problem”, exc_info=1)

error(_* args_, _** kwargs_)

Log ‘msg % args’ with severity ‘ERROR’.
To pass exception information, use the keyword argument exc_info with a true value, e.g.
logger.error(“Houston, we have a %s”, “major problem”, exc_info=1)

get_component_logger(_component_name_)


get_log_path()


info(_* args_, _** kwargs_)

Log ‘msg % args’ with severity ‘INFO’.
To pass exception information, use the keyword argument exc_info with a true value, e.g.
logger.info(“Houston, we have a %s”, “interesting problem”, exc_info=1)

log(_level_ , _* args_, _** kwargs_)

Log ‘msg % args’ with the integer severity ‘level’.
To pass exception information, use the keyword argument exc_info with a true value, e.g.
logger.log(level, “We have a %s”, “mysterious problem”, exc_info=1)

message(_* args_, _** kwargs_)


notice(_* args_, _** kwargs_)


pack_logs(_starttime_ , _endtime_ , _storage_path =None_)

打包日志文件（跨进程安全版本，使用文件锁避免 PermissionError）

record_buffer(_src_buffer_ , _src_offset_ , _size_ , _dst_buffer =None_, _dst_offset =0_)

记录数据： - 如果传入 src_buffer 和 dst_buffer：记录两份数据（源+目标） - 如果只传入 src_buffer：只记录一份数据

record_comparison_data(_src_buffer_ , _src_offset_ , _dst_buffer_ , _dst_offset_ , _size_)


rename_log(_new_log_file_name_)


set_component_log_level(_component_name_ , _log_level_)


set_log_print_level(_level_name_)


set_logs_dir(_new_path_)


set_non_rotation_log_level(_level_name_)


set_rotation_log_level(_level_name_)


warning(_* args_, _** kwargs_)

Log ‘msg % args’ with severity ‘WARNING’.
To pass exception information, use the keyword argument exc_info with a true value, e.g.
logger.warning(“Houston, we have a %s”, “bit of a problem”, exc_info=1)

_class _ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger(_name_)

Bases: `object`
Component-specific logging classes

debug(_* args_, _** kwargs_)


error(_* args_, _** kwargs_)


info(_* args_, _** kwargs_)


log(_level_ , _* args_, _** kwargs_)


message(_* args_, _** kwargs_)


notice(_* args_, _** kwargs_)


warning(_* args_, _** kwargs_)


_class _ark.ark_logging.logging.ark_logging.ark_logging.RealTimeFileHandler(_filename_ , _mode ='a'_, _encoding =None_, _delay =False_, _errors =None_)

Bases: `FileHandler`

emit(_record_)

Emit a record.
If the stream was not opened because ‘delay’ was specified in the constructor, open it before calling the superclass’s emit.

_class _ark.ark_logging.logging.ark_logging.ark_logging.RealTimeRotatingFileHandler(_filename_ , _mode ='a'_, _maxBytes =0_, _backupCount =0_, _encoding =None_, _delay =False_, _lock_file : str | None = None_)

Bases: `RotatingFileHandler`
多进程共享同一日志文件并支持轮换的 Handler。 原理：使用独立的 lock 文件（filename + ‘.lock’）作为全局互斥锁。 所有进程在写入时先 lock(lockfile)，写入并 flush、关闭文件后检查是否需要轮换， 若需要则在同一把锁下调用父类的 doRollover() 完成轮换。

emit(_record_)

写日志记录（带跨进程锁保护）
## Module contents
