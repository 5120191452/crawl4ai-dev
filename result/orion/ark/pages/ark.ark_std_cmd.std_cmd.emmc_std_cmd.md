---
title: "ark.ark_std_cmd.std_cmd.emmc_std_cmd package"
docname: "ark.ark_std_cmd.std_cmd.emmc_std_cmd"
source: "http://orion.longsys.com/ark.ark_std_cmd.std_cmd.emmc_std_cmd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_std_cmd.std_cmd.emmc_std_cmd package
## Submodules
## ark.ark_std_cmd.std_cmd.emmc_std_cmd.emmc_std_cmd module

_class _ark.ark_std_cmd.std_cmd.emmc_std_cmd.emmc_std_cmd.EMMCSTDCMD(_* args_, _** kwargs_)

Bases: [`ArkStdEmmcCmdInterface`](ark.ark_std_cmd.std_cmd.md#ark.ark_std_cmd.std_cmd.ark_std_emmc_cmd_interface.ArkStdEmmcCmdInterface "ark.ark_std_cmd.std_cmd.ark_std_emmc_cmd_interface.ArkStdEmmcCmdInterface")

cmd00(_handle_ , _arg_ , _timeout_us =1000000_)


Brief:

Sends CMD00 to switch the reset device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **arg** – (int) 32-bit argument, typically 0x00000000.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (None): CMD00 does not produce a response. - data (None): CMD00 does not return data.

cmd01(_handle_ , _ocr_ , _timeout_us =1000000_)


Brief:

Send CMD01.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **ocr** – (int) ocr value
  * **timeout_us** – (int) cmd01 time out time.


Return (tuple) A tuple containing:

  * res (int): Result of the command execution.
  * rsp (int or None): R3 response if successful, None otherwise.
  * data (None): CMD01 does not return data.


cmd01_till_ready(_handle_ , _ocr =1090486400_, _cnt =0_, _linkup_timeout_ms =1000_, _timeout_us =1000000_)


Brief:

Send CMD01 till device is not busy.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **ocr** – (int) ocr value
  * **cnt** – (int) if is set, the execution of cmd1 will repeat cnt times mostly.
  * **time_out** – (int) if cnt is not set, the execution of cmd1 will repeat time_out seconds mostly.
  * **timeout_us** – (int) Single cmd01 time out time.


Return (tuple) A tuple containing:

  * res (int): Result of the command execution.
  * link_up_time_out_ms (float): CMD01 ready time.


cmd02(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD02 to request the Card Identification (CID) register.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **stuff_bits** – (int) stuff_bits
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R2 response if successful, None otherwise. - data (None): CMD02 does not return data.

cmd03(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD03 to assign or query the Relative Card Address (RCA).

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **stuff_bits** – (int) stuff_bits
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD03 does not return data.

cmd04(_handle_ , _dsr_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD04 to set the Driver Strength Register (DSR).

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **dsr** – (int) 16-bit driver strength register value.
  * **stuff_bits** – (int) stuff_bits
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (None): CMD04 does not produce a response. - data (None): CMD04 does not return data.

cmd05(_handle_ , _rca_ , _sleep_or_awaken_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD05 to transition the device to or from sleep mode.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **sleep_or_awaken** – (int) sleep or awaken.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD05 does not return data.

cmd06(_handle_ , _access_ , _index_ , _value_ , _cmd_set_ , _zero26_31 =0_, _zero3_7 =0_, _timeout_us =1000000_)


Brief:

Sends CMD06 to switch functions or modify register values.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **access** – (int) 2-bit access mode (e.g., write byte or write bit).
  * **index** – (int) 8-bit register index.
  * **value** – (int) 8-bit value to write.
  * **cmd_set** – (int) 3-bit command set selection.
  * **zero26_31** – (int) All zero.
  * **zero3_7** – (int) All zero.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD06 does not return data.

cmd07(_handle_ , _rca_ , _stuff_bits =0_, _is_stand_by_state =False_, _is_deselect =False_, _timeout_us =1000000_)


Brief:

Sends CMD07 to select or deselect a device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address (0 to deselect).
  * **stuff_bits** – (int) Stuff bits.
  * **is_stand_by_state** – (bool) if in stand by state.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD07 does not return data.

cmd08(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD08 to get EXT_CSD register.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (bytes or None): EXT_CSD register if successful.

cmd09(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD09 to get the Card-Specific Data (CSD) register.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (list or None): R2 response if successful, None otherwise. - data (None): CMD09 does not return data.

cmd10(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends CMD10 to get the Card Identification (CID) register.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (list or None): R2 response if successful, None otherwise. - data (None): CMD10 does not return data.

cmd11()


Brief:

Not supported.

cmd12(_handle_ , _rca_ , _stuff_bits =0_, _hpi =0_, _is_read =True_, _timeout_us =1000000_)


Brief:

Forces the Device to stop transmission. If HPI flag is set the device shall interrupt its internal operations in a well-defined timing.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **stuff_bits** – (int) Stuff bits.
  * **hpi** – (int) hpi.
  * **is_read** – (bool) True means to stop a read command, otherwise a write command.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD12 does not return data.

cmd13(_handle_ , _rca_ , _sqs =0_, _stuff_bits =0_, _hpi =0_, _timeout_us =1000000_)


Brief:

Sends CMD13 to read the status of the card (CMD13 returns R1 response).

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **sqs** – (int) 1-bit status query selection, default is 0.
  * **stuff_bits** – (int) Stuff bits.
  * **hpi** – (int) 1-bit High-Power Index flag, default is 0.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD13 does not return additional data.

cmd14(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

A host reads the reversed bus testing data pattern from a Device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD14 does not return additional data.

cmd15(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sets the Device to inactive state

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) 16-bit relative card address.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (None): CMD15 does not produce a response. - data (None): CMD15 does not return data.

cmd16(_handle_ , _block_length_ , _timeout_us =1000000_)


Brief:

Sets the block length (in bytes) for all following block commands (read and write). Default block length is specified in the CSD.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **block_length** – (int) Desired block length in bytes.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD16 does not return data.

cmd17(_handle_ , _data_address_ , _timeout_us =1000000_)


Brief:

Sends CMD17 to read a single block of data.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) The address of the data to read.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - read_buffer (object): Buffer containing the read data.

cmd18(_handle_ , _data_address_ , _data_length_ , _timeout_us =1000000_)


Brief:

Sends CMD18 to read multiple blocks of data.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) The address of the first block to read.
  * **data_length** – (int) The number of blocks to read.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - read_buffer (object): Buffer containing the read data.

cmd19(_handle_ , _bus_width_ , _buffer_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sends the bus test data pattern to a Device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **bus_width** – (int) Width of the bus (e.g., 4 or 8 bits).
  * **buffer** – (object) The buffer containing the data to write.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD19 does not return data.

cmd20()


Brief:

Not supported.

cmd21(_handle_ , _buffer_ , _bit_mode =4_, _stuff_bits =0_, _timeout_us =1000000_)


Brief:

128 clocks of tuning pattern (64 byte in 4 bit mode or 128 byte in 8 bit mode) is sent for HS200 optimal sampling point detection

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **buffer** – (object) The buffer containing data to be send.
  * **bit_mode** – (int) Which bit mode, either 4 or 8.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD21 does not return data.

cmd22()


Brief:

Not supported.

cmd23(_handle_ , _num_of_blks_ , _reliable_write =0_, _packed =0_, _tag_request =0_, _context_id =0_, _force_programming =0_, _zero16_23_default =0_, _zero31_packed =0_, _zero16_29_packed =0_, _timeout_us =1000000_)


Brief:

Sends CMD23 to set the block count and other control flags for future operations.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **num_of_blks** – (int) Number of blocks to be addressed.
  * **reliable_write** – (int) A flag indicating if reliable write is enabled.
  * **packed** – (int) Indicating if packed is used.
  * **tag_request** – (int) A flag for tag request in the command.
  * **context_id** – (int) The context ID for the command.
  * **force_programming** – (int) A flag indicating whether to force programming.
  * **zero16_23_default** – (int) All zero.
  * **zero31_packed** – (int) All zero.
  * **zero16_29_packed** – (int) All zero.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD23 does not return data.

cmd24(_handle_ , _data_address_ , _buffer_ , _timeout_us =1000000_)


Brief:

Sends CMD24 to write data to the given address with a specified block length.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) Address where the data is to be written.
  * **buffer** – (object) The buffer containing the data to be written.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD24 does not return data.

cmd25(_handle_ , _data_address_ , _data_length_ , _buffer_ , _timeout_us =1000000_)


Brief:

Sends CMD25 to write multiple blocks of data starting from the specified address.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) Address to start writing the data.
  * **data_length** – (int) Number of blocks to be written.
  * **buffer** – (object) The buffer containing the data to be written.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD25 does not return data.

cmd26(_handle_ , _buffer_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Programming of the Device identification register. This command shall be issued only once. The Device contains hardware to prevent this operation after the first programming. Normally this command is reserved for the manufacturer.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **buffer** – (object) The buffer containing desired Device identification register value.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD26 does not return data.

cmd27(_handle_ , _buffer_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Programming of the programmable bits of the CSD.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **buffer** – (object) The buffer containing desired CSD register value.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD27 does not return data.

cmd28(_handle_ , _data_address_ , _timeout_us =1000000_)


Brief:

Sends CMD28 to perform a specific control operation on the given data address.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) The address to operate on.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD28 does not return data.

cmd29(_handle_ , _data_address_ , _timeout_us =1000000_)


Brief:

Sends CMD29 to perform a specific control operation on the given data address.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) The address to operate on.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD29 does not return data.

cmd30(_handle_ , _write_protect_data_address_ , _timeout_us =1000000_)


Brief:

SEND_WRITE_PROT command.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **write_protect_data_address** – (int) The address to operate on.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD30 does not return data.

cmd31(_handle_ , _write_protect_data_address_ , _timeout_us =1000000_)


Brief:

SEND_WRITE_PROT_TYPE command.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **write_protect_data_address** – (int) The address of the data to operate on.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD31 does not return data.

cmd32()


Brief:

Not supported.

cmd33()


Brief:

Not supported.

cmd34()


Brief:

Not supported.

cmd35(_handle_ , _data_address_ , _timeout_us =1000000_)


Brief:

Sets the address of the first erase group within a range to be selected for erase.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) The address of the first erase group.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD35 does not return data.

cmd36(_handle_ , _data_address_ , _timeout_us =1000000_)


Brief:

Sets the address of the last erase group within a continuous range to be selected for erase.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **data_address** – (int) The address of the last erase group.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD36 does not return data.

cmd37()


Brief:

Not supported.

cmd38(_handle_ , _secure_request =0_, _zero16_30 =0_, _force_garbage_collect =0_, _zero2_14 =0_, _discard_enable =0_, _trim_enable =0_, _timeout_us =1000000_)


Brief:

Erases all previously selected write blocks according to argument bits.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **secure_request** – (int) Flag to indicate a secure request (default 0).
  * **zero16_30** – (int) All zero.
  * **force_garbage_collect** – (int) Flag to force garbage collection (default 0).
  * **zero2_14** – (int) All zero.
  * **discard_enable** – (int) Flag to enable discard operation (default 0).
  * **trim_enable** – (int) Flag to enable trim operation (default 0).
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD38 does not return data.

cmd39(_handle_ , _rca_ , _register_write_flag_ , _register_address_ , _register_data =0_, _timeout_us =1000000_)


Brief:

Sends CMD39 to the MMC card for register read or write operation.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) Relative card address.
  * **register_write_flag** – (int) Flag indicating whether to write (1) or read (0) from the register.
  * **register_address** – (int) Address of the register.
  * **register_data** – (object) Data to be written if the write flag is set.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R4 response if successful, None otherwise. - data (None): CMD39 does not return data.

cmd40(_handle_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sets the system into interrupt mode.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R5 response if successful, None otherwise. - data (None): CMD40 does not return data.

cmd41()


Brief:

Not supported.

cmd42(_handle_ , _buffer_ , _stuff_bits =0_, _blk_len =512_, _timeout_us =1000000_)


Brief:

Used to set/reset the password or lock/unlock the Device. The size of the data block is set by the SET_BLOCK_LEN command.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **buffer** – (object) The buffer containing the data of lock/unlock info.
  * **blk_len** – (int) Block length in bytes, default is 512.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD42 does not return data.

cmd43()


Brief:

Not supported.

cmd44(_handle_ , _reliable_write_request_ , _dd_ , _tag_request_ , _context_id_ , _forced_programming_ , _priority_ , _task_id_ , _num_of_blks_ , _timeout_us =1000000_)


Brief:

Sends CMD44 to the MMC card for a complex command with multiple control flags.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **reliable_write_request** – (int) Flag indicating if reliable write is requested (1 = true, 0 = false).
  * **dd** – (int) Data direction flag (1 = read, 0 = write).
  * **tag_request** – (int) Tag request flag (1 = true, 0 = false).
  * **context_id** – (int) Context ID, a value between 0 and 15.
  * **forced_programming** – (int) Flag indicating forced programming (1 = true, 0 = false).
  * **priority** – (int) Priority flag (1 = high, 0 = simple).
  * **task_id** – (int) Task ID, a value between 0 and 31.
  * **num_of_blks** – (int) Number of blocks for the operation (up to 255).
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD44 does not return data.

cmd45(_handle_ , _start_block_address_ , _timeout_us =1000000_)


Brief:

Defines the block address of queued task.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **start_block_address** – (int) The start block address for the command.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD45 does not return data.

cmd46(_handle_ , _task_id_ , _blk_cnt_ , _reserved21_31 =0_, _reserved0_15 =0_, _timeout_us =1000000_)


Brief:

Device shall execute task from the queue whose ID is encoded in the argument.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **task_id** – (int) Task ID, a value between 0 and 31.
  * **blk_cnt** – (int) Block count to be read.
  * **reserved21_31** – (int) All zero.
  * **reserved0_15** – (int) All zero.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - read_buffer (ArkBuffer): The buffer containing the read data if the command succeeds.

cmd47(_handle_ , _task_id_ , _blk_cnt_ , _buffer_ , _reserved21_31 =0_, _reserved0_15 =0_, _timeout_us =1000000_)


Brief:

Device shall execute task from the queue whose ID is encoded in the argument.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **task_id** – (int) Task ID, a value between 0 and 31.
  * **blk_cnt** – (int) Block count to be written.
  * **buffer** – (Buffer) The buffer containing data to be written.
  * **reserved21_31** – (int) Reserved.
  * **reserved0_15** – (int) Reserved.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD47 does not return data.

cmd48(_handle_ , _task_id_ , _tm_opcode_ , _reserved21_31 =0_, _reserved4_15 =0_, _timeout_us =1000000_)


Brief:

Device shall discard a specific task or entire queue (all tasks in the queue).

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **task_id** – (int) Task ID, a value between 0 and 31.
  * **tm_opcode** – (int) TM operation code, a value between 0 and 15.
  * **reserved21_31** – (int) Reserved.
  * **reserved4_15** – (int) Reserved.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD48 does not return data.

cmd49(_handle_ , _buffer_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Sets the real time clock according to the RTC information in the 512 B data block

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **buffer** – (object) The buffer containing data to be written.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD49 does not return data.

cmd50()


Brief:

Not supported.

cmd51()


Brief:

Not supported.

cmd52()


Brief:

Not supported.

cmd53(_handle_ , _security_protocol_specific_ , _security_protocol_ , _data_length_ , _reserved =0_, _timeout_us =1000000_)


Brief:

Continuously transfers data blocks from device to host. Number of data blocks shall be defined by a preceding CMD23. Data Transfer may be interrupted by a STOP_TRANSMISSION command, This command is not supported if sent as a packed command. Block size is always 512bytes

cmd54(_handle_ , _security_protocol_specific_ , _security_protocol_ , _data_length_ , _buffer_ , _reserved =0_, _timeout_us =1000000_)


Brief:

Continuously transfers data blocks from device to host. Number of data blocks shall be defined by a preceding CMD23. Data Transfer may be interrupted by a STOP_TRANSMISSION command, This command is not supported if sent as a packed command. Block size is always 512bytes

cmd55(_handle_ , _rca_ , _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Indicates to the Device that the next command is an application specific command rather than a standard command.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rca** – (int) The Relative Card Address.
  * **stuff_bits** – (int) Stuff bits.
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - data (None): CMD55 does not return data.

cmd56(_handle_ , _rd_or_wr1 =1_, _buffer =None_, _stuff_bits =0_, _timeout_us =1000000_)


Brief:

Used either to transfer a data block to the Device or to get a data block from the Device for general purpose / application specific commands. The size of the data block shall be set by the SET_BLOCK_LEN command.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **rd_or_wr1** – (int) Indicating whether the operation is read (1) or write (0).
  * **buffer** – (object) Buffer containing the data to be written (if rd is 0) or to be used to read data (if rd is 1).
  * **timeout_us** – (int) cmd time out time in us.


Returns:

(tuple) A tuple containing: - res (int): Result of the command execution. - rsp (int or None): R1 response if successful, None otherwise. - read_buffer (object): The buffer containing data read from the card if rd is 1, otherwise None.

cmd57()


Brief:

Not supported.

cmd58()


Brief:

Not supported.

cmd59()


Brief:

Not supported.

cmd60()


Brief:

Not supported.

cmd61()


Brief:

Not supported.

cmd62()


Brief:

Not supported.

cmd63()


Brief:

Not supported.

emmc_get_cid(_handle_)


Brief:

Get the CID register from the eMMC device. Usable in Transfer state. For Standby state, use cmd10.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - cid (list) CID register

emmc_get_csd(_handle_)


Brief:

Get the CSD register from the eMMC device. Usable in Transfer state. For Standby state, use cmd09.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - csd (list) CSD register

emmc_get_ext_csd(_handle_)


Brief:

Get extended csd register from the emmc device.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - ext_csd (ark_buffer) EXT_CSD register

emmc_get_manufacturer_id(_handle_)


Brief:

Get mid from the emmc device.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - mid (int) MID value.

emmc_get_register(_handle_ , _dw_reg_)


Brief:

Get a register value from the emmc device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **dwreg** – (int) The register address to read.


Returns:

(int) Register value.

emmc_get_status(_handle_)


Brief:

Get status of the emmc device.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - status (int) Device status register

emmc_go_idle(_handle_)


Brief:

Put the emmc device into idle state.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_packed_reads(_handle_ , _packed_cmds_)


Brief:

Packed reads data from emmc device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **packed_cmds** – (list) A list containing several tuples of addresses and lengths.


Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - buffer (ark_buffer) Read data.

emmc_packed_writes(_handle_ , _packed_cmds_ , _write_buffer_)


Brief:

Packed writes data to emmc device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **packed_cmds** – (list) A list containing several tuples of addresses and lengths.
  * **write_buffer** – (ark_buffer) Write buffer.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_read_d0(_handle_)


Brief:

Read d0 from the emmc device.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(int) D0 status

emmc_rpmb_config_read(_handle_ , _register_index_)


Brief:

Authenticated Device Configuration read.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **register_index** – (int) The index of Device Configuration register to be read.


Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - read_buffer (ark_buffer): Buffer containing the read data.

emmc_rpmb_config_write(_handle_ , _register_index_ , _write_data_ , _write_cnt =None_)


Brief:

Authenticated Device Configuration write.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **register_index** – (int) The index of Device Configuration register to be updated.
  * **write_data** – (ark_buffer) Write buffer.
  * **write_counter** – (int) Write counter, default to None and write counter will be fetched inside this interface.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_rpmb_get_write_counter(_handle_)


Brief:

Read the Write Counter value of rpmb partition.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - write_counter (int) Write counter.

emmc_rpmb_read(_handle_ , _startlba_ , _blkcnt_)


Brief:

Authenticated data read.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **startlba** – (int) Address to start reading the data.
  * **blkcnt** – (int) Number of blocks to be read.


Returns:

(tuple) A tuple containing: - res (int) Error code (0 if successful, non-zero if an error occurred). - read_buffer (ark_buffer): Buffer containing the read data.

emmc_rpmb_set_key(_handle_)


Brief:

Set authentication key to rpmb partition.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_rpmb_write(_handle_ , _startlba_ , _blkcnt_ , _write_data_ , _write_cnt =None_)


Brief:

Authenticated data write.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **startlba** – (int) Address to start writing the data.
  * **blkcnt** – (int) Number of blocks to be written.
  * **write_data** – (ark_buffer) Write buffer.
  * **write_counter** – (int) Write counter, default to None and write counter will be fetched inside this interface.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_send_cmd0_with_0xfffffffa_state(_handle_)


Brief:

Performs eMMC alternative boot operation (CMD0 with 0xFFFFFFFA argument) and retrieves boot data with timing.

Parameters:

**handle** – (int) The handle to the eMMC device interface.

Returns:

(tuple) A tuple containing: - result (int): Execution status or error code. - buffer (ArkBuffer): The boot data read from the device (only read 2 sectors, 1024 bytes). - ack_time_us (int): Time in microseconds between CMD0 and the device’s boot ACK signal. - first_block_time_us (int): Time in microseconds until the first boot data block is received.

emmc_set_blocklen(_handle_ , _dw_len_)


Brief:

Set the block length for the emmc device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **dw_len** – (int) Length to set.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_stop_transmission(_handle_ , _is_read =True_)


Brief:

Stop transmission for the emmc device.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_switch(_handle_ , _b_access_ , _w_index_ , _b_value_ , _timeout_us =1000000_)


Brief:

Switch the emmc device settings.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **b_access** – (int) Access bits in switch command.
  * **w_index** – (int) Index bits in switch command.
  * **b_value** – (int) Value bits in switch command.
  * **timeout_us** – (int) cmd06 and cmd13 time out time in us.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_switch_to_rpmb(_handle_)


Brief:

Switch to operate on rpmb partition.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_switch_to_user_data_area(_handle_)


Brief:

Switch to operate on user data area.

Parameters:

**handle** – (object) The handle to the emmc device.

Returns:

(int) Error code (0 if successful, non-zero if an error occurred).

emmc_transfer_original_boot_data(_handle_)


Brief:

Performs eMMC original boot operation and retrieves boot data along with timing information.

Parameters:

**handle** – (int) The handle to the eMMC device interface.

Returns:

(tuple) A tuple containing: - result (int): Execution status or error code. - buffer (ArkBuffer): The boot data read from the device (only read 2 sectors, 1024 bytes). - ack_time_us (int): Time in microseconds between CMD0 and the device’s boot ACK signal. - first_block_time_us (int): Time in microseconds until the first boot data block is received.

emmc_wait_cardstatus(_handle_ , _timeout_ms =1000_)


Brief:

Wait for the card status of the emmc device.

Parameters:

  * **handle** – (object) The handle to the emmc device.
  * **timeout_ms** – (int) Wait max time in ms.


Returns:

(int) Error code (0 if successful, non-zero if an error occurred).
## Module contents
