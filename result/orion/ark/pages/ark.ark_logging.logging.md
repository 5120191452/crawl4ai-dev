---
title: "ark.ark_logging.logging package"
docname: "ark.ark_logging.logging"
source: "http://orion.longsys.com/ark.ark_logging.logging.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_logging.logging package
## Subpackages
  * [ark.ark_logging.logging.ark_logging package](ark.ark_logging.logging.ark_logging.md)
    * [Submodules](ark.ark_logging.logging.ark_logging.md#submodules)
    * [ark.ark_logging.logging.ark_logging.administrator module](ark.ark_logging.logging.ark_logging.md#module-ark.ark_logging.logging.ark_logging.administrator)
      * [`Administrator`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.administrator.Administrator)
        * [`Administrator.delete_logs()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.administrator.Administrator.delete_logs)
        * [`Administrator.update_config()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.administrator.Administrator.update_config)
    * [ark.ark_logging.logging.ark_logging.ark_logging module](ark.ark_logging.logging.ark_logging.md#module-ark.ark_logging.logging.ark_logging.ark_logging)
      * [`ArkLogging`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging)
        * [`ArkLogging.add_extra_file()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.add_extra_file)
        * [`ArkLogging.debug()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.debug)
        * [`ArkLogging.error()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.error)
        * [`ArkLogging.get_component_logger()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.get_component_logger)
        * [`ArkLogging.get_log_path()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.get_log_path)
        * [`ArkLogging.info()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.info)
        * [`ArkLogging.log()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.log)
        * [`ArkLogging.message()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.message)
        * [`ArkLogging.notice()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.notice)
        * [`ArkLogging.pack_logs()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.pack_logs)
        * [`ArkLogging.record_buffer()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.record_buffer)
        * [`ArkLogging.record_comparison_data()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.record_comparison_data)
        * [`ArkLogging.rename_log()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.rename_log)
        * [`ArkLogging.set_component_log_level()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.set_component_log_level)
        * [`ArkLogging.set_log_print_level()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.set_log_print_level)
        * [`ArkLogging.set_logs_dir()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.set_logs_dir)
        * [`ArkLogging.set_non_rotation_log_level()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.set_non_rotation_log_level)
        * [`ArkLogging.set_rotation_log_level()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.set_rotation_log_level)
        * [`ArkLogging.warning()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ArkLogging.warning)
      * [`ComponentLogger`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger)
        * [`ComponentLogger.debug()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.debug)
        * [`ComponentLogger.error()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.error)
        * [`ComponentLogger.info()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.info)
        * [`ComponentLogger.log()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.log)
        * [`ComponentLogger.message()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.message)
        * [`ComponentLogger.notice()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.notice)
        * [`ComponentLogger.warning()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.ComponentLogger.warning)
      * [`RealTimeFileHandler`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.RealTimeFileHandler)
        * [`RealTimeFileHandler.emit()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.RealTimeFileHandler.emit)
      * [`RealTimeRotatingFileHandler`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.RealTimeRotatingFileHandler)
        * [`RealTimeRotatingFileHandler.emit()`](ark.ark_logging.logging.ark_logging.md#ark.ark_logging.logging.ark_logging.ark_logging.RealTimeRotatingFileHandler.emit)
    * [Module contents](ark.ark_logging.logging.ark_logging.md#module-ark.ark_logging.logging.ark_logging)


## Submodules
## ark.ark_logging.logging.ark_logging_interface module

_class _ark.ark_logging.logging.ark_logging_interface.ArkLoggingInterface

Bases: `ABC`
Abstract class that declares an interface for the logging.

_abstract _add_extra_file(_file_ , _remove_after_pack =False_)


Breif:

Adding files to the list that stores additional log files.

Parameters:

  * **file** – Path of the file to be added.
  * **remove_after_pack** – Whether to delete after packaging, default is False, indicating not to delete.


_abstract _debug(_* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with severity ‘DEBUG’.

Parameters:

  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None

_abstract _error(_* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with severity ‘ERROR’.

Parameters:

  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None

_abstract _get_component_logger(_component_name_)


Breif:

Creating a new logger for a component. If in ‘debug’ mode, the log severity level will be set according to the ‘debug_log.yaml’ file for the appropriate component, and the log severity level will be set to ‘ERROR’ for all other components.

Parameters:

**component_name** – component name

Returns:

class object of ‘ComponentLogger’

_abstract _get_log_path()


Brief:

Get the full path of the current non-rotation log file.

Returns:

Full path to the current log file (str), returns empty string if not initialized.

_abstract _info(_* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with severity ‘INFO’.

Parameters:

  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None

_abstract _log(_level_ , _* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with the integer severity ‘level’.

Parameters:

  * **level** – severity level of logging information
  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None

_abstract _message(_* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with severity ‘MESSAGE’.

Parameters:

  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None

_abstract _notice(_* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with severity ‘NOTICE’.

Parameters:

  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None

_abstract _pack_logs(_starttime_ , _endtime_ , _storage_path =None_)


Breif:

Get the error critical information from the log file, write it to the “xx” file, and then compress and save the “xx” file with the log to a certain path.

Parameters:

  * **starttime** – starting time
  * **endtime** – ending time
  * **storage_path** – storage path of the compressed file, the default value is None, which means it is stored in the forward script path


Returns:

storage path of the zip archive, and the error code

_abstract _record_buffer(_src_buffer_ , _src_offset_ , _size_ , _dst_buffer =None_, _dst_offset =0_)


Brief:

Record the source buffer and destination buffer into two txt files respectively, If only the source buffer is passed in, only one copy of the source data will be recorded

Param:

src_buffer (Class byte objects like bytes, bytearray, memoryview): The source buffer containing the data to compare.

Param:

src_offset (int): The starting offset in the source buffer.

Param:

dst_buffer (Class byte objects like bytes, bytearray, memoryview): The destination buffer to compare the data against.

Param:

dst_offset (int): The starting offset in the destination buffer.

Param:

size (int): The number of bytes to compare.
:return:0 indicates successful data recording, failure returns corresponding error code.

_abstract _record_comparison_data(_src_buffer_ , _src_offset_ , _dst_buffer_ , _dst_offset_ , _size_)


Brief:

“record_comparison_data” is deprecated and will be removed in a future version. use “record_buffer” instead
details: please check “record_buffer” annotation

_abstract _rename_log(_new_log_file_name_)


Brief:

Set a custom name for the non-rotating log file.

Parameters:

**new_log_file_name** – the new name for the non-rotating log file

Returns:

0 means the name change is successful, error returns the corresponding error code

_abstract _set_component_log_level(_component_name_ , _log_level_)


Breif:

Setting the level of logging output from related components. This function will fail if you are in ‘debug’ mode

Parameters:

  * **component_name** – component name
  * **log_level** – the log severity level corresponding to this component


Returns:

None

_abstract _set_log_print_level(_level_name_)


Brief:

Setting the level of logging output to the console.

Parameters:

**level_name** – severity level

Returns:

0 indicates that setting the print level is successful, and the corresponding error code is returned for failure.

_abstract _set_logs_dir(_new_path_)


Brief:

Set the log file path, creating the path if it does not exist.

Parameters:

**new_path** – path to the new storage log file(like “C:Program FilesRecuvaLang”, not “C:Program FilesRecuvaLanglog_test.log”)

Returns:

Success returns 0, failure returns the corresponding error code

_abstract _set_non_rotation_log_level(_level_name_)


Brief:

Setting the level of logging output to the non-rotation log file.

Parameters:

**level_name** – severity level

Returns:

0 indicates that setting the non-rotation level is successful, and the corresponding error code is returned for failure.

_abstract _set_rotation_log_level(_level_name_)


Brief:

Setting the level of logging output to the rotation log file.

Parameters:

**level_name** – severity level

Returns:

0 indicates that setting the rotation level is successful, and the corresponding error code is returned for failure.

_abstract _warning(_* args_, _** kwargs_)


Brief:

Log ‘msg % args’ with severity ‘WARNING’.

Parameters:

  * **args** – for receiving any number of positional parameters
  * **kwargs** – for receiving any number of keyword arguments


Returns:

None
## Module contents
