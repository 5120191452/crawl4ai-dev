---
title: "ark.ark_ssd.ssd package"
docname: "ark.ark_ssd.ssd"
source: "http://orion.longsys.com/ark.ark_ssd.ssd.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_ssd.ssd package
## Submodules
## ark.ark_ssd.ssd.ark_ssd_factory module

_class _ark.ark_ssd.ssd.ark_ssd_factory.ArkSSDFactory(_* args_, _** kwargs_)

Bases: `object`

create_object()

## ark.ark_ssd.ssd.ark_ssd_interface module

_class _ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule(_value_)

Bases: `str`, `Enum`
An enumeration.

EQ _ = 'eq'_


GT _ = 'gt'_


LT _ = 'lt'_


_class _ark.ark_ssd.ssd.ark_ssd_interface.OutputFormat(_value_)

Bases: `str`, `Enum`
An enumeration.

JSON _ = 'json'_


TEXT _ = 'text'_


_class _ark.ark_ssd.ssd.ark_ssd_interface.SSDInterface

Bases: `object`
NVMe device management and query interface.

nvme_dev_format(_device_path : str_, _lbaf : int = 0_, _ses : int = 1_) → dict


Brief:

Format the NVMe namespace with the specified LBA format.

Note:

This operation is currently supported only on Linux.

Parameters:

  * **device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”
  * **lbaf** – int LBA format index.
  * **ses** – int Secure erase setting.


Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”command_output”: str

>> Raw command output.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “Format success”, “data”: {
> “command_output”: “Success formatting namespace:1”
}, “error”: None
}

nvme_dev_get_all_nvme_list() → dict


Brief:

Retrieve a structured list of all NVMe devices detected on the system.

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”nvme_list”: list[dict]


Each item includes:


”device_alias”: str | int

>> Device alias identifier. Linux example: “nvme0n1” Windows example: “0”

”dev_path”: str

>> Full physical device path.

”sn”: str

>> Device serial number.

”model”: str

>> Device model name.

”namespace”: int

>> Namespace ID.

”capacity_bytes”: int

>> Device capacity in bytes.

”capacity_raw”: str

>> Raw capacity string reported by the underlying tool. In Linux: nvme list output. In Windows: diskpart list disk output.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
>

“nvme_list”: [


{

> “device_alias”: “nvme0n1”, “dev_path”: “/dev/nvme0n1”, “sn”: “ABC123456”, “model”: “Example NVMe SSD”, “namespace”: 1, “capacity_bytes”: 512110190592, “capacity_raw”: “512.11 GB”
> }
> ]
}, “error”: None
}

nvme_dev_get_basic_info(_device_path : str_) → dict


Brief:

Retrieve basic information of the specified NVMe device.

Parameters:

**device_path** –
str In Linux: Full NVMe namespace path. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”sn”: str

>> Serial number.

”model”: str

>> Device model name.

”firmware”: str

>> Firmware version.

”capacity_bytes”: int

>> Device capacity in bytes.

”capacity_raw”: str:

>> Raw capacity string reported by the underlying tool. In Linux: nvme list output. In Windows: diskpart list disk output.

”nvme_version”: str

>> NVMe specification version string.

”nvme_version_hex”: str

>> NVMe version in hexadecimal format.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “sn”: “ABC123456”, “model”: “Example NVMe SSD”, “firmware”: “1.2A”, “capacity_bytes”: 512110190592, “capacity_raw”: “512.11 GB”, “nvme_version”: “1.4”, “nvme_version_hex”: “0x10400”
}, “error”: None
}

nvme_dev_get_controller_and_pci_address(_device_path : str_) → dict


Brief:

Retrieve the controller name and PCIe BDF address of the specified NVMe device.

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** – str In Linux: Full NVMe namespace path. Example: “/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>> ”controller”: str “pci_address”: str
>>> PCIe BDF address (e.g., “0000:5e:00.0”).

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “controller”: “nvme0”, “pci_address”: “0000:5e:00.0”
}, “error”: None
}

