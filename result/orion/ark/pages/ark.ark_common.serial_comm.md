---
title: "ark.ark_common.serial_comm package"
docname: "ark.ark_common.serial_comm"
source: "http://orion.longsys.com/ark.ark_common.serial_comm.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_common.serial_comm package
## Submodules
## ark.ark_common.serial_comm.serial_comm module
@Project ：pythonProject_temperature_control @File ：serial_comm.py @IDE ：PyCharm @Author ：厄运马马卡 @Date ：2024/5/6 19:22

_class _ark.ark_common.serial_comm.serial_comm.SerialInterface

Bases: `object`
Enables serial communication with devices

connect(_addr_ , _baudrate =115200_, _bytesize =8_, _parity ='N'_, _stopbits =1_, _timeout =3_, _xonxoff =False_, _rtscts =False_, _write_timeout =None_, _dsrdtr =False_, _inter_byte_timeout =None_, _exclusive =None_)


Breif:

Establishing a communication link with related device(s).

Param:

please reference <https://pyserial.readthedocs.io/en/latest/pyserial_api.html>

Returns:

Success returns 0, failure returns an error code

disconnect()


Breif:

Disconnect the serial port from the device.

module_name _ = 'serial_comm'_


serialread(_rcvmsg_ , _expected_length_ , _timeout =0_)


Breif:

Read data over the serial connection

Parameters:

  * **rcvmsg** – list of received response data
  * **expected_length** – ideally the data length of the received response
  * **timeout**


Returns:

0 means success, error returns the corresponding error code

serialwrite(_sendmsg_ , _size_ , _timeout =0_)


Breif:

Send data over the serial connection

Parameters:

  * **sendmsg** – pending data
  * **size** – length of data to be sent
  * **timeout**


Returns:

0 means success, error returns the corresponding error code
## Module contents
