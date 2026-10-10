---
title: "ark.ark_ipc.ipc package"
docname: "ark.ark_ipc.ipc"
source: "http://orion.longsys.com/ark.ark_ipc.ipc.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_ipc.ipc package
## Subpackages
  * [ark.ark_ipc.ipc.ark_ipc package](ark.ark_ipc.ipc.ark_ipc.md)
    * [Module contents](ark.ark_ipc.ipc.ark_ipc.md#module-ark.ark_ipc.ipc.ark_ipc)


## Submodules
## ark.ark_ipc.ipc.ark_ipc_factory module

_class _ark.ark_ipc.ipc.ark_ipc_factory.ArkIpcFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_ipc_type_)

## ark.ark_ipc.ipc.ark_ipc_interface module

_class _ark.ark_ipc.ipc.ark_ipc_interface.ArkIpcInterface

Bases: `ABC`

_abstract _capture_progress_bar_image(_ipc_number : str_, _save_path : str | None = None_) → Tuple[int, List[ndarray | None]]

Capture a progress bar image from the camera.

Args:

ipc_number: Device identifier. save_path: Optional path to save the stitched image.

Returns:


Tuple[int, List[Optional[np.ndarray]]]:

  * Error code (int).
  * A list containing images: `[stitched_image, last_frame_image]`. Returns an empty list (`[]`) if failed.


_abstract _check_app_login_status() → int

@brief: Check whether the app is in the main login screen. @return: int Error code (0 for logged in, non-zero for not logged in or failure).

_abstract _check_ipc_device_status() → int

@brief: Check if the IPC camera device is online. @return: int Error code.

_abstract _check_progress_bar_from_image(_image : str | ndarray_) → int

@brief: Check the progress bar status from the given image. @param image: Image file path or image array. @return: int Error code (0 for complete, non-zero for incomplete).

_abstract _check_sd_exist() → int

@brief: Check whether an SD card is inserted. @return: int Error code.

_abstract _find_ipc_device(_ipc_number : str_) → int

@brief: Search for a device by its IPC number. @param ipc_number: Device serial number. @return: int Error code.

_abstract _find_ui_with_ad_ui_handle(_find_ui_str : str_, _ad_img_path : str_, _ocr_text : List[str]_, _ad_ui : List[str]_) → Tuple[int, WebElement | None]

@brief: Find a UI element; if blocked by an ad, close the ad and retry. @param find_ui_str: UI path to find. @param ad_img_path: Image path of the ad. @param ocr_text: List of recognized text strings from OCR. @param ad_ui: List of ad UI paths to handle. @return: Tuple[int, Optional[WebElement]] Error code and found WebElement or None.

_abstract _full_day_recording_set() → int

@brief: Set the camera to record all day. @return: int Error code.

_abstract _get_ipc_brand() → Tuple[int, str]

Retrieve the IPC brand name.

Returns:


Tuple[int, str]:

  * Error code.
  * Brand name on success; empty string on failure.


_abstract _get_sd_capacity() → Tuple[int, float]

@brief: Get the SD card capacity. @return: Tuple[int, float] Error code and SD card size in GB.

_abstract _is_video_available() → int

@brief: Check whether a video has been recorded. @return: int Error code (0 if video is available, others for no video or error).

_abstract _kill_port_process() → int

Clear ADB port forwarding (`adb forward`) rules to free ports used by Appium/UiAutomator2.

Notes:

  * Attempts per-device cleanup with `adb -s <serial> forward --remove-all`; if no devices are attached, falls back to global `adb forward --remove-all`.
  * If no forwarding rules exist, still returns success.
  * This does not kill OS processes; it only removes ADB forwards. Any sessions relying on them (e.g., Appium, WebView remote debugging, Frida) will disconnect and must be re-established.


Returns:


int:

  * `self.error_list.err_ok`: Cleanup succeeded (including “nothing to clean”).
  * `self.module_err | self.error_list.err_close`: Cleanup failed for some/all devices.
  * `self.module_err | self.error_list.err_check`: ADB unavailable or unexpected error occurred.


_abstract _screenshot_and_find_text(_target_text : str_, _is_tap : bool = True_, _tap_count : int = 1_, _duration_ms : int = 1000_) → int

@brief: Take a screenshot, perform OCR, and optionally tap on the detected text. @param target_text: Text to find. @param is_tap: Whether to simulate a tap (default True). @param tap_count: Number of taps (default 1). @param duration_ms: Tap duration in milliseconds (default 1000). @return: int Error code.

_abstract _sd_format() → Tuple[int, int]

@brief: Format the SD card and simulate a long press on the confirmation. @return: int Error code and sd format time (s)

_abstract _set_ultra_hd_quality() → int

@brief: Set video quality to ultra HD. @return: int Error code.

_class _ark.ark_ipc.ipc.ark_ipc_interface.IpcType(_value_)

Bases: `Enum`
An enumeration.

EZVIZ _ = 'EZVIZ'_


HIKVISION _ = 'HIKVISION'_


HUAWEI _ = 'HUAWEI'_


IMOU _ = 'IMOU'_


Q360 _ = 'Q360'_


SKYWORTH _ = 'SKYWORTH'_


TP_LINK _ = 'TP_LINK'_


XIAOMI _ = 'XIAOMI'_

## Module contents
