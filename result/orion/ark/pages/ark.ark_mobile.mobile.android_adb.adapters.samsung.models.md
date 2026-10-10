---
title: "ark.ark_mobile.mobile.android_adb.adapters.samsung.models package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.samsung.models"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.samsung.models.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.samsung.models package
## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_a156m module
Samsung Galaxy A15 (SM-A156M) adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_a156m.SamsungA15Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

camera_video_entry_dialog_cancel_id _ = 'android:id/button2'_


camera_video_entry_dialog_title_id _ = 'com.sec.android.app.camera:id/alertTitle'_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-a15-sm-a156m'_


video_settings _ = (('FHD', 30),)_


wake_before_screen_probe _ = True_

## ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_a5460 module
Samsung Galaxy A54 (SM-A5460) adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_a5460.SamsungA5460Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-a54-sm-a5460'_


video_settings _ = (('UHD', 30),)_

## ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_s9110 module
Samsung Galaxy S23 (SM-S9110) adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_s9110.SamsungS23Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-s23-sm-s9110'_


video_settings _ = (('8K', 30),)_

## ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_s921n module
Samsung Galaxy S24 (SM-S921N) verified adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_s921n.SamsungS24Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer : str_, _model : str_) → bool


name _ = 'samsung-s24-sm-s921n'_


video_settings _ = (('8K', 30),)_

## ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_s9310 module
Samsung Galaxy S25 (SM-S9310) verified adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_s9310.SamsungS25Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

camera_external_switch_texts _ = ('Save videos to external storage', 'Save videos to USB storage', '保存至外部存储', '保存视频到外部存储', '将视频保存到外部存储', '将视频保存至外部存储')_


camera_save_settings_button_id _ = 'com.sec.android.app.camera:id/quick_setting_button_main'_


camera_save_settings_entry_id _ = 'com.sec.android.app.camera:id/quick_setting_entry_button'_


camera_save_settings_texts _ = ('进入设置', '相机设置', 'Camera settings', 'Settings')_


camera_video_entry_dialog_cancel_id _ = 'android:id/button2'_


camera_video_entry_dialog_title_id _ = 'com.sec.android.app.camera:id/alertTitle'_


_classmethod _matches(_manufacturer : str_, _model : str_) → bool


name _ = 'samsung-s25-sm-s9310'_


recording_search_test_volumes _ = True_


supports_external_camera_target _ = True_


supports_reboot _ = True_


video_settings _ = (('8K', 30), ('UHD', 60), ('UHD', 30), ('FHD', 60), ('FHD', 30), ('HD', 30))_

## ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_x730 module
Samsung Galaxy Tab SM-X730 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.sm_x730.SamsungX730Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-sm-x730'_


video_settings _ = (('UHD', 30),)_

## Module contents
Explicitly registered Samsung model profiles.

_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.SamsungA15Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

camera_video_entry_dialog_cancel_id _ = 'android:id/button2'_


camera_video_entry_dialog_title_id _ = 'com.sec.android.app.camera:id/alertTitle'_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-a15-sm-a156m'_


video_settings _ = (('FHD', 30),)_


wake_before_screen_probe _ = True_


_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.SamsungA5460Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-a54-sm-a5460'_


video_settings _ = (('UHD', 30),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.SamsungS23Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-s23-sm-s9110'_


video_settings _ = (('8K', 30),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.SamsungS24Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer : str_, _model : str_) → bool


name _ = 'samsung-s24-sm-s921n'_


video_settings _ = (('8K', 30),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.SamsungS25Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

camera_external_switch_texts _ = ('Save videos to external storage', 'Save videos to USB storage', '保存至外部存储', '保存视频到外部存储', '将视频保存到外部存储', '将视频保存至外部存储')_


camera_save_settings_button_id _ = 'com.sec.android.app.camera:id/quick_setting_button_main'_


camera_save_settings_entry_id _ = 'com.sec.android.app.camera:id/quick_setting_entry_button'_


camera_save_settings_texts _ = ('进入设置', '相机设置', 'Camera settings', 'Settings')_


camera_video_entry_dialog_cancel_id _ = 'android:id/button2'_


camera_video_entry_dialog_title_id _ = 'com.sec.android.app.camera:id/alertTitle'_


_classmethod _matches(_manufacturer : str_, _model : str_) → bool


name _ = 'samsung-s25-sm-s9310'_


recording_search_test_volumes _ = True_


supports_external_camera_target _ = True_


supports_reboot _ = True_


video_settings _ = (('8K', 30), ('UHD', 60), ('UHD', 30), ('FHD', 60), ('FHD', 30), ('HD', 30))_


_class _ark.ark_mobile.mobile.android_adb.adapters.samsung.models.SamsungX730Adapter

Bases: [`SamsungAdapter`](ark.ark_mobile.mobile.android_adb.adapters.samsung.md#ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter "ark.ark_mobile.mobile.android_adb.adapters.samsung.adapter.SamsungAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'samsung-sm-x730'_


video_settings _ = (('UHD', 30),)_
