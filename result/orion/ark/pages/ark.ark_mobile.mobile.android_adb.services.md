---
title: "ark.ark_mobile.mobile.android_adb.services package"
docname: "ark.ark_mobile.mobile.android_adb.services"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.services.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.services package
## Submodules
## ark.ark_mobile.mobile.android_adb.services.app module
Non-UI Android application control and gallery queries.

_class _ark.ark_mobile.mobile.android_adb.services.app.AppService(_session_)

Bases: `object`

gallery_counts()


stop_app(_app_id : str_, _timeout_s : float_)

## ark.ark_mobile.mobile.android_adb.services.device module
Android connection, battery, screen and reboot workflows.

_class _ark.ark_mobile.mobile.android_adb.services.device.DeviceService(_session_)

Bases: `object`

INTERACTIVE_LEASE_S _ = 15.0_


RECOVER_PACKAGE _ = 'com.phoneauto.adbrecover'_


battery_percent() → Tuple[int, int | None]


ensure_interactive(_timeout_s : float_)


reboot(_timeout_s : float_) → Tuple[int, [MobileReconnectResult](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobileReconnectResult "ark.ark_mobile.mobile.contracts.models.MobileReconnectResult")]


reconnect(_timeout_s : float_, _previous_boot_id : str | None = None_) → Tuple[int, [MobileReconnectResult](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobileReconnectResult "ark.ark_mobile.mobile.contracts.models.MobileReconnectResult")]


turn_screen(_on : bool_, _timeout_s : float_, _unlock : bool = False_) → Tuple[int, [MobileOperationResult](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobileOperationResult "ark.ark_mobile.mobile.contracts.models.MobileOperationResult")]

## ark.ark_mobile.mobile.android_adb.services.file module
File and text-content business operations.

_class _ark.ark_mobile.mobile.android_adb.services.file.FileService(_session_ , _storage_service_ , _ui_ , _device_service_)

Bases: `object`

append(_path_ , _content_ , _encoding_)


compare(_source : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _destination : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_)


copy(_source : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _destination_directory : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _overwrite : bool_, _timeout_s : float_)


create_directory(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _parents : bool_, _exist_ok : bool_)


delete(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _recursive : bool_)


delete_field(_path_ , _field_ , _encoding_)


info(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_)


load_file(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _observation_duration_s : float_)


read(_path_ , _start_line_ , _line_count_ , _encoding_)


rename(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _new_name : str_, _overwrite : bool_)


stat_absolute(_absolute : str_, _exclude_name : str = ''_)


update_field(_path_ , _field_ , _value_ , _encoding_)


video_frame_rate(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_)

## ark.ark_mobile.mobile.android_adb.services.file_content module
Text-file content operations shared by supported Android models.

_class _ark.ark_mobile.mobile.android_adb.services.file_content.FileContentService(_storage_ , _helper_)

Bases: `object`

append(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _content : str_, _encoding : str_)


delete_field(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _field : str_, _encoding : str_)


read(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _start_line : int_, _line_count : int | None_, _encoding : str_)


update_field(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _field : str_, _value : str_, _encoding : str_)

## ark.ark_mobile.mobile.android_adb.services.file_helper module
Transport for an externally installed FileHelper application.

_class _ark.ark_mobile.mobile.android_adb.services.file_helper.FileHelper(_session_ , _screen_)

Bases: `object`

call(_op : str_, _timeout_s : float = 120.0_, _** extras_)


_static _info(_path : [MobilePath](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePath "ark.ark_mobile.mobile.contracts.models.MobilePath")_, _data : Dict_) → [MobilePathInfo](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.MobilePathInfo "ark.ark_mobile.mobile.contracts.models.MobilePathInfo")

## ark.ark_mobile.mobile.android_adb.services.file_helper_protocol module
Validate successful FileHelper responses at the APK protocol boundary.

ark.ark_mobile.mobile.android_adb.services.file_helper_protocol.validate_result(_operation_ , _data_)

## ark.ark_mobile.mobile.android_adb.services.interactive module
Optional device-specific interactive readiness strategies.

ark.ark_mobile.mobile.android_adb.services.interactive.wake_then_unlock(_service_ , _timeout_s_)

Wake without the slow power dump, then verify only keyguard state.
## ark.ark_mobile.mobile.android_adb.services.lexar module
Cross-device Lexar application backup flow with verified stage transitions.

_class _ark.ark_mobile.mobile.android_adb.services.lexar.LexarBackupFlow(_session_ , _storage_service_ , _file_service_ , _ui_)

Bases: `object`
Complete Lexar UI flow; every click verifies its expected next state.

run(_timeout_s : float_, _terminal_capture =None_)

## ark.ark_mobile.mobile.android_adb.services.media_files module
Android media snapshots used to verify camera operations.

_class _ark.ark_mobile.mobile.android_adb.services.media_files.MediaFiles(_session_ , _file_service_)

Bases: `object`

IMAGE_EXTENSIONS _ = {'.dng', '.gif', '.heic', '.jpeg', '.jpg', '.png', '.webp'}_


VIDEO_EXTENSIONS _ = {'.3gp', '.mkv', '.mov', '.mp4', '.webm'}_


_static _new_paths(_before_ , _after_)


roots(_test_storage =None_, _include_test_storage =True_)


snapshot(_roots_ , _extensions_)

