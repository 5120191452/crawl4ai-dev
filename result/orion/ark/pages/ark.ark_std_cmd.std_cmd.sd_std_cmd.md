---
title: "ark.ark_std_cmd.std_cmd.sd_std_cmd package"
docname: "ark.ark_std_cmd.std_cmd.sd_std_cmd"
source: "http://orion.longsys.com/ark.ark_std_cmd.std_cmd.sd_std_cmd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_std_cmd.std_cmd.sd_std_cmd package
## Submodules
## ark.ark_std_cmd.std_cmd.sd_std_cmd.sd_std_cmd module

_class _ark.ark_std_cmd.std_cmd.sd_std_cmd.sd_std_cmd.CMDINFO(_exec_time : float_)

Bases: `object`

exec_time _: float_


_class _ark.ark_std_cmd.std_cmd.sd_std_cmd.sd_std_cmd.SDSTDCMD(_* args_, _** kwargs_)

Bases: `object`

acmd01()


acmd02()


acmd03()


acmd04()


acmd05()


acmd06(_handle_ , _stuff_bits =0_, _bus_width =0_, _timeout_us =1000000_)


acmd07()


acmd08()


acmd09()


acmd10()


acmd11()


acmd12()


acmd13(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


acmd14()


acmd15()


acmd16()


acmd17()


acmd18()


acmd19()


acmd20()


acmd21()


acmd22(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


acmd23(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


acmd24()


acmd25()


acmd26()


acmd27()


acmd28()


acmd29()


acmd30()


acmd31()


acmd32()


acmd33()


acmd34()


acmd35()


acmd36()


acmd37()


acmd38()


acmd39()


acmd40()


acmd41(_handle_ , _reserved_ , _HCS_ , _reserved_for_eSD_ , _xpc_ , _reserved_bits_ , _s18r_ , _voltage_windows_ , _timeout_us =1000000_)


acmd42(_handle_ , _stuff_bits =0_, _set_cd =0_, _timeout_us =1000000_)


acmd43()


acmd44()


acmd45()


acmd46()


acmd47()


acmd48()


acmd49()


acmd50()


acmd51(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


acmd52()


acmd53()


acmd54()


acmd55()


acmd56()


acmd57()


acmd58()


acmd59()


cmd00(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd01()


cmd02(_handle_ , _stuff_bits_ , _timeout_us =1000000_)


cmd03(_handle_ , _stuff_bits_ , _timeout_us =1000000_)


cmd04(_handle_ , _dsr_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd05()


cmd06(_handle_ , _mode_ , _group_ , _value_ , _timeout_us =1000000_)


cmd07(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd08(_handle_ , _reserved_ , _supply_voltage_ , _check_pattern_ , _timeout_us =1000000_)


cmd09(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd10(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd11(_handle_ , _reserved_ , _timeout_us =1000000_)


cmd12(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd13(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd14()


cmd15(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd16(_handle_ , _block_length_ , _timeout_us =1000000_)


cmd17(_handle_ , _bus_width_ , _data_address_ , _timeout_us =1000000_)


cmd18(_handle_ , _data_address_ , _data_length_ , _blk_len =512_, _is_high_capacity =True_, _timeout_us =1000000_)


cmd19(_handle_ , _reserved_ , _timeout_us =1000000_)


cmd20(_handle_ , _speed_class_control_ , _see_command_descriptor_ , _timeout_us =1000000_)


cmd21()


cmd22(_handle_ , _reserved_ , _extend_address_ , _timeout_us =1000000_)


cmd23(_handle_ , _block_count_ , _timeout_us =1000000_)


cmd24(_handle_ , _data_address_ , _buffer_ , _blk_len =512_, _is_high_capacity =True_, _timeout_us =1000000_)


cmd25(_handle_ , _data_address_ , _data_length_ , _buffer_ , _blk_len =512_, _is_high_capacity =True_, _timeout_us =1000000_)


cmd26()


cmd27(_handle_ , _stuff_bits_ , _buffer_ , _timeout_us =1000000_)


cmd28(_handle_ , _data_address_ , _timeout_us =1000000_)


cmd29(_handle_ , _data_address_ , _timeout_us =1000000_)


cmd30(_handle_ , _data_address_ , _timeout_us =1000000_)


cmd31()


cmd32(_handle_ , _data_address_ , _timeout_us =1000000_)


cmd33(_handle_ , _data_address_ , _timeout_us =1000000_)


cmd34()


cmd35()


cmd36()


cmd37()


cmd38(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd39()


cmd40(_handle_ , _defind_by_DSP_spec_ , _timeout_us =1000000_)


cmd41()


cmd42(_handle_ , _reserved_bit_ , _blkLen_ , _buffer_ , _timeout_us =1000000_)


cmd43(_handle_ , _reserved_ , _task_id_ , _operation_Code_ , _timeout_us =1000000_)


cmd44(_handle_ , _wBlockCnt_ , _task_id_ , _Direction_ , _priority_ , _timeout_us =1000000_)


cmd45(_handle_ , _dwStartAddr_ , _timeout_us =1000000_)


cmd46(_handle_ , _data_address_ , _data_length_ , _timeout_us =1000000_)


cmd47(_handle_ , _buffer_ , _data_address_ , _data_length_ , _timeout_us =1000000_)


cmd48(_handle_ , _data_address_ , _timeout_us =1000000_)


cmd49(_handle_ , _buffer_ , _data_address_ , _timeout_us =1000000_)


cmd50()


cmd51()


cmd52()


cmd53()


cmd54()


cmd55(_handle_ , _rca_ , _stuff_bits_ , _timeout_us =1000000_)


cmd56(_handle_ , _stuff_bits_ , _rd_wr_ , _buffer =None_, _timeout_us =1000000_)


cmd57()


cmd58(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


cmd59()


cmd60()


cmd61()


cmd62()


cmd63()


get_cmd_exec_info()


get_device_capacity()


host_reset(_handle_)


sd_disable_clk(_handle_)


sd_enable_clk(_handle_)


sd_get_register(_handle_ , _dw_reg_)


sd_get_status(_handle_ , _timeout_us =1000000_)


sd_go_idle(_handle_)


sd_init(_handle_ , _is_continue_when_error =False_, _timeout_us =1000000_)


sd_read_d0(_handle_)


sd_set_bus_width(_handle_ , _bus_width =0_)


sd_set_clk(_handle_ , _clk =3000000_)


sd_set_speed_mode(_handle_ , _speed_mode =0_)


sd_set_timing(_handle_ , _clk =3000000_, _speed_mode =0_, _bus_width =0_)


sd_wait_ready(_handle_ , _timeout_us =1000000_)


wait_init_command_acmd41(_handle_ , _timeout_us =1000000_)

## Module contents
