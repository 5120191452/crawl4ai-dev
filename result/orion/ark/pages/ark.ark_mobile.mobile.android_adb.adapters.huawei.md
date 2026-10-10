---
title: "ark.ark_mobile.mobile.android_adb.adapters.huawei package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.huawei"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.huawei.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.huawei package
## Subpackages
  * [ark.ark_mobile.mobile.android_adb.adapters.huawei.models package](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md)
    * [Submodules](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#submodules)
    * [ark.ark_mobile.mobile.android_adb.adapters.huawei.models.xyao_w00 module](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.huawei.models.xyao_w00)
      * [`HuaweiXyaoW00Adapter`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.xyao_w00.HuaweiXyaoW00Adapter)
        * [`HuaweiXyaoW00Adapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.xyao_w00.HuaweiXyaoW00Adapter.matches)
        * [`HuaweiXyaoW00Adapter.name`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.xyao_w00.HuaweiXyaoW00Adapter.name)
        * [`HuaweiXyaoW00Adapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.xyao_w00.HuaweiXyaoW00Adapter.video_settings)
    * [Module contents](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#module-ark.ark_mobile.mobile.android_adb.adapters.huawei.models)
      * [`HuaweiXyaoW00Adapter`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.HuaweiXyaoW00Adapter)
        * [`HuaweiXyaoW00Adapter.matches()`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.HuaweiXyaoW00Adapter.matches)
        * [`HuaweiXyaoW00Adapter.name`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.HuaweiXyaoW00Adapter.name)
        * [`HuaweiXyaoW00Adapter.video_settings`](ark.ark_mobile.mobile.android_adb.adapters.huawei.models.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.models.HuaweiXyaoW00Adapter.video_settings)


## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.huawei.adapter module
Huawei Android camera and native-viewer defaults.

_class _ark.ark_mobile.mobile.android_adb.adapters.huawei.adapter.HuaweiAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_actions _ = {'photo': 'android.intent.action.MAIN', 'video': 'android.media.action.VIDEO_CAMERA'}_


camera_categories _ = {'photo': 'android.intent.category.LAUNCHER'}_


camera_components _ = {'photo': 'com.huawei.camera/.controller.CameraActivity', 'video': 'com.huawei.camera/com.android.camera.VideoCamera'}_


camera_flow_type

alias of [`HuaweiCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.huawei.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.camera_flow.HuaweiCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.huawei.camera_flow.HuaweiCameraFlow")

camera_package _ = 'com.huawei.camera'_


camera_photo_keycode _ = 27_


camera_record_start_keycode _ = 27_


camera_record_stop_keycode _ = 27_


file_error_ids _ = ('first_text',)_


file_load_components _ = {'audio': 'com.huawei.music.local/com.huawei.music.ui.player.oneshot.MediaPlaybackActivityStarter', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.huawei.himovie.local/com.huawei.hwvplayer.service.player.FullscreenActivity'}_


file_playback_progress_ids _ = {'video': 'speed_bar'}_


file_playback_reveal_id _ = 'tplayer_screen'_


interruption_packages _ = ('com.huawei.camera',)_


lexar_post_launch_recovery _ = True_


photo_mode_texts _ = ('照片', '拍照', 'Photo')_


popup_handler_type

alias of [`HuaweiPopupHandler`](ark.ark_mobile.mobile.android_adb.adapters.huawei.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.popup_handler.HuaweiPopupHandler "ark.ark_mobile.mobile.android_adb.adapters.huawei.popup_handler.HuaweiPopupHandler")

video_mode_texts _ = ('视频', '录像', 'Video')_

## ark.ark_mobile.mobile.android_adb.adapters.huawei.camera_flow module
Huawei semantic resolution and frame-rate controls.

_class _ark.ark_mobile.mobile.android_adb.adapters.huawei.camera_flow.HuaweiCameraFlow(_session_ , _storage_service_ , _file_service_ , _ui_)

Bases: [`AndroidCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.camera_flow.AndroidCameraFlow")
## ark.ark_mobile.mobile.android_adb.adapters.huawei.popup_handler module
Huawei system-guide recovery.

_class _ark.ark_mobile.mobile.android_adb.adapters.huawei.popup_handler.HuaweiPopupHandler

Bases: [`AndroidPopupHandler`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.popup_handler.AndroidPopupHandler "ark.ark_mobile.mobile.android_adb.adapters.popup_handler.AndroidPopupHandler")

_classmethod _handle_special(_ui_ , _app_package_ , _nodes_ , _external_)

Return None when no brand-specific interruption was recognized.
## Module contents
Huawei Android/ADB adaptation layer.

_class _ark.ark_mobile.mobile.android_adb.adapters.huawei.HuaweiAdapter

Bases: [`AndroidGenericAdapter`](ark.ark_mobile.mobile.android_adb.adapters.md#ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter "ark.ark_mobile.mobile.android_adb.adapters.generic.AndroidGenericAdapter")

camera_actions _ = {'photo': 'android.intent.action.MAIN', 'video': 'android.media.action.VIDEO_CAMERA'}_


camera_categories _ = {'photo': 'android.intent.category.LAUNCHER'}_


camera_components _ = {'photo': 'com.huawei.camera/.controller.CameraActivity', 'video': 'com.huawei.camera/com.android.camera.VideoCamera'}_


camera_flow_type

alias of [`HuaweiCameraFlow`](ark.ark_mobile.mobile.android_adb.adapters.huawei.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.camera_flow.HuaweiCameraFlow "ark.ark_mobile.mobile.android_adb.adapters.huawei.camera_flow.HuaweiCameraFlow")

camera_package _ = 'com.huawei.camera'_


camera_photo_keycode _ = 27_


camera_record_start_keycode _ = 27_


camera_record_stop_keycode _ = 27_


file_error_ids _ = ('first_text',)_


file_load_components _ = {'audio': 'com.huawei.music.local/com.huawei.music.ui.player.oneshot.MediaPlaybackActivityStarter', 'text': 'com.android.htmlviewer/.HTMLViewerActivity', 'video': 'com.huawei.himovie.local/com.huawei.hwvplayer.service.player.FullscreenActivity'}_


file_playback_progress_ids _ = {'video': 'speed_bar'}_


file_playback_reveal_id _ = 'tplayer_screen'_


interruption_packages _ = ('com.huawei.camera',)_


lexar_post_launch_recovery _ = True_


photo_mode_texts _ = ('照片', '拍照', 'Photo')_


popup_handler_type

alias of [`HuaweiPopupHandler`](ark.ark_mobile.mobile.android_adb.adapters.huawei.md#ark.ark_mobile.mobile.android_adb.adapters.huawei.popup_handler.HuaweiPopupHandler "ark.ark_mobile.mobile.android_adb.adapters.huawei.popup_handler.HuaweiPopupHandler")

video_mode_texts _ = ('视频', '录像', 'Video')_