nvme_dev_get_from_controller(_device_path : str_) → dict


Brief:

Retrieve the physical NVMe device and associated logical drives from a controller.

Parameters:

**device_path** –
str In Linux: NVMe controller name. Example: “nvme0”
In Windows: Physical disk index. Example: “0”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”physical_path”: str

>> Physical NVMe device path.

”drive_letter”: list[str]

>> Logical drive letters mapped to this device.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “physical_path”: “/dev/nvme0n1”, “drive_letter”: [“/dev/nvme0n1p1”, “/dev/nvme0n1p2”]
}, “error”: None
}

nvme_dev_get_identify_controller_info(_device_path : str_, _output_format : [OutputFormat](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.OutputFormat "ark.ark_ssd.ssd.ark_ssd_interface.OutputFormat") = OutputFormat.TEXT_) → dict


Brief:

Retrieve Identify Controller information of the NVMe device.

Parameters:

  * **device_path** –
str In Linux: Full NVMe namespace path. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”
  * **output_format** –
OutputFormat Output format of the Identify Controller data.

Supported values:

TEXT - Raw command output. JSON - Structured JSON output.


Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok.

Contains:


”content”: Any

> Returned payload. - str when output_format == OutputFormat.TEXT - dict when output_format == OutputFormat.JSON

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “content”: “NVME Identify Controller…”
}, “error”: None
}

nvme_dev_get_power_state(_device_path : str_) → dict


Brief:

Retrieve the current NVMe power state.

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** – str NVMe namespace path. Example: “/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None
>

Contains:


”current_ps”: int

> Current power state.

”command_output”: str

> Raw command output.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “current_ps”: 3, “command_output”: “Current value: 0x3”
}, “error”: None
}

nvme_dev_get_sector_info(_device_path : str_) → dict


Brief:

Retrieve LBA format information and sector sizes of the NVMe namespace.

Parameters:

**device_path** –
str In Linux: Full NVMe namespace path. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”in_use_sector_size_bytes”: int

>> Sector size currently in use.

”in_use_lbads”: int

>> LBA data size exponent (LBADS).

”optional_sector_size_bytes”: list[int]

>> Optional sector sizes supported by the device.

”optional_lbads”: list[int]

>> LBADS values corresponding to optional sector sizes.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “in_use_sector_size_bytes”: 512, “in_use_lbads”: 9, “optional_sector_size_bytes”: [4096], “optional_lbads”: [12]
}, “error”: None
}

nvme_dev_is_support_write_zeroes(_device_path : str_) → dict


Brief:

Check whether the NVMe device supports Write Zeroes.

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** –
str NVMe device path.

Linux example:

”/dev/nvme0n1”

Windows example:

”0”

Returns:

dict code: int msg: str data: dict | None
>

Contains:

> ”support_write_zeroes”: bool

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “support_write_zeroes”: true
}, “error”: None
}

nvme_dev_set_power_state(_device_path : str_, _power_state : int_) → dict


Brief:

Set the NVMe power state.

Note:

This operation is currently supported only on Linux.

Parameters:

  * **device_path** – str NVMe namespace path. Example: “/dev/nvme0n1”
  * **power_state** – int Target power state.


Returns:

dict code: int msg: str data: dict | None
>

Contains:


”current_ps”: int

> Power state set.

”command_output”: str

> Raw command output.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “current_ps”: 3, “command_output”: “set-feature success”
}, “error”: None
}

nvme_hw_device_remove(_device_path : str_) → dict


Brief:

Remove the NVMe device from the PCI bus.

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None error: dict | None
> Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: None, “error”: None
}

nvme_hw_device_rescan() → dict


Brief:

Trigger a PCI bus rescan to detect newly added or reattached devices.

Note:

This operation is currently supported only on Linux.

Returns:

dict code: int msg: str data: dict | None error: dict | None
> Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: None, “error”: None
}

nvme_hw_disable_apst(_device_path : str_) → dict


