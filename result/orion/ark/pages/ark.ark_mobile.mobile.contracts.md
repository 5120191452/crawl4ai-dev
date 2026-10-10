---
title: "ark.ark_mobile.mobile.contracts package"
docname: "ark.ark_mobile.mobile.contracts"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.contracts.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.contracts package
## Submodules
## ark.ark_mobile.mobile.contracts.error_info module
Structured error data returned by failed ark_mobile interfaces.

_class _ark.ark_mobile.mobile.contracts.error_info.MobileErrorInfo(_stage: str_, _message: str_, _source: str = 'ark_mobile'_, _native_return_code: int | None = None_, _raw_message: str = ''_, _details: ~typing.Dict[str_, _~typing.Any] = <factory>_)

Bases: `object`
Context created at one failure site; the outer code remains authoritative.

details _: Dict[str, Any]_


message _: str_


native_return_code _: int | None_ _ = None_


raw_message _: str_ _ = ''_


source _: str_ _ = 'ark_mobile'_


stage _: str_

## ark.ark_mobile.mobile.contracts.models module
Immutable values returned by the public mobile interface.

_class _ark.ark_mobile.mobile.contracts.models.MobileBackupResult(_completed : 'bool'_, _destination_path : 'Optional[MobilePath]' = None_, _backed_up_count : 'Optional[int]' = None_, _storage_added_count : 'Optional[int]' = None_, _storage_added_size_bytes : 'int' = 0_, _count_matched : 'Optional[bool]' = None_, _duration_ms : 'int' = 0_, _average_speed_bytes_per_second : 'float' = 0.0_, _message : 'str' = ''_, _screenshot_path : 'Optional[str]' = None_)

Bases: `object`

average_speed_bytes_per_second _: float_ _ = 0.0_


backed_up_count _: int | None_ _ = None_


completed _: bool_


count_matched _: bool | None_ _ = None_


destination_path _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath") | None_ _ = None_


duration_ms _: int_ _ = 0_


message _: str_ _ = ''_


screenshot_path _: str | None_ _ = None_


storage_added_count _: int | None_ _ = None_


storage_added_size_bytes _: int_ _ = 0_


_class _ark.ark_mobile.mobile.contracts.models.MobileCopyResult(_source : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _destination_directory : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _copied_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _object_type : str_, _copied_size_bytes : int_, _duration_ms : int_, _average_speed_bytes_per_second : float_)

Bases: `object`
Destination and transfer metrics reported by one copy operation.

average_speed_bytes_per_second _: float_


copied_path _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


copied_size_bytes _: int_


destination_directory _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


duration_ms _: int_


object_type _: str_


source _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


_class _ark.ark_mobile.mobile.contracts.models.MobileDeviceInfo(_transport_selector : 'str'_, _platform : 'MobilePlatform'_, _transport_endpoint : 'Optional[str]' = None_, _mdns_service : 'Optional[str]' = None_, _fixed_endpoint : 'Optional[str]' = None_, _manufacturer : 'Optional[str]' = None_, _brand : 'Optional[str]' = None_, _model : 'Optional[str]' = None_, _os_version : 'Optional[str]' = None_, _build_id : 'Optional[str]' = None_, _hardware_serial : 'Optional[str]' = None_, _adapter_name : 'Optional[str]' = None_)

Bases: `object`

adapter_name _: str | None_ _ = None_


brand _: str | None_ _ = None_


build_id _: str | None_ _ = None_


fixed_endpoint _: str | None_ _ = None_


hardware_serial _: str | None_ _ = None_


manufacturer _: str | None_ _ = None_


mdns_service _: str | None_ _ = None_


model _: str | None_ _ = None_


os_version _: str | None_ _ = None_


platform _: [MobilePlatform](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePlatform "ark.ark_mobile.mobile.contracts.models.MobilePlatform")_


transport_endpoint _: str | None_ _ = None_


transport_selector _: str_


_class _ark.ark_mobile.mobile.contracts.models.MobileFileLoadResult(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _loaded : bool_, _app_id : str | None = None_, _observed_state : str | None = None_, _observation_source : str | None = None_, _observation_duration_ms : int | None = None_, _message : str = ''_, _screenshot_path : str | None = None_)

Bases: `object`
Observable outcome of asking a device application to load one file.

app_id _: str | None_ _ = None_


loaded _: bool_


message _: str_ _ = ''_


observation_duration_ms _: int | None_ _ = None_


observation_source _: str | None_ _ = None_


observed_state _: str | None_ _ = None_


path _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


screenshot_path _: str | None_ _ = None_


_class _ark.ark_mobile.mobile.contracts.models.MobileGalleryCounts(_photo_count : 'int'_, _video_count : 'int'_)

Bases: `object`

photo_count _: int_


video_count _: int_


_class _ark.ark_mobile.mobile.contracts.models.MobileMediaResult(_files : 'Tuple[MobilePath, ...]'_, _created_count : 'int'_, _duration_ms : 'int' = 0_, _message : 'str' = ''_)

Bases: `object`

created_count _: int_


duration_ms _: int_ _ = 0_