## ark.ark_mobile.mobile.android_adb.services.playback module
PC-side playback observation shared by Android model adapters.

_class _ark.ark_mobile.mobile.android_adb.services.playback.PlaybackObservation(_state : str_, _source : str | None_, _duration_ms : int_, _error : str | None = None_)

Bases: `object`

duration_ms _: int_


error _: str | None_ _ = None_


source _: str | None_


state _: str_


_class _ark.ark_mobile.mobile.android_adb.services.playback.PlaybackObserver(_session_)

Bases: `object`
Observe another app without placing device-specific rules in the API.

observe(_package : str_, _title : str_, _duration_s : float_, _ui_probe : Callable[[], [PlaybackUiEvidence](ark.ark_mobile.mobile.android_adb.services.md#ark.ark_mobile.mobile.android_adb.services.playback.PlaybackUiEvidence "ark.ark_mobile.mobile.android_adb.services.playback.PlaybackUiEvidence")]_, _resume : Callable[[], bool]_, _foreground : Callable[[], bool]_, _recover : Callable[[], bool] | None = None_, _foreground_verified : bool = False_, _resume_unknown : bool = False_, _start_timeout_s : float = 8.0_, _wait_for_initial_stopped : bool = False_) → [PlaybackObservation](ark.ark_mobile.mobile.android_adb.services.md#ark.ark_mobile.mobile.android_adb.services.playback.PlaybackObservation "ark.ark_mobile.mobile.android_adb.services.playback.PlaybackObservation")


_class _ark.ark_mobile.mobile.android_adb.services.playback.PlaybackUiEvidence(_state : str | None = None_, _error : str | None = None_, _fallback_error : str | None = None_)

Bases: `object`
Optional model-specific evidence extracted from the current UI.

error _: str | None_ _ = None_


fallback_error _: str | None_ _ = None_


state _: str | None_ _ = None_

## ark.ark_mobile.mobile.android_adb.services.playback_progress module
Adapter-directed UI progress evidence for Android media viewers.

ark.ark_mobile.mobile.android_adb.services.playback_progress.read_playback_progress(_ui_ , _adapter_ , _kind_)

Return the visible player position, revealing controls when required.

ark.ark_mobile.mobile.android_adb.services.playback_progress.verify_playback_progress(_ui_ , _adapter_ , _kind_)

Require repeated forward movement, not a single seek or restored offset.
## ark.ark_mobile.mobile.android_adb.services.reconnect module
Reboot recovery restricted to the bound device’s known transports.

_class _ark.ark_mobile.mobile.android_adb.services.reconnect.AdbReconnect(_session_)

Bases: `object`

boot_id()


run(_timeout_s : float_, _previous_boot_id =None_)

## ark.ark_mobile.mobile.android_adb.services.screenshot module
Host-side screenshot capture for Android/ADB operations.

_class _ark.ark_mobile.mobile.android_adb.services.screenshot.ScreenshotService(_session_)

Bases: `object`

REMOTE_DIRECTORY _ = '/data/local/tmp/ark_mobile'_


capture(_host_directory_ , _operation : str_)

## ark.ark_mobile.mobile.android_adb.services.session_cleanup module
Best-effort release of per-session external resources.

ark.ark_mobile.mobile.android_adb.services.session_cleanup.close_ui(_ui_)

## ark.ark_mobile.mobile.android_adb.services.storage module
Test-volume discovery, selection, operations and path resolution.

_class _ark.ark_mobile.mobile.android_adb.services.storage.StorageService(_session_)

Bases: `object`

eject(_selector : [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector") | None_, _timeout_s : float_)


format(_selector : [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector") | None_, _timeout_s : float_)


get_storage_info()


get_volume(_selector : [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector") | None_, _refresh : bool = True_)


list_volumes(_refresh : bool = True_)


mount(_selector : [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector") | None_, _timeout_s : float_)


resolve_path(_location_ , _relative_path : str_, _selector : [TestStorageSelector](ark.ark_mobile.mobile.contracts.md#ark.ark_mobile.mobile.contracts.models.TestStorageSelector "ark.ark_mobile.mobile.contracts.models.TestStorageSelector") | None_)

## ark.ark_mobile.mobile.android_adb.services.storage_discovery module
Android vold and mount-table discovery.

_class _ark.ark_mobile.mobile.android_adb.services.storage_discovery.StorageDiscovery(_session_)

Bases: `object`

discover()


list_disks()


_class _ark.ark_mobile.mobile.android_adb.services.storage_discovery.Volume(_volume_id : 'str'_, _state : 'str'_, _uuid : 'Optional[str]'_, _mount_path : 'Optional[str]'_, _filesystem : 'Optional[str]'_, _label : 'Optional[str]'_, _device_node : 'Optional[str]'_, _disk_id : 'Optional[str]'_, _writable : 'Optional[bool]'_)

Bases: `object`

device_node _: str | None_


disk_id _: str | None_


filesystem _: str | None_


label _: str | None_


mount_path _: str | None_


state _: str_


uuid _: str | None_


volume_id _: str_


writable _: bool | None_

## ark.ark_mobile.mobile.android_adb.services.values module
Small value conversions shared by Android service parsers.

ark.ark_mobile.mobile.android_adb.services.values.float_or_none(_value_)


ark.ark_mobile.mobile.android_adb.services.values.int_or_none(_value_)

## Module contents
Android/ADB business services.