Brief:

Disable NVMe Autonomous Power State Transition (APST).

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None error: dict | None
> Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: None, “error”: None
}

nvme_hw_get_pcie_aspm(_device_path : str_) → dict


Brief:

Retrieve the current PCIe link control register value (lower 8 bits, ASPM related).

Note:

This operation is currently supported only on Linux.
The value is read from the lower byte (bits [7:0]) of the PCIe Link Control register (offset: CAP_EXP + 0x10).

The interface interprets the register value as follows:

  * 0x40 : ASPM disabled
  * 0x42 : ASPM enabled
  * others : ASPM state unknown


Parameters:

**device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”

Returns:

dict code: int msg: str
>

Possible values:

> ”Get success, ASPM enabled” “Get success, ASPM disabled” “Get success, state unknown”

data: dict | None


Contains:


”register_value”: str

Lower 8 bits of the raw link control register value.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “Get success, ASPM unknown”, “data”: {
> “register_value”: “0x03”
}, “error”: None
}

nvme_hw_get_pcie_l1pm_substates_cap(_device_path : str_) → dict


Brief:

Retrieve PCIe L1 PM Substates capability information.

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None
>

Contains:


”pci_pm_l12_supported”: bool

> Indicates whether PCI-PM L1.2 is supported.

”pci_pm_l11_supported”: bool

> Indicates whether PCI-PM L1.1 is supported.

”aspm_l12_supported”: bool

> Indicates whether ASPM L1.2 is supported.

”aspm_l11_supported”: bool

> Indicates whether ASPM L1.1 is supported.

”l1_pm_substates_supported”: bool

> Indicates whether L1 PM Substates are supported.

”register_value”: str

> Raw register value.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “pci_pm_l12_supported”: true, “pci_pm_l11_supported”: true, “aspm_l12_supported”: true, “aspm_l11_supported”: true, “l1_pm_substates_supported”: true, “register_value”: “0x0000001f”
}, “error”: None
}

nvme_hw_get_pcie_l1pm_substates_ctrl_l12(_device_path : str_) → dict


Brief:

Retrieve the PCIe L1 PM Substates control register value (Lower 8 bits, L1.2 related).

Note:

This operation is currently supported only on Linux.

The interface interprets the register value as follows:

  * 0x0f : L1.2 is considered enabled.
  * others : L1.2 state unknown.


Parameters:

**device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”

Returns:

dict code: int msg: str
>

Possible values:

> ”Get success, L1.2 enabled” “Get success, state unknown”

”data”: dict | None


Contains:

”pci_pm_l12_enabled”: bool, “pci_pm_l11_enabled”: bool, “aspm_l12_enabled”: bool, “aspm_l11_enabled”: bool, “register_value”: str
> Lower 8 bits of the raw control register value.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “Get success, L1.2 enabled”, “data”: {
> “pci_pm_l12_enabled”: true, “pci_pm_l11_enabled”: true, “aspm_l12_enabled”: true, “aspm_l11_enabled”: true, “register_value”: “0x0f”
}, “error”: None
}

nvme_hw_get_pcie_link_info(_device_path : str_) → dict


Brief:

Retrieve PCIe link capability and current link status of the NVMe device.

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** – str In Linux: Full NVMe namespace path. Example: “/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”current_gen”: str

>> Current PCIe generation.

”current_speed”: str

>> Current link speed.

”current_width”: str

>> Current link width.

”max_gen”: str

>> Maximum supported PCIe generation.

”max_speed”: str

>> Maximum supported link speed.

”max_width”: str

>> Maximum supported link width.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “current_gen”: “4.0”, “current_speed”: “16GT/s”, “current_width”: “x4”, “max_gen”: “4.0”, “max_speed”: “16GT/s”, “max_width”: “x4”
}, “error”: None
}

nvme_hw_get_pcie_link_info_by_register(_device_path : str_) → dict


Brief:

Retrieve PCIe link capability and current link status of the NVMe device by directly reading PCIe configuration space registers.

