---
title: "ark.ark_mobile.mobile.android_adb.adapters.tecno package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.tecno"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.tecno.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.tecno package
## Subpackages
  * [ark.ark_mobile.mobile.android_adb.adapters.tecno.models package](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md)
    * [Submodules](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#submodules)
    * [ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n module](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n)
      * [`TecnoCk9nAdapter`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n.TecnoCk9nAdapter)
        * [`TecnoCk9nAdapter.camera_record_start_keycode`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n.TecnoCk9nAdapter.camera_record_start_keycode)
        * [`TecnoCk9nAdapter.camera_record_stop_keycode`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n.TecnoCk9nAdapter.camera_record_stop_keycode)
        * [`TecnoCk9nAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n.TecnoCk9nAdapter.matches)
        * [`TecnoCk9nAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n.TecnoCk9nAdapter.name)
        * [`TecnoCk9nAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.ck9n.TecnoCk9nAdapter.video_settings)
    * [Module contents](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.tecno.models)
      * [`TecnoCk9nAdapter`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.TecnoCk9nAdapter)
        * [`TecnoCk9nAdapter.camera_record_start_keycode`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.TecnoCk9nAdapter.camera_record_start_keycode)
        * [`TecnoCk9nAdapter.camera_record_stop_keycode`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.TecnoCk9nAdapter.camera_record_stop_keycode)
        * [`TecnoCk9nAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.TecnoCk9nAdapter.matches)
        * [`TecnoCk9nAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.TecnoCk9nAdapter.name)
        * [`TecnoCk9nAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.tecno.models.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.models.TecnoCk9nAdapter.video_settings)


## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.tecno.adapter module
TECNO camera and viewer defaults.

_class _ark.ark_mobile.mobile.android_adb.adapters.tecno.adapter.TecnoAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_components _ = {'photo': 'com.transsion.camera/.app.CameraActivity', 'video': 'com.transsion.camera/.app.CameraActivity'}_


camera_flow_type

alias of [`TecnoCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.tecno.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.camera_flow.TecnoCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.tecno.camera_flow.TecnoCameraFlow")

camera_package _ = 'com.transsion.camera'_


camera_photo_id_tokens _ = ('shutter_button',)_


camera_photo_keycode _ = 27_


camera_record_start_id_tokens _ = ('shutter_button',)_


camera_record_stop_id_tokens _ = ('shutter_button',)_


file_load_components _ = {'audio': 'com.google.android.apps.nbu.files/.gateway.preview.PreviewActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.google.android.apps.nbu.files/.gateway.preview.PreviewActivity'}_


photo_mode_texts _ = ('AI CAM', '照片', 'Photo')_


video_mode_texts _ = ('视频', '录像', 'Video')_

## ark.ark_mobile.mobile.android_adb.adapters.tecno.camera_flow module
TECNO recording-quality popup.

_class _ark.ark_mobile.mobile.android_adb.adapters.tecno.camera_flow.TecnoCameraFlow(_session_ , _storage_service_ , _file_service_ , _ui_)

Bases: [`AndroidCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow")
## Module contents
TECNO Android adapter family.

_class _ark.ark_mobile.mobile.android_adb.adapters.tecno.TecnoAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_components _ = {'photo': 'com.transsion.camera/.app.CameraActivity', 'video': 'com.transsion.camera/.app.CameraActivity'}_


camera_flow_type

alias of [`TecnoCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.tecno.md#ark.ark_mobile.mobile.android_adb.adapters.tecno.camera_flow.TecnoCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.tecno.camera_flow.TecnoCameraFlow")

camera_package _ = 'com.transsion.camera'_


camera_photo_id_tokens _ = ('shutter_button',)_


camera_photo_keycode _ = 27_


camera_record_start_id_tokens _ = ('shutter_button',)_


camera_record_stop_id_tokens _ = ('shutter_button',)_


file_load_components _ = {'audio': 'com.google.android.apps.nbu.files/.gateway.preview.PreviewActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.google.android.apps.nbu.files/.gateway.preview.PreviewActivity'}_


photo_mode_texts _ = ('AI CAM', '照片', 'Photo')_


video_mode_texts _ = ('视频', '录像', 'Video')_
