---
title: "ark.ark_mobile.mobile.android_adb.adapters.honor.models package"
docname: "ark.ark_mobile.mobile.android_adb.adapters.honor.models"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.android_adb.adapters.honor.models.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.android_adb.adapters.honor.models package
## Submodules
## ark.ark_mobile.mobile.android_adb.adapters.honor.models.bkq_an10 module
HONOR BKQ-AN10 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.bkq_an10.HonorBkqAn10Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'honor-bkq-an10'_


video_settings _ = (('4K', 120),)_

## ark.ark_mobile.mobile.android_adb.adapters.honor.models.elp_an00 module
HONOR ELP-AN00 verified adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.elp_an00.HonorElpAn00Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

_classmethod _matches(_manufacturer : str_, _model : str_) → bool


name _ = 'honor-elp-an00'_


video_settings _ = (('4K', 60),)_


video_settings_combined_picker _ = True_


video_settings_reapply_on_record _ = True_


video_settings_requiring_hdr_off _ = (('4K', 60),)_

## ark.ark_mobile.mobile.android_adb.adapters.honor.models.ndl_w09 module
HONOR NDL-W09 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.ndl_w09.HonorNdlW09Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

file_paused_action_texts _ = ('播放',)_


file_playback_action_ids _ = ('btn_play_or_pause',)_


file_playing_action_texts _ = ('暂停',)_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'honor-ndl-w09'_


storage_mount_user_id _ = 0_


ui_dump_compressed _ = True_


ui_dump_root_in_active _ = True_


video_settings _ = (('1080P', 30),)_

## ark.ark_mobile.mobile.android_adb.adapters.honor.models.ptp_an00 module
HONOR PTP-AN00 adaptation profile.

_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.ptp_an00.HonorPtpAn00Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'honor-ptp-an00'_


video_setting_style _ = 'cycle'_


video_settings _ = (('4K', 60),)_

## Module contents
Explicitly registered HONOR model profiles.

_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.HonorBkqAn10Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'honor-bkq-an10'_


video_settings _ = (('4K', 120),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.HonorElpAn00Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

_classmethod _matches(_manufacturer : str_, _model : str_) → bool


name _ = 'honor-elp-an00'_


video_settings _ = (('4K', 60),)_


video_settings_combined_picker _ = True_


video_settings_reapply_on_record _ = True_


video_settings_requiring_hdr_off _ = (('4K', 60),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.HonorNdlW09Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

file_paused_action_texts _ = ('播放',)_


file_playback_action_ids _ = ('btn_play_or_pause',)_


file_playing_action_texts _ = ('暂停',)_


_classmethod _matches(_manufacturer_ , _model_)


name _ = 'honor-ndl-w09'_


storage_mount_user_id _ = 0_


ui_dump_compressed _ = True_


ui_dump_root_in_active _ = True_


video_settings _ = (('1080P', 30),)_


_class _ark.ark_mobile.mobile.android_adb.adapters.honor.models.HonorPtpAn00Adapter

Bases: [`HonorAdapter`](ark.ark_mobile.mobile.android_adb.adapters.honor.md#ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter "ark.ark_mobile.mobile.android_adb.adapters.honor.adapter.HonorAdapter")

_classmethod _matches(_manufacturer_ , _model_)


name _ = 'honor-ptp-an00'_


video_setting_style _ = 'cycle'_


video_settings _ = (('4K', 60),)_