Note:

This operation is currently supported only on Linux. The information is obtained via PCIe registers (e.g., using setpci), which reflects the raw hardware-level values.

Register decoding (PCIe Link Status / Link Capabilities):

  * Bits [3:0] : Link Speed
  * Bits [9:4] : Link Width


Where:

  *

Link Speed encoding:

1 -> 2.5GT/s (Gen1) 2 -> 5GT/s (Gen2) 3 -> 8GT/s (Gen3) 4 -> 16GT/s (Gen4) 5 -> 32GT/s (Gen5) 6 -> 64GT/s (Gen6)
  *

Link Width encoding:

Value represents lane count directly (e.g., 1 -> x1, 4 -> x4, 8 -> x8)


Parameters:

**device_path** – str In Linux: Full NVMe namespace path. Example: “/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>>

”current_gen”: str

>> Current PCIe generation (decoded from register).

”current_speed”: str

>> Current link speed (decoded).

”current_width”: str

>> Current link width (decoded).

”max_gen”: str

>> Maximum supported PCIe generation (decoded).

”max_speed”: str

>> Maximum supported link speed (decoded).

”max_width”: str

>> Maximum supported link width (decoded).

”current_register_value”: str

>> Raw value of Link Status register first 10 bits (hex).

”max_register_value”: str

>> Raw value of Link Capabilities register first 10 bits (hex).

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “current_gen”: “4.0”, “current_speed”: “16GT/s”, “current_width”: “x4”, “max_gen”: “4.0”, “max_speed”: “16GT/s”, “max_width”: “x4”, “current_register_value”: “0x43”, “max_register_value”: “0x43”
}, “error”: None
}

nvme_hw_is_support_flr(_device_path : str_) → dict


Brief:

Check whether the NVMe device supports PCIe Function Level Reset (FLR).

Note:

This operation is currently supported only on Linux.

Parameters:

**device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”

Returns:

dict code: int msg: str data: dict | None
>

Contains:

> ”support_flr”: bool

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “support_flr”: true
}, “error”: None
}

nvme_hw_set_pcie_aspm(_device_path : str_, _value : int_) → dict


Brief:

Configure PCIe Link Control register (lower 8 bits, ASPM related).

Note:

This operation is currently supported only on Linux.
The value is written directly to the lower byte (bits [7:0]) of the PCIe Link Control register (offset: CAP_EXP + 0x10).
ASPM control is located at bits [1:0] of this register. However, this interface writes the entire lower byte following existing business behavior, which may affect other control bits.

Parameters:

  * **device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”
  * **value** – int Value written to the lower 8 bits of the link control register.


Returns:

dict code: int msg: str data: dict | None error: dict | None
> Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: None, “error”: None
}

nvme_hw_set_pcie_l1pm_substates_ctrl_l12(_device_path : str_, _value : int_) → dict


Brief:

Configure PCIe L1 PM Substates control register (Lower 8 bits, L1.2 related).

Note:

This operation is currently supported only on Linux.
The value is written directly to the lower byte (bits [7:0]) of the PCIe L1 PM Substates Control register.

Parameters:

  * **device_path** –
str NVMe namespace path.

Example:

”/dev/nvme0n1”
  * **value** – int Value written to the first byte of the L1 PM Substates control register.


Returns:

dict code: int msg: str data: dict | None error: dict | None
> Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: None, “error”: None
}

nvme_smart_check_batch(_device_path : str_, _check_items : list_) → dict


Brief:

Check multiple NVMe SMART parameters using baseline or threshold rules.

Parameters:

  * **device_path** –
str In Linux: Full NVMe namespace path with “/dev/” prefix. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”
  * **check_items** –
list[dict] List of SMART check configurations.

Each item must contain:

”param”: str
Optional comparison methods:
    1.

Base value comparison:


{

“param”: “percentage_used”, “base_value”: 5, “judge_rule”: JudgeRule.LT
}
    2.

Threshold comparison:


