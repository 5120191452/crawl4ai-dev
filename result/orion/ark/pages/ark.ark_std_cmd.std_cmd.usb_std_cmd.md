---
title: "ark.ark_std_cmd.std_cmd.usb_std_cmd package"
docname: "ark.ark_std_cmd.std_cmd.usb_std_cmd"
source: "http://orion.longsys.com/ark.ark_std_cmd.std_cmd.usb_std_cmd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_std_cmd.std_cmd.usb_std_cmd package
## Submodules
## ark.ark_std_cmd.std_cmd.usb_std_cmd.usb_std_cmd module

_class _ark.ark_std_cmd.std_cmd.usb_std_cmd.usb_std_cmd.USBSTDCMD(_* args_, _** kwargs_)

Bases: `object`

access_control_in(_handle_ , _Reserved1 =0_, _SERVICE_ACTION =0_, _MANAGEMENT_IDENTIFIER_KEY =0_, _ALLOCATION_LENGTH =0_, _Reserved2 =0_, _CONTROL =0_, _func_time_out =1000000_)


access_control_out(_handle_ , _buffer_ , _Reserved1 =0_, _SERVICE_ACTION =0_, _Reserved2 =0_, _PARAMETER_LIST_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


async_send_cmd(_handle =None_, _cmd =None_, _cmd_len =None_, _buf =None_, _buf_size =0_, _direction =None_, _time_out =None_)


async_send_scsi(_handle =None_, _cdb =None_, _cdb_len =None_, _buf =None_, _buf_size =0_, _streams_id =1_, _direction =None_, _time_out =None_)


ata_pass_through12(_handle_ , _buffer =None_, _MULTIPLE_COUNT =0_, _PROTOCOL =0_, _Reserved1 =0_, _OFF_LINE =0_, _CK_COND =0_, _T_TYPE =0_, _T_DIR =0_, _BYTE_BLOCK =0_, _T_LENGTH =0_, _FEATURES_7_0 =0_, _SECTOR_COUNT_7_0 =0_, _LBA_LOW_7_0 =0_, _LBA_MID_7_0 =0_, _LBA_HIGH_7_0 =0_, _DEVICE =0_, _COMMAND =0_, _Reserved2 =0_, _CONTROL =0_, _func_time_out =1000000_)


ata_pass_through16(_handle_ , _buffer =None_, _MULTIPLE_COUNT =0_, _PROTOCOL =0_, _EXTEND =0_, _OFF_LINE =0_, _CK_COND =0_, _T_TYPE =0_, _T_DIR =0_, _BYTE_BLOCK =0_, _T_LENGTH =0_, _FEATURES_15_8 =0_, _FEATURES_7_0 =0_, _SECTOR_COUNT_15_8 =0_, _SECTOR_COUNT_7_0 =0_, _LBA_LOW_15_8 =0_, _LBA_LOW_7_0 =0_, _LBA_MID_15_8 =0_, _LBA_MID_7_0 =0_, _LBA_HIGH_15_8 =0_, _LBA_HIGH_7_0 =0_, _DEVICE =0_, _COMMAND =0_, _CONTROL =0_, _func_time_out =1000000_)


build_bot_cmd(_cdb =None_, _cdb_len =None_, _dCBWSignature =1431519811_, _dCBWTag =3504792642_, _dCBWDataTransferLength =0_, _bmCBWFlags =0_, _bCBWLUN =0_, _Reserved0 =0_, _bCBWCBLength =16_, _Reserved1 =0_)


build_uasp_cmd(_cdb =None_, _cdb_len =None_, _IU_ID =1_, _Reserved_1 =0_, _TAG =1_, _Reserved_2 =0_, _COMMAND_PRIORITY =0_, _TASK_ATTRIBUTE =0_, _Reserved_3 =0_, _ADDITIONAL_CDB_LENGTH =0_, _Reserved_4 =0_, _Reserved_5 =0_, _LOGICAL_UNIT_NUMBER =0_)


bulkOnly_read(_handle =None_, _length =0_, _time_out =0_)


bulkOnly_write(_handle =None_, _buffer =None_, _length =0_, _time_out =0_)


check_sense(_sense_ , _expect_value_)


clear_feature(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


extended_copy(_handle_ , _buffer_ , _Reserved1 =0_, _PARAMETER_LIST_LENGTH =24_, _Reserved2 =0_, _CONTROL =0_, _func_time_out =1000000_)


format_unit(_handle_ , _FMTPINFO =0_, _LONGLIST =0_, _FMTDATA =0_, _CMPLST =0_, _DEFECT_LIST_FORMAT =0_, _VendorSpecific =0_, _Obsolete =0_, _CONTROL =0_, _PARAMETER_LIST_LENGTH =0_, _PARAMETER_LIST =None_, _func_time_out =1000000_)


format_unit_ufi(_handle_ , _LOGICAL_UNIT_NUMBER =0_, _FMTDATA =0_, _CMPLST =0_, _DEFECT_LIST_FORMAT =0_, _TrackNumber =0_, _Interleave =0_, _Reserved1 =0_, _PARAMETER_LIST_LENGTH =0_, _Reserved2 =0_, _PARAMETER_LIST =None_, _func_time_out =1000000_)


get_async_cmd_result(_handle_ , _streams_id_ , _buf_size =0_, _time_out =256_)


get_cmd_exec_info()


get_configuration(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =1_, _timeout_us =500000_)


get_descriptor(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


get_device_configuration(_handle_)


get_endpoint_address(_handle_ , _request_uas_endpoints =False_)


get_interface(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =1_, _timeout_us =500000_)


get_status(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =2_, _timeout_us =500000_)


inquiry(_handle_ , _Reserved =0_, _Obsolete =0_, _EVPD =0_, _PAGE_CODE =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


log_select(_handle_ , _Reserved1 =0_, _PCR =0_, _SP =0_, _PC =0_, _PAGE_CODE =0_, _SUB_PAGE_CODE =0_, _Reserved2 =0_, _PARAMETER_LIST_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


log_sense(_handle_ , _Reserved1 =0_, _Obsolete =0_, _SP =0_, _PC =0_, _PAGE_CODE =0_, _SUB_PAGE_CODE =0_, _Reserved2 =0_, _PARAMETER_POINTER =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


management_protocol_in(_handle_ , _Reserved1 =0_, _SERVICE_ACTION =16_, _MANAGEMENT_PROTOCOL =0_, _MANAGEMENT_PROTOCOL_SPECIFIC1 =0_, _ALLOCATION_LENGTH =0_, _MANAGEMENT_PROTOCOL_SPECIFIC2 =0_, _CONTROL =0_, _func_time_out =1000000_)


management_protocol_out(_handle_ , _buffer_ , _Reserved1 =0_, _SERVICE_ACTION =16_, _MANAGEMENT_PROTOCOL =0_, _MANAGEMENT_PROTOCOL_SPECIFIC1 =0_, _PARAMETER_LIST_LENGTH =0_, _MANAGEMENT_PROTOCOL_SPECIFIC2 =0_, _CONTROL =0_, _func_time_out =1000000_)


mode_select10(_handle_ , _Reserved1 =0_, _PF =0_, _Reserved2 =0_, _SP =0_, _Reserved3 =0_, _PARAMETER_LIST_LENGTH =0_, _PARAMETER_BUFFER =None_, _CONTROL =0_, _func_time_out =1000000_)


mode_select6(_handle_ , _buffer_ , _Reserved1 =0_, _PF =0_, _Reserved2 =0_, _SP =0_, _Reserved3 =0_, _PARAMETER_LIST_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


mode_sense10(_handle_ , _LLBAA =0_, _DBD =0_, _PC =0_, _PAGE_CODE =0_, _SUBPAGE_CODE =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


mode_sense6(_handle_ , _Reserved1 =0_, _DBD =0_, _Reserved2 =0_, _PC =0_, _PAGE_CODE =0_, _SUBPAGE_CODE =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


orwrite16(_handle_ , _buffer_ , _ORPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Reserved2 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


persistent_reserve_in(_handle_ , _Reserved1 =0_, _SERVICE_ACTION =0_, _Reserved2 =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


persistent_reserve_out(_handle_ , _buffer_ , _Reserved1 =0_, _SERVICE_ACTION =0_, _SCOPE =0_, _TYPE =0_, _Reserved2 =0_, _PARAMETER_LIST_LENGTH =24_, _CONTROL =0_, _func_time_out =1000000_)


prefetch10(_handle_ , _Reserved1 =0_, _IMMED =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _PREFETCH_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


prefetch16(_handle_ , _Reserved1 =0_, _IMMED =0_, _Reserved2 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _PREFETCH_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


prevent_allow_medium_removal(_handle_ , _Reserved1 =0_, _Reserved2 =0_, _Reserved3 =0_, _Reserved4 =0_, _PREVENT =0_, _CONTROL =0_, _func_time_out =1000000_)


read10(_handle_ , _RDPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


read12(_handle_ , _RDPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Reserved2 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Restricted_for_MMC_6 =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


read16(_handle_ , _RDPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Reserved2 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


read32(_handle_ , _CONTROL =0_, _Reserved1 =0_, _Reserved2 =0_, _GroupNumber =0_, _AdditionalCDBLength =24_, _ServiceAction =9_, _RDPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved4 =0_, _FUA_NV =0_, _Reserved5 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _ExpectedInitialLogicalBlockReferenceTag =0_, _ExpectedLogicalBlockApplicationTag =0_, _LogicalBlockApplicationTagMask =0_, _TRANSFER_LENGTH =0_, _func_time_out =1000000_)


read6(_handle_ , _Reserved =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


read_attribute(_handle_ , _Reserved1 =0_, _SERVICE_ACTION =0_, _Restricted =0_, _VOLUME_NUMBER =0_, _Reserved2 =0_, _PARTITION_NUMBER =0_, _FIRST_ATTRIBUTE_IDENTIFIER =0_, _ALLOCATION_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


read_buffer(_handle_ , _Reserved1 =0_, _MODE =0_, _BUFFER_ID =0_, _BUFFER_OFFSET =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


read_capacity10(_handle_ , _Reserved1 =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _Reserved3 =0_, _PMI =0_, _CONTROL =0_, _func_time_out =1000000_)


read_capacity16(_handle_ , _Reserved1 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _ALLOCATION_LENGTH =0_, _Reserved2 =0_, _PMI =0_, _CONTROL =0_, _func_time_out =1000000_)


read_defect_data10(_handle_ , _Reserved1 =0_, _Reserved2 =0_, _REQ_PLIST =0_, _REQ_GLIST =0_, _DEFECT_LIST_FORMAT =0_, _Reserved3 =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


read_defect_data12(_handle_ , _Reserved1 =0_, _REQ_PLIST =0_, _REQ_GLIST =0_, _DEFECT_LIST_FORMAT =0_, _Reserved2 =0_, _ALLOCATION_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


read_format_capacity(_handle_ , _LOGICAL_UNIT_NUMBER =0_, _Allocation_Length =0_, _func_time_out =1000000_)


read_long10(_handle_ , _Reserved1 =0_, _PBLOCK =0_, _CORRCT =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _BYTE_TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


reassign_blocks(_handle_ , _Reserved1 =0_, _LONGLBA =0_, _LONGLIST =0_, _Reserved2 =0_, _CONTROL =0_, _func_time_out =1000000_)


receive_copy_results(_handle_ , _Reserved1 =0_, _SERVICE_ACTION =0_, _LIST_IDENTIFIER =0_, _Reserved2 =0_, _ALLOCATION_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


receive_diagnostic_results(_handle_ , _Reserved1 =0_, _PCV =0_, _PAGE_CODE =0_, _ALLOCATION_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


report_luns(_handle_ , _Reserved1 =0_, _SELECTREPORT =0_, _Reserved2 =0_, _ALLOCATION_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


request_read(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =1000000_)


request_sense(_handle_ , _DESC =0_, _ALLOCATION_LENGTH =18_, _CONTROL =0_, _Reserved1 =0_, _Reserved2 =0_, _func_time_out =1000000_)


request_write(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =1000000_)


reset_device(_handle_)


security_protocol_in(_handle_ , _SECURITY_PROTOCOL =0_, _SECURITY_PROTOCOL_SPECIFIC =0_, _INC_512 =0_, _Reserved1 =0_, _Reserved2 =0_, _ALLOCATION_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


security_protocol_out(_handle_ , _buffer_ , _SECURITY_PROTOCOL =0_, _SECURITY_PROTOCOL_SPECIFIC =0_, _INC_512 =0_, _Reserved1 =0_, _Reserved2 =0_, _TRANSFER_LENGTH =0_, _Reserved3 =0_, _CONTROL =0_, _func_time_out =1000000_)


send_cmd(_handle =None_, _cmd =None_, _cmd_len =None_, _buf =None_, _buf_size =0_, _direction =None_, _time_out =None_)


send_cmd_execute_without_data(_handle =None_, _cmd =None_, _cmd_len =None_, _time_out =None_)


send_cmd_read(_handle =None_, _cmd =None_, _cmd_len =None_, _buf =None_, _buf_size =0_, _time_out =None_)


send_cmd_write(_handle =None_, _cmd =None_, _cmd_len =None_, _buf =None_, _buf_size =0_, _time_out =None_)


send_diagnostic(_handle_ , _SELFTEST_CODE =0_, _PF =0_, _Reserved =0_, _SELFTEST =0_, _DevOFFL =0_, _UnitOFFL =0_, _Reserved2 =0_, _ParameterListLength =0_, _CONTROL =0_, _func_time_out =1000000_)


send_scsi(_handle_ , _cdb_ , _direction =Direction.read_, _data_length =0_, _data_buf =None_, _func_time_out =1000000_)


send_scsi_execute_without_data(_handle_ , _cdb_ , _func_time_out =1000000_)


send_scsi_read(_handle_ , _cdb_ , _data_length =0_, _func_time_out =1000000_)


send_scsi_write(_handle_ , _cdb_ , _data_buf =None_, _data_length =0_, _func_time_out =1000000_)


set_address(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_configuration(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_descriptor(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_feature(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_interface(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_isochronous_delay(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_sel(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


set_stl(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


start_stop_unit(_handle_ , _Reserved1 =0_, _IMMED =0_, _Reserved2 =0_, _Reserved3 =0_, _POWER_CONDITION_MODIFIER =0_, _POWER_CONDITION =0_, _Reserved4 =0_, _NO_FLUSH =0_, _LOEJ =0_, _START =0_, _CONTROL =0_, _func_time_out =1000000_)


synch_frame(_handle_ , _bmRequestType_ , _bRequest_ , _wValue_ , _wIndex_ , _data =None_, _wLength =0_, _timeout_us =500000_)


synchronize_cache10(_handle_ , _Reserved1 =0_, _SYNC_NV =0_, _IMMED =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _NUMBER_OF_LOGICAL_BLOCKS =0_, _CONTROL =0_, _func_time_out =1000000_)


synchronize_cache16(_handle_ , _SYNC_NV =0_, _IMMED =0_, _Reserved1 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _NUMBER_OF_LOGICAL_BLOCKS =0_, _Reserved2 =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


test_unit_ready(_handle_ , _Reserved =0_, _CONTROL =0_)


unmap(_handle_ , _buffer_ , _Reserved1 =0_, _ANCHOR =0_, _Reserved2 =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _PARAMETER_LIST_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


verify10(_handle_ , _VRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _VERIFICATION_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


verify12(_handle_ , _VRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _VERIFICATION_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


verify16(_handle_ , _VRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _VERIFICATION_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


write10(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


write12(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Reserved2 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


write16(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved1 =0_, _FUA_NV =0_, _Reserved2 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


write32(_handle_ , _buffer_ , _CONTROL =0_, _Reserved1 =0_, _Reserved2 =0_, _GroupNumber =0_, _AdditionalCDBLength =24_, _ServiceAction =11_, _WRPROTECT =0_, _DPO =0_, _FUA =0_, _Reserved3 =0_, _FUA_NV =0_, _Reserved4 =0_, _Reserved5 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _ExpectedInitialLogicalBlockReferenceTag =0_, _ExpectedLogicalBlockApplicationTag =0_, _LogicalBlockApplicationTagMask =0_, _TRANSFER_LENGTH =0_, _func_time_out =1000000_)


write6(_handle_ , _buffer_ , _Reserved =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


write_and_verify(_handle_ , _WRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


write_and_verify10(_handle_ , _WRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


write_and_verify12(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


write_and_verify16(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _Reserved1 =0_, _BYTCHK =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _TRANSFER_LENGTH =0_, _Restricted_for_MMC_6 =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _CONTROL =0_, _func_time_out =1000000_)


write_attribute(_handle_ , _buffer_ , _Reserved1 =0_, _Restricted =0_, _VOLUME_NUMBER =0_, _Reserved2 =0_, _PARTITION_NUMBER =0_, _Reserved3 =0_, _PARAMETER_LIST_LENGTH =0_, _Reserved4 =0_, _CONTROL =0_, _func_time_out =1000000_)


write_buffer(_handle_ , _MODE_SPECIFIC =0_, _MODE =0_, _BUFFER_ID =0_, _BUFFER_OFFSET =0_, _PARAMETER_LIST_LENGTH =0_, _CONTROL =0_, _PARAMETER_BUFFER =None_, _func_time_out =1000000_)


write_long10(_handle_ , _buffer_ , _COR_DIS =0_, _WR_UNCOR =0_, _PBLOCK =0_, _Reserved1 =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _BYTE_TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


write_same10(_handle_ , _buffer_ , _WRPROTECT =0_, _ANCHOR =0_, _UNMAP =0_, _PBDATA =0_, _LBDATA =0_, _Obsolete =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved1 =0_, _GROUP_NUMBER =0_, _NUMBER_OF_LOGICAL_BLOCKS =0_, _CONTROL =0_, _func_time_out =1000000_)


write_same16(_handle_ , _buffer_ , _WRPROTECT =0_, _ANCHOR =0_, _UNMAP =0_, _PBDATA =0_, _LBDATA =0_, _Reserved1 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _NUMBER_OF_LOGICAL_BLOCKS =0_, _Reserved2 =0_, _GroupNumber =0_, _CONTROL =0_, _func_time_out =1000000_)


xdread10(_handle_ , _Reserved1 =0_, _XORPINFO =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


xdwrite10(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _FUA =0_, _DISABLE_WRITE =0_, _FUA_NV =0_, _Reserved1 =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


xdwriteread10(_handle_ , _buffer_ , _WRPROTECT =0_, _DPO =0_, _FUA =0_, _DISABLE_WRITE =0_, _FUA_NV =0_, _XORPINFO =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved2 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)


xpwrite10(_handle_ , _buffer_ , _Reserved1 =0_, _DPO =0_, _FUA =0_, _Reserved2 =0_, _FUA_NV =0_, _XORPINFO =0_, _LOGICAL_BLOCK_ADDRESS =0_, _Reserved3 =0_, _GROUP_NUMBER =0_, _TRANSFER_LENGTH =0_, _CONTROL =0_, _func_time_out =1000000_)

## Module contents
