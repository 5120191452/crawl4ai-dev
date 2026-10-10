---
title: "ark.ark_vu_cmd.vu_cmd package"
docname: "ark.ark_vu_cmd.vu_cmd"
source: "http://orion.longsys.com/ark.ark_vu_cmd.vu_cmd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_vu_cmd.vu_cmd package
## Submodules
## ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_factory module

_class _ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_factory.ArkVuCmdFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_device_type_)


Brief:

Initialising objects

Returns:

Success returns the corresponding object, failure returns None.
## ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface module

_class _ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.TransferCMDType(_value_)

Bases: `Enum`
An enumeration.

read_card_cmd _ = 'read_card_cmd'_


std_protocol_cmd _ = 'std_protocol_cmd'_


_class _ark.ark_vu_cmd.vu_cmd.ark_vu_cmd_interface.VuCmdInterface

Bases: `ABC`

_abstract _erase_blk(_fd_ , _bFlashIndex =0_, _dwRowAddr =0_, _bEraseMode =0_, _wBlkNum =0_, _bSLC =0_, _bChannelNum =0_, _time_out =3_)


@brief: This command is used to erase blocks on the device. This can be used to clear data in specific blocks

or to prepare the blocks for new data to be written.
@param fd: Device handle (int).
@param bFlashIndex: Flash chip index (int). Specifies which flash chip to operate on (default is 0).
@param dwRowAddr: Row address (int). The starting address for the block erase operation (default is 0).
@param bEraseMode: Erase mode (int). Specifies the type of erase operation (default is 0).
@param wBlkNum: Block number (int). The number of blocks to be erased (default is 0).
@param bSLC: SLC mode flag (int). If set to 1, Single-Level Cell mode is used for the erase operation (default is 0).
@param bChannelNum: Channel number (int). Specifies the flash channel to be used for the erase operation (default is 0).
@param time_out: Timeout duration (int). The duration in seconds before This command times out (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _get_dev_smart_info(_fd_ , _time_out =3_)

@brief: This command is used to get dev smart information. This command currently supports SD cards, but TL300 does not support it.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: Success: returns dev smart information (of type bytearray). Failure: returns None.

_abstract _get_dft_info(_fd_ , _bDataFlag_ , _wFunctionIndex_ , _dwParameter_ , _size_ , _time_out =3_)


@brief: This command is used to retrieve the DFT (Device Function Test) information from the device.

This function allows the user to query specific test data related to the device’s functionality.
@param fd: Device handle (int).
@param bDataFlag: Data flag (int).
@param wFunctionIndex: Function index (int). The index of the specific test function whose data is to be retrieved.
@param dwParameter: Parameter (int).
@param size: Size (int). The size of the buffer to store the returned data.
@param time_out: Timeout duration (int). The duration in seconds before This command times out (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _get_firmware_info(_fd_ , _time_out =3_)

@brief: This command is used to get the device firmware information, including the firmware name, firmware version and more information can be found in the document with pageId=127854089.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value：3s).
@return: Success: returns buffer (of type bytearray). Failure: returns None.

_abstract _get_flash_id(_fd_ , _bFlashIndex_ , _bChannelNum_ , _time_out =3_)

@brief: This command is used to get the flash id.
@param fd: Device handle (int).
@param bFlashIndex: (ctypes.c_uint8: 0~255) Flash index specifies the particular flash chip number.
@param bChannelNUm: (ctypes.c_uint8: 0~255) Channel number is used to select a particular channel.
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: Success: returns flash id buffer (of type bytearray). Failure: returns None.

_abstract _get_flash_param(_fd_ , _time_out =3_)

@brief: This command is used to get flash param information, including the number of chip selects, PAGEs, and more information can be found in the document with pageId=127854089.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: Success: returns flash param buffer (of type bytearray). Failure: returns None.

_abstract _get_smart_info(_fd_ , _time_out =3_)

@brief: This command is used to get smart information, including fw version, the count of original bad block and more information can be found in the document with pageId=127854089.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: Success: returns smart information (of type bytearray). Failure: returns None.

_abstract _read_bit_info(_fd_ , _time_out =3_)

@brief: This command is used to read the data of the gtBITInfo structure, including Index BIT block number, Index BIT block chip select and more information can be found in the document with pageId=127854089.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: Success: returns the data of the gtBITInfo structure (of type bytearray). Failure: returns None.

_abstract _read_common_info(_fd_ , _time_out =3_)

@brief: This command is used to get the common information, including BIT Block number, SLC free block count and more information can be found in the document with pageId=127854089.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: Success: returns common info buffer (of type bytearray). Failure: returns None.

_abstract _read_flash_page(_fd_ , _bFlashIndex =0_, _dwRowAddr =0_, _dwSeed =0_, _bPackage =0_, _bRandmize =0_, _bOpenEcc =0_, _bRedunLen =0_, _bPlaneCmd =0_, _bDataType =0_, _bRetry =0_, _bCacheCmd =0_, _bChannelNum =0_, _bSLC =0_, _bInterLevOp =0_, _bRetryEccNum =0_, _bPlaneIndex =0_, _wBlkNum =0_, _wPageStart =0_, _time_out =3_)


@brief: This command is used to read a flash page from the device. It supports various configuration options

for flash read behavior, such as data randomization, ECC enabling, redundancy length, and plane selection. The function retrieves the data from the specified flash chip and returns it in the form of a bytearray.
@param fd: Device handle (int).
@param bFlashIndex: Flash chip index (int). Specifies the flash chip to read from (default is 0).
@param dwRowAddr: Row address (int). The starting address for the read operation (default is 0).
@param dwSeed: Seed for randomization (int). A seed value for randomizing data read from the flash (default is 0).
@param bPackage: (default is 0).
@param bRandmize: Randomization flag (int). If set to 1, randomizes the data during the read operation (default is 0).
@param bOpenEcc: ECC enabling flag (int). If set to 1, enables ECC during the read operation to correct potential errors (default is 0).
@param bRedunLen: Redundancy length (int). Defines the redundancy type and length for the data (default is 0).
@param bPlaneCmd: Plane command flag (int). If set to 1, enables multi-plane command for the read operation (default is 0).
@param bDataType: Data type (int). Specifies the type of data to be read (default is 0).
@param bRetry: Retry flag (int). If set to 1, enables retry in case of failure (default is 0).
@param bCacheCmd: Cache command flag (int). If set to 1, enables the flash cache command during the read operation (default is 0).
@param bChannelNum: Channel number (int). Specifies the flash channel to be used for the read operation (default is 0).
@param bSLC: SLC mode flag (int). If set to 1, Single-Level Cell (SLC) mode is used for the read operation (default is 0).
@param bInterLevOp: Interleave operation flag (int). If set to 1, interleaved operations will be used during the read (default is 0).
@param bRetryEccNum: Retry ECC count (int). Specifies the number of retries for ECC failure (default is 0).
@param bPlaneIndex: Plane index (int). Specifies the plane for the read operation (default is 0).
@param wBlkNum: Block number (int). The block number for the read operation (default is 0).
@param wPageStart: Page start address (int). The starting page address for the read operation (default is 0).
@param time_out: Timeout value (int). The timeout duration in seconds. If the operation exceeds this duration, it will be aborted (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _read_iir(_fd_ , _time_out =3_)


@brief: This command is used to read the IIR (Interrupt Information Register) from the device.

This register typically contains information about interrupt status or errors.
@param fd: Device handle (int).
@param time_out: Timeout duration (int). The duration in seconds before This command times out (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _read_ram(_fd_ , _dwAddr_ , _dwLen_ , _time_out =3_)


@brief: This command is used to read data from a specific location in the RAM of the device.

The data is read from the given address with a specified length.
@param fd: Device handle (int).
@param dwAddr: Address (int). The starting address in RAM from which data will be read.
@param dwLen: Length (int). The number of bytes to be read from the RAM.
@param time_out: Timeout duration (int). The duration in seconds before This command times out (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _rebuild_bit(_fd_ , _time_out =3_)

@brief: This command is used to clear IDA and rebuild BIT processing.
@param fd: Device handle (int).
@param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: TRUE is Pass, other is Failed.

_abstract _set_bad_blk(_fd_ , _lbk_idx_ , _wCrc =0_, _time_out =3_)

@brief: This command is used to mark a specific block as bad in the device.
@param fd: Device handle (int).
@param lbk_idx: Block index (int). The index of the block to be marked as bad.
@param wCrc: CRC error code (int). The error code related to CRC failure (default is 0).
@param time_out: Timeout duration (int). The duration in seconds before This command times out (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _user_cmd_authorize(_fd_ , _buf_ , _time_out =3_)

@brief: This command is used to authorize user commands. Some private commands need authorization to be executed properly.
@param fd: Device handle (int).
@param buf: The ‘buf’ is the buffer obtained by get_firmware_info command, and it’s type is bytearray. @param time_out: Time_out(int). The code execution time, exceeding time_out will abort execution (default value: 3s).
@return: TRUE is Pass, other is Failed.

_abstract _write_flash_page(_fd_ , _buf_ , _bFlashIndex =0_, _dwRowAddr =0_, _bPackages =0_, _dwSeed =0_, _bRandmize =0_, _bOpenEcc =0_, _bRedunLen =0_, _bPlaneCmd =0_, _bDataType =0_, _bRetry =0_, _bCacheCmd =0_, _bChannelNum =0_, _bSLC =0_, _bInterLevOp =0_, _bPlaneIndex =0_, _wBlkNum =0_, _wPageStart =0_, _time_out =3_)


@brief: This command is used to write a flash page of the device. It allows for a range of configuration options such as

the flash chip selection, ECC enabling, redundancy handling, and interleaved operations.
@param fd: Device handle (int).
@param buf: Data buffer (bytearray). The data to be written to the flash page.
@param bFlashIndex: Flash chip index (int). The chip selection for the write operation (default is 0).
@param dwRowAddr: Row address (int). The starting address for the page write operation (default is 0).
@param bPackages: (default is 0).
@param dwSeed: Seed for randomization (int). A seed value used for data randomization (default is 0).
@param bRandmize: Randomization flag (int). If set to 1, the data will be randomized using the seed value (default is 0).
@param bOpenEcc: ECC enabling flag (int). If set to 1, enables error correction code (ECC) for the write operation (default is 0).
@param bRedunLen: Redundancy length (int). Defines the redundancy type and length for the data (default is 0).
@param bPlaneCmd: Plane command type (int). If set to 1, multi-plane commands will be used for the flash (default is 0).
@param bDataType: Data type (int). Specifies the type of data for the write operation (default is 0).
@param bRetry: Retry flag (int). If set to 1, the write will be retried in case of failure (default is 0).
@param bCacheCmd: Cache command flag (int). If set to 1, enables cache commands for the flash write operation (default is 0).
@param bChannelNum: Channel number (int). Specifies the flash channel for the write operation (default is 0).
@param bSLC: SLC mode flag (int). If set to 1, Single-Level Cell (SLC) mode is used for the flash write, otherwise Triple-Level Cell (TLC) (default is 0).
@param bInterLevOp: Interleave operation flag (int). If set to 1, interleaved operations will be performed (default is 0).
@param bPlaneIndex: Plane index (int). The specific plane index for the flash page write (default is 0).
@param wBlkNum: Block number (int). The block number for the write operation (default is 0).
@param wPageStart: Page start address (int). The starting page address for the write operation (default is 0).
@param time_out: Timeout value (int). The timeout duration in seconds. If This command takes longer than this time, it will be aborted (default is 3s).
@return: TRUE is Pass, other is Failed.

_abstract _write_ram(_fd_ , _buf_ , _dwAddr_ , _dwLen_ , _time_out =3_)


@brief: This command is used to write data to a specific location in the RAM of the device.

The data is written starting from the given address with a specified length.
@param fd: Device handle (int).
@param buf: Data to be written (bytearray). The data that will be written to the RAM.
@param dwAddr: Address (int). The starting address in RAM where data will be written.
@param dwLen: Length (int). The length of the data to be written in bytes.
@param time_out: Timeout duration (int). The duration in seconds before This command times out (default is 3s).
@return: TRUE is Pass, other is Failed.
## Module contents