files _: Tuple[[MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath"), ...]_


message _: str_ _ = ''_


_class _ark.ark_mobile.mobile.contracts.models.MobileOperationResult(_operation: str_, _duration_ms: int = 0_, _message: str = ''_, _details: ~typing.Dict[str_, _~typing.Any] = <factory>_)

Bases: `object`
Elapsed time and diagnostics for one completed state-changing operation.

details _: Dict[str, Any]_


duration_ms _: int_ _ = 0_


message _: str_ _ = ''_


operation _: str_


_class _ark.ark_mobile.mobile.contracts.models.MobilePath(_location : 'MobilePathLocation'_, _relative_path : 'str'_, _test_storage : 'Optional[TestStorageSelector]' = None_)

Bases: `object`

location _: [MobilePathLocation](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePathLocation "ark.ark_mobile.mobile.contracts.models.MobilePathLocation")_


relative_path _: str_


test_storage _: [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector") | None_ _ = None_


_class _ark.ark_mobile.mobile.contracts.models.MobilePathCompareResult(_source : 'MobilePath'_, _destination : 'MobilePath'_, _matched : 'bool'_, _difference : 'Optional[str]' = None_)

Bases: `object`

destination _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


difference _: str | None_ _ = None_


matched _: bool_


source _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


_class _ark.ark_mobile.mobile.contracts.models.MobilePathInfo(_path : 'MobilePath'_, _exists : 'bool'_, _is_directory : 'Optional[bool]' = None_, _size_bytes : 'Optional[int]' = None_, _modified_time : 'Optional[str]' = None_, _file_count : 'Optional[int]' = None_, _directory_count : 'Optional[int]' = None_)

Bases: `object`

directory_count _: int | None_ _ = None_


exists _: bool_


file_count _: int | None_ _ = None_


is_directory _: bool | None_ _ = None_


modified_time _: str | None_ _ = None_


path _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


size_bytes _: int | None_ _ = None_


_class _ark.ark_mobile.mobile.contracts.models.MobilePathLocation(_value_)

Bases: `str`, `Enum`
An enumeration.

INTERNAL_STORAGE _ = 'internal_storage'_


TEST_STORAGE _ = 'test_storage'_


_class _ark.ark_mobile.mobile.contracts.models.MobilePlatform(_value_)

Bases: `str`, `Enum`
An enumeration.

ANDROID _ = 'android'_


AUTO _ = 'auto'_


HARMONY _ = 'harmony'_


IOS _ = 'ios'_


_class _ark.ark_mobile.mobile.contracts.models.MobileReconnectResult(_connected : 'bool'_, _transport_selector : 'str'_, _duration_ms : 'int' = 0_, _message : 'str' = ''_, _transport_endpoint : 'Optional[str]' = None_, _mdns_service : 'Optional[str]' = None_)

Bases: `object`

connected _: bool_


duration_ms _: int_ _ = 0_


mdns_service _: str | None_ _ = None_


message _: str_ _ = ''_


transport_endpoint _: str | None_ _ = None_


transport_selector _: str_


_class _ark.ark_mobile.mobile.contracts.models.MobileVideoFrameRate(_path : 'MobilePath'_, _nominal_fps : 'Optional[float]'_, _actual_fps : 'Optional[float]'_, _duration_ms : 'Optional[int]' = None_, _frame_count : 'Optional[int]' = None_, _source : 'str' = ''_)

Bases: `object`

actual_fps _: float | None_


duration_ms _: int | None_ _ = None_


frame_count _: int | None_ _ = None_


nominal_fps _: float | None_


path _: [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_


source _: str_ _ = ''_


_class _ark.ark_mobile.mobile.contracts.models.MobileVideoSettings(_resolution : 'str'_, _frame_rate : 'int'_)

Bases: `object`

frame_rate _: int_


resolution _: str_


_class _ark.ark_mobile.mobile.contracts.models.TestStorageInfo(_disk_detected : 'bool'_, _disk_id : 'Optional[str]' = None_, _volumes : 'Tuple[TestVolumeInfo, ...]' = ()_, _capacity_bytes : 'Optional[int]' = None_)

Bases: `object`

capacity_bytes _: int | None_ _ = None_


disk_detected _: bool_


disk_id _: str | None_ _ = None_


volumes _: Tuple[[TestVolumeInfo](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestVolumeInfo "ark.ark_mobile.mobile.contracts.models.TestVolumeInfo"), ...]__ = ()_


_class _ark.ark_mobile.mobile.contracts.models.TestStorageSelector(_volume_id : 'Optional[str]' = None_, _disk_id : 'Optional[str]' = None_)

Bases: `object`

disk_id _: str | None_ _ = None_


volume_id _: str | None_ _ = None_


_class _ark.ark_mobile.mobile.contracts.models.TestVolumeInfo(_mounted : 'bool'_, _mount_path : 'Optional[str]' = None_, _filesystem : 'Optional[str]' = None_, _label : 'Optional[str]' = None_, _uuid : 'Optional[str]' = None_, _volume_id : 'Optional[str]' = None_, _device_node : 'Optional[str]' = None_, _disk_id : 'Optional[str]' = None_, _writable : 'Optional[bool]' = None_)

Bases: `object`

device_node _: str | None_ _ = None_


disk_id _: str | None_ _ = None_


filesystem _: str | None_ _ = None_


label _: str | None_ _ = None_


mount_path _: str | None_ _ = None_


mounted _: bool_


_property _selector _: [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector")_

Return a selector that identifies this discovered volume.

uuid _: str | None_ _ = None_


volume_id _: str | None_ _ = None_


writable _: bool | None_ _ = None_


_class _ark.ark_mobile.mobile.contracts.models.TestVolumeOperationResult(_storage : 'TestVolumeInfo'_, _duration_ms : 'int'_)

Bases: `object`

duration_ms _: int_


storage _: [TestVolumeInfo](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestVolumeInfo "ark.ark_mobile.mobile.contracts.models.TestVolumeInfo")_

## Module contents
Immutable public models used by `ark_mobile_interface`.
