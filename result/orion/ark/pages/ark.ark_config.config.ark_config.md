---
title: "ark.ark_config.config.ark_config package"
docname: "ark.ark_config.config.ark_config"
source: "http://orion.longsys.com/ark.ark_config.config.ark_config.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_config.config.ark_config package
## Submodules
## ark.ark_config.config.ark_config.config module
@Project ：OrionProject @File ：ark_config.py @IDE ：VS Code @Author ：lu @Date ：2024/6/17 10:25

_class _ark.ark_config.config.ark_config.config.ArkConfig(_* args_, _** kwargs_)

Bases: [`ArkConfigInterface`](ark.ark_config.config.md#ark.ark_config.config.ark_config_interface.ArkConfigInterface "ark.ark_config.config.ark_config_interface.ArkConfigInterface")

get_parameter(_parameter_name =None_)


Brief:

Retrieves the value of a specified configuration parameter using a dot-separated key.

Parameters:

**parameter_name** –
str
The name of the parameter to retrieve, specified as a dot-separated string indicating the hierarchy of keys.
> example:
>> parameter_name = “electric.current”
If omitted or an empty string is provided, returns the entire configuration.

Returns:

Any Returns the value of the specified parameter if found.
If parameter_name is None or empty, returns the entire configuration dictionary.
If the parameter is not found, returns None.

init()


Brief:

load local config

Returns:

Returns 0 if the local config is successfully loaded, otherwise returns an error code

update_config(_update_info_)


Brief:

Updates the configuration based on the provided update information, which can be in the form of a dictionary, a file path, or a string.

Parameters:

**update_info** –
dict
A dictionary containing the type of update and the corresponding data. The keys should be from the UpdateType enumeration, and the values can be:
  * A dictionary of key-value pairs (UpdateType.config_dict)
  * A file path to a YAML file (UpdateType.file_path)
  * A string containing YAML formatted key-value pairs (UpdateType.config_string)


Returns:

int Returns 0 if the update operation is successful, otherwise returns an error code.

update_config_from_file(_file_path_)


Brief:

Updates the configuration by reading key-value pairs from a specified YAML/json/ini file.

Parameters:

**file_path** –
str
The path to the YAML file containing configuration key-value pairs.
> example:
>> file_path = r”D:\pycode\Orion_ark\config\pytest\haha.yaml”

Returns:

int Returns 0 if the update operation is successful, otherwise returns an error code.

update_config_from_key_value(_config_dict_)


Brief:

Updates the configuration based on a dictionary of key-value pairs.

Parameters:

**config_dict** –
dict A dictionary containing configuration keys and their corresponding values. example:
> config_dict = {“electric”: {“current”: 40}}
> note: while using this interface in the command line, it should be a backslash before double quote to avoid the double quote being interpreted as something else

Returns:

int Returns 0 if the update operation is successful, otherwise returns an error code.

update_config_from_string(_config_string_)


Brief:

Updates the configuration by parsing key-value pairs from a given string in YAML format.

Parameters:

**config_string** –
str
A string containing configuration key-value pairs in YAML format.
>

example:

> config_string =
>> ’’’
>> electric:
>>> current: 90
>> ’’’
> note: while using this interface in the command line, and it need to be written in one row, it can be like
>> r”electric:\n current: 90”

Returns:

int Returns 0 if the update operation is successful, otherwise returns an error code.

update_missing_config(_section_name_ , _new_config_path_)


Brief:

Update specific section config items to the latest according to the new config. The update will proceed only if the version differs between the current and new configs. This interface will not change the value of existing keys in the current config; it will only add keys and values that do not already exist.

Parameters:

**section_name** – the name of the section to update in config. new_config_path: the path of the new config.

Returns:

int Returns 0 if the update operation is successful, otherwise returns an error code.

_class _ark.ark_config.config.ark_config.config.UpdateType(_value_)

Bases: `Enum`
An enumeration.

config_dict _ = 1_


config_string _ = 3_


file_path _ = 2_


ark.ark_config.config.ark_config.config.get_parser()


ark.ark_config.config.ark_config.config.handle_command(_parser_ , _config_manager_)

## Module contents
