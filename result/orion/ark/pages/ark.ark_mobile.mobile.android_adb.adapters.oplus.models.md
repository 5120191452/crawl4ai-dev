---
title: "ark.ark_mobile.mobile.android_adb.adapters.oplus.models package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.oplus.models"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.oplus.models.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.oplus.models package
## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.oplus.models.opd2506 module
OPPO OPD2506 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.opd2506.OppoOpd2506Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_load_components _ = {'audio': 'com.heytap.music/com.allsaints.music.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oppo-opd2506'_


video_settings _ = (('4K', 30),)_

## ark.ark_mobile.mobile.android_adb.adapters.oplus.models.phz110 module
OPPO PHZ110 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.phz110.OppoPhz110Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_background_playback_kinds _ = ('audio',)_


file_load_components _ = {'audio': 'com.heytap.music/com.allsaints.music.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oppo-phz110'_


video_settings _ = (('4K', 60),)_

## ark.ark_mobile.mobile.android_adb.adapters.oplus.models.plg110 module
OPPO PLG110 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.plg110.OppoPlg110Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_load_components _ = {'audio': 'com.coloros.video/com.oplus.music.ui.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oppo-plg110'_


video_settings _ = (('4K', 120),)_

## ark.ark_mobile.mobile.android_adb.adapters.oplus.models.plk110 module
OnePlus PLK110 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.plk110.OnePlusPlk110Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_load_components _ = {'audio': 'com.coloros.video/com.oplus.music.ui.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oneplus-plk110'_


video_settings _ = (('8K', 30),)_

## ark.ark_mobile.mobile.android_adb.adapters.oplus.models.rmp2108 module
realme RMP2108 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.rmp2108.RealmeRmp2108Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.CameraImageActivity', 'video': 'com.oplus.camera/.VideoCamera'}_


camera_photo_mode_swipe _ = (0.5, 0.53, 0.5, 0.47)_


file_load_components _ = {'audio': 'com.heytap.music/com.allsaints.music.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.MoviePlayerActivity'}_


file_resume_unknown_kinds _ = ('audio',)_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'realme-rmp2108'_


video_setting_style _ = 'cycle'_


video_settings _ = (('1080P', 30),)_

## Module contents
Explicitly registered OPlus-platform model profiles.

_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.OnePlusPlk110Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_load_components _ = {'audio': 'com.coloros.video/com.oplus.music.ui.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oneplus-plk110'_


video_settings _ = (('8K', 30),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.OppoOpd2506Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_load_components _ = {'audio': 'com.heytap.music/com.allsaints.music.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oppo-opd2506'_


video_settings _ = (('4K', 30),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.OppoPhz110Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_background_playback_kinds _ = ('audio',)_


file_load_components _ = {'audio': 'com.heytap.music/com.allsaints.music.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oppo-phz110'_


video_settings _ = (('4K', 60),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.OppoPlg110Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.component.CameraImageActivity', 'video': 'com.oplus.camera/.component.VideoCameraActivity'}_


file_load_components _ = {'audio': 'com.coloros.video/com.oplus.music.ui.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.LocalVideoPlayActivity'}_


file_uri_modes _ = {'audio': 'media_store'}_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'oppo-plg110'_


video_settings _ = (('4K', 120),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.oplus.models.RealmeRmp2108Adapter

Bases: [`OplusAdapter`](ark.ark_mobile.mobile.android_adb.adapters.oplus.md#ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter "ark.ark_mobile.mobile.android_adb.adapters.oplus.adapter.OplusAdapter")

camera_components _ = {'photo': 'com.oplus.camera/.CameraImageActivity', 'video': 'com.oplus.camera/.VideoCamera'}_


camera_photo_mode_swipe _ = (0.5, 0.53, 0.5, 0.47)_


file_load_components _ = {'audio': 'com.heytap.music/com.allsaints.music.MainActivity', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.coloros.video/com.oplus.video.ui.MoviePlayerActivity'}_


file_resume_unknown_kinds _ = ('audio',)_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'realme-rmp2108'_


video_setting_style _ = 'cycle'_


video_settings _ = (('1080P', 30),)_