{

“param”: “composite_temperature”, “threshold”: {
> ”min”: 0, “max”: 70
}
}


Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok.

Contains:

> ”normal_items”: list[str] “abnormal_items”: list[str]

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
>

“normal_items”: [

> “percentage_used”, “power_on_hours”
> ], “abnormal_items”: [
>> “composite_temperature”
> ]
}, “error”: None
}

nvme_smart_check_single(_device_path : str_, _param : str_, _base_value : int_, _judge_rule : [JudgeRule](ark.ark_ssd.ssd.md#ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule "ark.ark_ssd.ssd.ark_ssd_interface.JudgeRule") = JudgeRule.EQ_) → dict


Brief:

Check a single NVMe SMART parameter against a baseline value.

Parameters:

  * **device_path** –
str In Linux: Full NVMe namespace path with “/dev/” prefix. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”
  * **param** – str SMART parameter name.
  * **base_value** – int Reference value used for comparison.
  * **judge_rule** –
JudgeRule Comparison rule.

Supported values:

EQ - equal to base_value GT - greater than base_value LT - less than base_value


Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok.

Contains:

> ”param”: str “current”: int “base”: int “diff”: int “is_normal”: bool

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “param”: “percentage_used”, “current”: 1, “base”: 5, “diff”: -4, “is_normal”: true
}, “error”: None
}

nvme_smart_get_batch(_device_path : str_, _params : list_) → dict


Brief:

Retrieve multiple NVMe SMART parameters at once.

Parameters:

  * **device_path** –
str In Linux: Full NVMe namespace path with “/dev/” prefix. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”
  * **params** –
list[str] List of NVMe SMART parameter names.

Example:


[

“composite_temperature”, “power_on_hours”, “percentage_used”
]


Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok.
> Contains a dictionary mapping parameter names to values.

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “composite_temperature”: 36, “power_on_hours”: 128, “percentage_used”: 1
}, “error”: None
}

nvme_smart_get_full(_device_path : str_) → dict


Brief:

Retrieve NVMe SMART / Health Information Log fields.
The returned data fields follow the NVMe specification “SMART / Health Information Log (Log Identifier 02h)” naming convention. Tool-specific field names are normalized to NVMe standard field names.

Parameters:

**device_path** – str NVMe device path. Example (Linux): “/dev/nvme0n1” Example (Windows internal mapping): “0”

Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok.
> SMART / Health Information fields (NVMe standard names), such as:
> critical_warning: int composite_temperature: int (Celsius) available_spare: int available_spare_threshold: int percentage_used: int data_units_read: int data_units_written: int host_read_commands: int host_write_commands: int controller_busy_time: int power_cycles: int power_on_hours: int unsafe_shutdowns: int media_and_data_integrity_errors: int number_of_error_information_log_entries: int warning_composite_temperature_time: int critical_composite_temperature_time: int temperature_sensor_1 ~ temperature_sensor_8: int(Celsius) thermal_management_temperature_1_transition_count: int thermal_management_temperature_2_transition_count: int total_time_for_thermal_management_temperature_1: int total_time_for_thermal_management_temperature_2: int

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

nvme_smart_get_single(_device_path : str_, _param : str_) → dict


Brief:

Retrieve a single NVMe SMART parameter.

Parameters:

  * **device_path** –
str In Linux: Full NVMe namespace path with “/dev/” prefix. Example: “/dev/nvme0n1”
In Windows: NVMe device index. Example: “0”
  * **param** –
str SMART parameter name defined in the NVMe SMART / Health Information Log.

Example:

”composite_temperature” “power_on_hours” “percentage_used”


Returns:

dict code: int msg: str data: dict | None
> Only present if code == err_ok. Contains:
>> ”param”: str “value”: int | float

error: dict | None

Only present if code != err_ok. Detailed error information. See unified return format definition.

Example:


{

“code”: 0, “msg”: “success”, “data”: {
> “param”: “power_on_hours”, “value”: 128
}, “error”: None
}
## Module contents
