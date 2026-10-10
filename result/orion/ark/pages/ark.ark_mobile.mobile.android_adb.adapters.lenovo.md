---
title: "ark.ark_mobile.mobile.android_adb.adapters.lenovo package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.lenovo"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.lenovo.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.lenovo package
## Subpackages
  * [ark.ark_mobile.mobile.android_adb.adapters.lenovo.models package](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md)
    * [Submodules](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#submodules)
    * [ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu module](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu)
      * [`LenovoTb321fuAdapter`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter)
        * [`LenovoTb321fuAdapter.camera_photo_keycode`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter.camera_photo_keycode)
        * [`LenovoTb321fuAdapter.camera_record_start_keycode`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter.camera_record_start_keycode)
        * [`LenovoTb321fuAdapter.camera_record_stop_keycode`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter.camera_record_stop_keycode)
        * [`LenovoTb321fuAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter.matches)
        * [`LenovoTb321fuAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter.name)
        * [`LenovoTb321fuAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.tb321fu.LenovoTb321fuAdapter.video_settings)
    * [Module contents](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.lenovo.models)
      * [`LenovoTb321fuAdapter`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter)
        * [`LenovoTb321fuAdapter.camera_photo_keycode`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter.camera_photo_keycode)
        * [`LenovoTb321fuAdapter.camera_record_start_keycode`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter.camera_record_start_keycode)
        * [`LenovoTb321fuAdapter.camera_record_stop_keycode`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter.camera_record_stop_keycode)
        * [`LenovoTb321fuAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter.matches)
        * [`LenovoTb321fuAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter.name)
        * [`LenovoTb321fuAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.models.LenovoTb321fuAdapter.video_settings)


## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.lenovo.adapter module
Lenovo ZUI camera and viewer defaults.

_class _ark.ark_mobile.mobile.android_adb.adapters.lenovo.adapter.LenovoAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_components _ = {'photo': 'com.zui.camera/.CameraActivity', 'video': 'com.zui.camera/.VideoCamera'}_


camera_flow_type

alias of [`LenovoCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.camera_flow.LenovoCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.lenovo.camera_flow.LenovoCameraFlow")

camera_package _ = 'com.zui.camera'_


camera_photo_id_tokens _ = ('shutter_button',)_


camera_record_start_id_tokens _ = ('shutter_button',)_


camera_record_stop_id_tokens _ = ('shutter_button',)_


file_load_components _ = {'audio': 'com.zui.gallery/.app.MovieActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.zui.gallery/.app.MovieActivity'}_


photo_mode_texts _ = ('拍照', 'Photo')_


video_mode_texts _ = ('视频', 'Video')_

## ark.ark_mobile.mobile.android_adb.adapters.lenovo.camera_flow module
Lenovo ZUI camera mode and video-quality behavior.

_class _ark.ark_mobile.mobile.android_adb.adapters.lenovo.camera_flow.LenovoCameraFlow(_session_ , _storage_service_ , _file_service_ , _ui_)

Bases: [`AndroidCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow")
## Module contents
Lenovo Android/ADB adaptation layer.

_class _ark.ark_mobile.mobile.android_adb.adapters.lenovo.LenovoAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_components _ = {'photo': 'com.zui.camera/.CameraActivity', 'video': 'com.zui.camera/.VideoCamera'}_


camera_flow_type

alias of [`LenovoCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.lenovo.md#ark.ark_mobile.mobile.android_adb.adapters.lenovo.camera_flow.LenovoCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.lenovo.camera_flow.LenovoCameraFlow")

camera_package _ = 'com.zui.camera'_


camera_photo_id_tokens _ = ('shutter_button',)_


camera_record_start_id_tokens _ = ('shutter_button',)_


camera_record_stop_id_tokens _ = ('shutter_button',)_


file_load_components _ = {'audio': 'com.zui.gallery/.app.MovieActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.zui.gallery/.app.MovieActivity'}_


photo_mode_texts _ = ('拍照', 'Photo')_


video_mode_texts _ = ('视频', 'Video')_
