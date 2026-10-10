---
title: "ark.ark_mobile.mobile.android_adb.adapters.google package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.google"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.google.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.google package
## Subpackages
  * [ark.ark_mobile.mobile.android_adb.adapters.google.models package](ark.ark_mobile.mobile.android_adb.adapters.google.models.md)
    * [Submodules](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#submodules)
    * [ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_10_pro module](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_10_pro)
      * [`Pixel10ProAdapter`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_10_pro.Pixel10ProAdapter)
        * [`Pixel10ProAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_10_pro.Pixel10ProAdapter.matches)
        * [`Pixel10ProAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_10_pro.Pixel10ProAdapter.name)
        * [`Pixel10ProAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_10_pro.Pixel10ProAdapter.video_settings)
    * [ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_9_pro module](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_9_pro)
      * [`Pixel9ProAdapter`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_9_pro.Pixel9ProAdapter)
        * [`Pixel9ProAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_9_pro.Pixel9ProAdapter.matches)
        * [`Pixel9ProAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_9_pro.Pixel9ProAdapter.name)
        * [`Pixel9ProAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.pixel_9_pro.Pixel9ProAdapter.video_settings)
    * [Module contents](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.google.models)
      * [`Pixel10ProAdapter`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel10ProAdapter)
        * [`Pixel10ProAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel10ProAdapter.matches)
        * [`Pixel10ProAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel10ProAdapter.name)
        * [`Pixel10ProAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel10ProAdapter.video_settings)
      * [`Pixel9ProAdapter`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel9ProAdapter)
        * [`Pixel9ProAdapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel9ProAdapter.matches)
        * [`Pixel9ProAdapter.name`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel9ProAdapter.name)
        * [`Pixel9ProAdapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.google.models.md#ark.ark_mobile.mobile.android_adb.adapters.google.models.Pixel9ProAdapter.video_settings)


## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.google.adapter module
Google Camera and Files defaults.

_class _ark.ark_mobile.mobile.android_adb.adapters.google.adapter.GoogleAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_components _ = {'photo': 'com.google.android.GoogleCamera/com.android.camera.CameraImageActivity', 'video': 'com.google.android.GoogleCamera/com.android.camera.CameraVideoShortcutActivity'}_


camera_flow_type

alias of [`GoogleCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.google.md#ark.ark_mobile.mobile.android_adb.adapters.google.camera_flow.GoogleCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.google.camera_flow.GoogleCameraFlow")

camera_package _ = 'com.google.android.GoogleCamera'_


camera_photo_keycode _ = 27_


camera_record_start_keycode _ = 27_


camera_record_stop_keycode _ = 27_


file_load_components _ = {'audio': 'com.google.android.apps.youtube.music/.audiopreview.AudioPreviewPlayerActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.google.android.apps.photos/.pager.HostPhotoPagerActivity'}_


file_loader_type

alias of [`GoogleFileLoader`](ark.ark_mobile.mobile.android_adb.adapters.google.md#ark.ark_mobile.mobile.android_adb.adapters.google.file_loader.GoogleFileLoader "ark.ark_mobile.mobile.android_adb.adapters.google.file_loader.GoogleFileLoader")

file_resume_unknown_kinds _ = ('video',)_


photo_mode_texts _ = ('照片', 'Photo')_


popup_handler_type

alias of [`GooglePopupHandler`](ark.ark_mobile.mobile.android_adb.adapters.google.md#ark.ark_mobile.mobile.android_adb.adapters.google.popup_handler.GooglePopupHandler "ark.ark_mobile.mobile.android_adb.adapters.google.popup_handler.GooglePopupHandler")

video_mode_texts _ = ('视频', 'Video')_


video_settings_record_only _ = True_

## ark.ark_mobile.mobile.android_adb.adapters.google.camera_flow module
Google Camera recording-quality controls.

_class _ark.ark_mobile.mobile.android_adb.adapters.google.camera_flow.GoogleCameraFlow(_session_ , _storage_service_ , _file_service_ , _ui_)

Bases: [`AndroidCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow")
## ark.ark_mobile.mobile.android_adb.adapters.google.file_loader module
Google Photos playback evidence and control behavior.

_class _ark.ark_mobile.mobile.android_adb.adapters.google.file_loader.GoogleFileLoader(_session_ , _helper_ , _playback_ , _ui_)

Bases: [`AndroidFileLoader`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.file_loader.AndroidFileLoader "ark.ark_mobile.mobile.android_adb.adapters.file_loader.AndroidFileLoader")
Handle controls that Google Photos exposes without resource IDs.

MAX_EXTERNAL_VIDEO_ATTEMPTS _ = 4_


PAUSED_TEXTS _ = ('play', '播放')_


PLAYING_TEXTS _ = ('pause', '暂停')_


VIDEO_SURFACE_ID _ = 'com.google.android.apps.photos:id/photos_videoplayer_videolayout'_


load(_path_ , _absolute_ , _observation_duration_s_)

## ark.ark_mobile.mobile.android_adb.adapters.google.popup_handler module
Google Camera onboarding recovery.

_class _ark.ark_mobile.mobile.android_adb.adapters.google.popup_handler.GooglePopupHandler

Bases: [`AndroidPopupHandler`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.popup_handler.AndroidPopupHandler "ark.ark_mobile.mobile.android_adb.adapters.popup_handler.AndroidPopupHandler")

_classmethod _handle_special(_ui_ , _app_package_ , _nodes_ , _external_)

Return None when no brand-specific interruption was recognized.
## Module contents
Google Android adapter family.

_class _ark.ark_mobile.mobile.android_adb.adapters.google.GoogleAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_components _ = {'photo': 'com.google.android.GoogleCamera/com.android.camera.CameraImageActivity', 'video': 'com.google.android.GoogleCamera/com.android.camera.CameraVideoShortcutActivity'}_


camera_flow_type

alias of [`GoogleCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.google.md#ark.ark_mobile.mobile.android_adb.adapters.google.camera_flow.GoogleCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.google.camera_flow.GoogleCameraFlow")

camera_package _ = 'com.google.android.GoogleCamera'_


camera_photo_keycode _ = 27_


camera_record_start_keycode _ = 27_


camera_record_stop_keycode _ = 27_


file_load_components _ = {'audio': 'com.google.android.apps.youtube.music/.audiopreview.AudioPreviewPlayerActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.google.android.apps.photos/.pager.HostPhotoPagerActivity'}_


file_loader_type

alias of [`GoogleFileLoader`](ark.ark_mobile.mobile.android_adb.adapters.google.md#ark.ark_mobile.mobile.android_adb.adapters.google.file_loader.GoogleFileLoader "ark.ark_mobile.mobile.android_adb.adapters.google.file_loader.GoogleFileLoader")

file_resume_unknown_kinds _ = ('video',)_


photo_mode_texts _ = ('照片', 'Photo')_


popup_handler_type

alias of [`GooglePopupHandler`](ark.ark_mobile.mobile.android_adb.adapters.google.md#ark.ark_mobile.mobile.android_adb.adapters.google.popup_handler.GooglePopupHandler "ark.ark_mobile.mobile.android_adb.adapters.google.popup_handler.GooglePopupHandler")

video_mode_texts _ = ('视频', 'Video')_


video_settings_record_only _ = True_
