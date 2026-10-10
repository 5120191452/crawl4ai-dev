---
title: "ark.ark_camera.camera package"
docname: "ark.ark_camera.camera"
source: "http://orion.longsys.com/ark.ark_camera.camera.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_camera.camera package
## Submodules
## ark.ark_camera.camera.ark_camera_factory module

_class _ark.ark_camera.camera.ark_camera_factory.ArkCameraFactory(_* args_, _** kwargs_)

Bases: `object`
Responsible for controlling the camera device.

create_object(_camera_type =CameraType.CONSUMER_WIRED_)


Brief:

Initialising objects

Returns:

the corresponding object

_class _ark.ark_camera.camera.ark_camera_factory.CameraType(_value_)

Bases: `Enum`
Supported types are consumer_wired, consumer_wireless

CONSUMER_WIRED _ = 'consumer_wired'_


CONSUMER_WIRELESS _ = 'consumer_wireless'_

## ark.ark_camera.camera.ark_camera_interface module

_class _ark.ark_camera.camera.ark_camera_interface.ArkCameraInterface(_camnum =0_)

Bases: `ABC`
Abstract class that declares interfaces for the operation of camera.

_abstract _connect(_device_ , _connect_type =ConnectType.RemoteControl_)

@brief: Connect the selected camera device to the host. @param device: The camera connection target.
> For wired cameras, use the framework device ID. The device ID is composed of a brand prefix and the last two digits of the asset number: Canon: 10 + asset number’s last two digits. Fuji: 20 + asset number’s last two digits. Sony: 30 + asset number’s last two digits. Nikon: 40 + asset number’s last two digits. Lumix: 50 + asset number’s last two digits.
> Examples: Canon asset XX -> 10XX Fuji asset XX -> 20XX Sony asset XX -> 30XX Nikon asset XX -> 40XX Lumix asset XX -> 50XX
> For wireless cameras, use the camera IP address, e.g. “10.2.161.151”.
@param connect_type: (enum) Connection type for Sony cameras only. Other camera brands ignore this parameter. @return: Status: Success: returns 0. Failure: returns others.

_abstract _continuous_capture(_capture_count_)

@brief: Control the camera to take continuous photos and the number of continuous photos can be set. @param capture_count: (int) the number of continuous photos. @return: Status: Success: returns 0. Failure: returns others.

_abstract _copy_file(_src_path_ , _tar_path_ , _collect_performance =False_)

@brief: Copy the file from the source path to the target path on the PC. @param src_path: (str) The absolute source path of the file. @param tar_path: (str) The absolute target path of the file. @param collect_performance: (bool) Whether to collect file copy performance statistics. Default is False. @return: (status, performance_data). Status: Success returns 0; failure returns others.
> performance_data: Returns performance statistics when collect_performance is True; otherwise returns None.

_abstract _decrease_testing_flag()

@brief: Decrease the testing flag in the shared memory by one. @return: Status: Success: returns 0. Failure: returns others.

deinit()

@brief: Deinitial SDK program. @return: Status: Success: returns 0. Failure: returns others.

_abstract _delete_file(_file_path =None_, _opt_type =OperationType.Camera_)

@brief: Delete the specified file. @param file_path: (str) The enumerated file path. @param opt_type: (enum) The operation type, defaults to Camera.
> OperationType(Enum):
> Camera = “OperationType_Camera”
> Host = “OperationType_Host”
@return: Status: Success: returns 0. Failure: returns others.

_abstract _disconnect()

@brief: Disconnect the camera from the host computer for connection. @return: Status: Success: returns 0. Failure: returns others.

_abstract _download_file(_file_name_ , _dest_path_)

@brief: Transfer files from the Camera to the Host. @param file_name: The file path enumerated through the enum_files interface. @param dest_path: The destination path where the file is saved. @return: (Status, Save_path). Status: Success returns 0; failure returns a non-zero value. Save_path: The full path where the downloaded file is located.

_abstract _enum_files(_file_type =FileType.ALL_, _opt_type =OperationType.Camera_, _file_dir =None_)

@brief: Enumerate files of the specified type. @param file_type: (enum) The file type, defaults to ALL (Picture+Video).
> FileType(Enum):
> Picture = “FileType_Picture”
> Video = “FileType_Video”
> ALL = “FileType_Picture_Video”
@param opt_type: (enum) The operation type, defaults to Camera.
> OperationType(Enum):
> Camera = “OperationType_Camera”
> Host = “OperationType_Host”

@param file_dir: (str, optional) The host directory to search when opt_type is Host. The directory is searched recursively.

This parameter is required for Host operations and is ignored for Camera operations.

@return: A tuple of (status, file_paths).

status: Success returns 0; failure returns a non-zero value. file_paths: A list of full file paths matching file_type.
> The list is empty when no matching files exist.

_abstract _format(_opt_type =OperationType.Camera_)

@brief: Format the imager disk using the camera or host. @param opt_type: (enum) The operation type, defaults to Camera.
> OperationType(Enum):
>> Camera = “OperationType_Camera”
>> Host = “OperationType_Host”
> Note: Host-side formatting is currently not supported.
@return: Status: Success: returns 0. Failure: returns others.

_abstract _get_device_name()

@brief: Get the names of the physically connected devices. @return: (Status, Device_name). Status: Success returns 0; failure returns a non-zero value. Device_name: list; the names of the physically connected devices.

_abstract _get_file_num(_file_type_ , _opt_type =OperationType.Camera_, _file_dir =None_)

@brief: Get the number of files of the specified file type. @param file_type: (enum) The file type, defaults to ALL (Picture+Video).
> FileType(Enum):
> Picture = “FileType_Picture”
> Video = “FileType_Video”
> ALL = “FileType_Picture_Video”
@param opt_type: (enum) The operation type, defaults to Camera.
> OperationType(Enum):
> Camera = “OperationType_Camera”
> Host = “OperationType_Host”

@return:

Status: Success: returns 0. Failure: returns others.
file_num: (int) the number of files.

_abstract _increase_testing_flag()

@brief: Increase the testing flag in the shared memory by one. @return: Status: Success: returns 0. Failure: returns others.

_abstract _init(_device_)

@brief: Initial SDK program. @return: Status: Success: returns 0. Failure: returns others.

_abstract _notice_switch_camera_mode(_secret_ , _robot_url_)

@brief: Notify users via DingTalk bot to switch the camera to video mode. @param secret: (string) The DingTalk robot’s secret key can be obtained from the robot’s settings page. @param robot_url: (string) The communication address of the DingTalk robot (Webhook URL), can be obtained from the robot’s settings page. @return: Status: Success: returns 0. Failure: returns others.

_abstract _quality_check(_file_path_)

@brief: Check the quality of the specified picture or video. @param file_path: (str) The absolute path of the file, that is, the file path saved on the host. @return: Status: Success: returns 0. Failure: returns others.

_abstract _scanning_device_loop()

@brief: Loop through (or continuously scan) the currently connected camera device IDs and update them in the XML file. @return: Status: Success: returns 0. Failure: returns others.

_abstract _set_device_name(_device_name_)

@brief: Set the name for the connected camera devices. Just only Support the Cannon. @param device_name(int): The name set for the connected camera device. @return: Status: Success: returns 0. Failure: returns others.

_abstract _set_picture_type(_picture_type =PictureType.ALL_)

@brief: Set the type for saving pictures taken. @param picture_type: (enum) The picture type, defaults to ALL(RAW+JPEG).
> PictureType(Enum):
> JPEG = “PictureType_JPEG”
> RAW = “PictureType_RAW”
> ALL = “PictureType_RAW_JPEG”
@return: Status: Success: returns 0. Failure: returns others.

_abstract _set_save_path(_save_path_)

@brief: Set the path for saving the captured pictures. only support Sony Camera for now. @param save_path: (str) The absolute path of the directory where the captured pictures are saved on the host. @return: Status: Success: returns 0. Failure: returns others.

_abstract _set_video_config(_video_format_ , _video_fps =None_, _video_quality =None_)

@brief: Set the video recording format, frame rate, and quality. @param video_format: (enum/int) The video format value. The supported values depend on the camera model and its current capabilities. @param video_fps: (enum/int, optional) The requested frame rate. Use None to keep the current frame rate. @param video_quality: (enum/int, optional) The requested video quality or recording setting. Use None to keep the current quality. @return: Status: Success: returns 0. Failure: returns others.

_abstract _single_capture()

@brief: Control the camera to take a single photo. @return: Status: Success: returns 0. Failure: returns others.

_abstract _sleep_wake(_sleep_time_)

@brief: (not yet implemented) @param sleep_time: (int) Sleeping time. The unit is seconds. @return: Status: Success: returns 0. Failure: returns others.

_abstract _video_start()

@brief: Control the camera to start recording videos. @return: Status: Success: returns 0. Failure: returns others.

_abstract _video_status_check()

@brief: Check the video status. @return: Status: Success: returns 0. Failure: returns others.

_abstract _video_stop()

@brief: Control the camera to stop recording videos. @return: Status: Success: returns 0. Failure: returns others.

_class _ark.ark_camera.camera.ark_camera_interface.CameraBrand(_value_)

Bases: `Enum`
An enumeration.

Canon _ = 1000_


Fuji _ = 2000_


Lumix _ = 5000_


Nikon _ = 4000_


Sony _ = 3000_


_class _ark.ark_camera.camera.ark_camera_interface.ConnectType(_value_)

Bases: `Enum`
An enumeration.

ContentTransfer _ = 1_


RemoteControl _ = 0_


RemoteTransfer _ = 2_


_class _ark.ark_camera.camera.ark_camera_interface.FileType(_value_)

Bases: `Enum`
An enumeration.

ALL _ = 'picture+video'_


Picture _ = 'picture'_


Video _ = 'video'_


_class _ark.ark_camera.camera.ark_camera_interface.OperationType(_value_)

Bases: `Enum`
An enumeration.

Camera _ = 'OperationType_Camera'_


Host _ = 'OperationType_Host'_


_class _ark.ark_camera.camera.ark_camera_interface.PictureType(_value_)

Bases: `Enum`
An enumeration.

ALL _ = 3_


JPEG _ = 2_


RAW _ = 1_


_class _ark.ark_camera.camera.ark_camera_interface.VideoEncodingQuality(_value_)

Bases: `IntEnum`
An enumeration.

BLACKMAGIC_BRAW_12_1 _ = 300_


BLACKMAGIC_BRAW_3_1 _ = 302_


BLACKMAGIC_BRAW_5_1 _ = 303_


BLACKMAGIC_BRAW_8_1 _ = 301_


BLACKMAGIC_BRAW_Q0 _ = 304_


BLACKMAGIC_BRAW_Q1 _ = 305_


BLACKMAGIC_BRAW_Q3 _ = 306_


BLACKMAGIC_BRAW_Q5 _ = 307_


LUMIX_REC_MODE_AVCHD _ = 0_


LUMIX_REC_MODE_MAX _ = 6_


LUMIX_REC_MODE_MJPEG _ = 1_


LUMIX_REC_MODE_MOV _ = 3_


LUMIX_REC_MODE_MP4 _ = 2_


LUMIX_REC_MODE_MP4_HEVC _ = 5_


LUMIX_REC_MODE_MP4_LPCM _ = 4_


NIKON_H264_8BIT_MP4 _ = 2_


NIKON_H265_10BIT_MOV _ = 4_


NIKON_H265_8BIT_MOV _ = 3_


NIKON_NRAW_12BIT_NEV _ = 7_


NIKON_PRORES_422_HQ_10BIT_MOV _ = 5_


NIKON_PRORES_RAW_HQ_12BIT_MOV _ = 6_


NIKON_R3D_HE _ = 8_


SONY_150M_420_10BIT _ = 50_


SONY_150M_420_8BIT _ = 51_


SONY_16M_420_8BIT _ = 67_


SONY_185M_422_10BIT _ = 49_


SONY_200M_420_10BIT _ = 47_


SONY_200M_420_8BIT _ = 48_


SONY_200M_422_10BIT _ = 46_


SONY_250M_422_10BIT _ = 43_


SONY_25M_420_8BIT _ = 66_


SONY_260M_422_10BIT _ = 69_


SONY_280M_422_10BIT _ = 42_


SONY_400M_420_10BIT _ = 40_


SONY_500M_422_10BIT _ = 39_


SONY_50M_420_10BIT _ = 62_


SONY_50M_420_8BIT _ = 63_


SONY_50M_422_10BIT _ = 61_


SONY_520M_422_10BIT _ = 68_


SONY_93M_422_10BIT _ = 57_


_class _ark.ark_camera.camera.ark_camera_interface.VideoFormat(_value_)

Bases: `IntEnum`
设置视频画质尺寸前，请确认当前存储卡支持所设置的视频格式

BLACKMAGIC_1920X1080 _ = 100_


BLACKMAGIC_2112X1184 _ = 101_


BLACKMAGIC_4096X2160 _ = 102_


BLACKMAGIC_4096X2304 _ = 103_


BLACKMAGIC_4096X3072 _ = 104_


BLACKMAGIC_4832X4032 _ = 105_


BLACKMAGIC_6048X2520 _ = 106_


BLACKMAGIC_6048X3200 _ = 107_


BLACKMAGIC_6048X3408 _ = 108_


BLACKMAGIC_6048X4032 _ = 109_


CANON_2K_D_100P_LGOP _ = 8796100453424_


CANON_2K_D_150P_LGOP _ = 10995123721776_


CANON_2K_D_24P_LGOP _ = 3298542295088_


CANON_2K_D_25P_LGOP _ = 4398053923120_


CANON_2K_D_50P_LGOP _ = 6597077185072_


CANON_4K_D_100P_LGOP _ = 8796096259120_


CANON_4K_D_24P_LGOP _ = 3298538100784_


CANON_4K_D_25P_LGOP _ = 4398049728816_


CANON_4K_D_50P_LGOP _ = 6597072990768_


CANON_4K_D_FINE_24P_LGOP _ = 3367257577520_


CANON_4K_D_FINE_25P_LGOP _ = 4466769205552_


CANON_4K_D_FINE_50P_LGOP _ = 6665792467504_


CANON_4K_U_100P_LGOP _ = 8796098356272_


CANON_4K_U_25P_LGOP _ = 4398051825968_


CANON_4K_U_50P_LGOP _ = 6597075087920_


CANON_4K_U_FINE_25P_LGOP _ = 4466771302704_


CANON_4K_U_FINE_50P_LGOP _ = 6665794564656_


CANON_FHD_100P_LGOP _ = 8796093113392_


CANON_FHD_150P_LGOP _ = 10995116381744_


CANON_FHD_25P_LGOP _ = 4398046583088_


CANON_FHD_50P_LGOP _ = 6597069845040_


CANON_RAW_24P_RAW _ = 3298545571952_


CANON_RAW_24P_RAWL _ = 3298545571953_


CANON_RAW_25P_RAW _ = 4398057199984_


CANON_RAW_25P_RAWL _ = 4398057199985_


CANON_RAW_50P_RAWL _ = 6597080461937_


LUMIX_AVCHD_FHD_24P_24M _ = 4_


LUMIX_AVCHD_FHD_25P_24M _ = 27_


LUMIX_AVCHD_FHD_50P_28M _ = 0_


LUMIX_AVCHD_FHD_50i_17M _ = 1_


LUMIX_MOV_4K_24P_420_10L _ = 501_


LUMIX_MOV_4K_24P_422_10I _ = 231_


LUMIX_MOV_4K_24P_422_10L _ = 230_


LUMIX_MOV_4K_30P_420_10L _ = 500_


LUMIX_MOV_4K_30P_422_10I _ = 229_


LUMIX_MOV_4K_30P_422_10L _ = 228_


LUMIX_MOV_4K_48P_420_10L _ = 408_


LUMIX_MOV_4K_48P_422_10I_H _ = 497_


LUMIX_MOV_4K_48P_422_10I_L _ = 498_


LUMIX_MOV_4K_48P_422_10L _ = 499_


LUMIX_MOV_4K_60P_420_10_L _ = 406_


LUMIX_MOV_4K_60P_422_10I_H _ = 494_


LUMIX_MOV_4K_60P_422_10I_L _ = 495_


LUMIX_MOV_4K_60P_422_10L _ = 496_


LUMIX_MOV_5K_24P_200M _ = 655_


LUMIX_MOV_5K_25P_200M _ = 654_


LUMIX_MOV_5K_30P_200M _ = 653_


LUMIX_MOV_C4K_24P_420_10L _ = 491_


LUMIX_MOV_C4K_24P_422_10I _ = 224_


LUMIX_MOV_C4K_24P_422_10L _ = 222_


LUMIX_MOV_C4K_30P_420_10L _ = 490_


LUMIX_MOV_C4K_30P_422_10I _ = 378_


LUMIX_MOV_C4K_30P_422_10L _ = 381_


LUMIX_MOV_C4K_48P_420_10L _ = 404_


LUMIX_MOV_C4K_48P_422_10I_H _ = 487_


LUMIX_MOV_C4K_48P_422_10I_L _ = 488_


LUMIX_MOV_C4K_48P_422_10L _ = 489_


LUMIX_MOV_C4K_60P_420_10L _ = 402_


LUMIX_MOV_C4K_60P_422_10I_H _ = 484_


LUMIX_MOV_C4K_60P_422_10I_L _ = 485_


LUMIX_MOV_C4K_60P_422_10L _ = 486_


LUMIX_MOV_FHD_24P_420_10L _ = 515_


LUMIX_MOV_FHD_24P_422_10I _ = 249_


LUMIX_MOV_FHD_24P_422_10L _ = 250_


LUMIX_MOV_FHD_30P_420_10L _ = 514_


LUMIX_MOV_FHD_30P_422_10I _ = 247_


LUMIX_MOV_FHD_30P_422_10L _ = 248_


LUMIX_MOV_FHD_48P_420_10L _ = 420_


LUMIX_MOV_FHD_48P_422_10I _ = 512_


LUMIX_MOV_FHD_48P_422_10L _ = 513_


LUMIX_MOV_FHD_60I_422_10I _ = 414_


LUMIX_MOV_FHD_60I_422_10L _ = 415_


LUMIX_MOV_FHD_60P_420_10L _ = 511_


LUMIX_MOV_FHD_60P_422_10I _ = 245_


LUMIX_MOV_FHD_60P_422_10L _ = 246_


LUMIX_MP4_4K_24P_100M_8bit _ = 179_


LUMIX_MP4_4K_24P_72M_10bit _ = 367_


LUMIX_MP4_4K_30P_100M_8bit _ = 177_


LUMIX_MP4_4K_30P_72M_10bit _ = 366_


LUMIX_MP4_4K_60P_100M_10bit _ = 430_


LUMIX_MP4_FHD_24P_24M_8bit _ = 180_


LUMIX_MP4_FHD_25P_20M _ = 21_


LUMIX_MP4_FHD_30P_20M _ = 20_


LUMIX_MP4_FHD_30P_20M_8bit _ = 20_


LUMIX_MP4_FHD_50P_28M _ = 19_


LUMIX_MP4_FHD_60P_28M _ = 18_


LUMIX_MP4_FHD_60P_28M_8bit _ = 18_


LUMIX_MP4_QFHD_4K_24P_100M _ = 179_


LUMIX_MP4_QFHD_4K_25P_100M _ = 178_


LUMIX_MP4_QFHD_4K_30P_100M _ = 177_


LUMIX_MP4_QFHD_4K_50P_LPCM_150M _ = 386_


LUMIX_MP4_QFHD_4K_60P_LPCM_150M _ = 187_


NIKON_1920X1080_100P _ = 19_


NIKON_1920X1080_120P _ = 18_


NIKON_1920X1080_200P _ = 75_


NIKON_1920X1080_240P _ = 74_


NIKON_1920X1080_24P _ = 7_


NIKON_1920X1080_24P_X5_SLOW _ = 17_


NIKON_1920X1080_25P _ = 6_


NIKON_1920X1080_25P_X4_SLOW _ = 16_


NIKON_1920X1080_30P _ = 5_


NIKON_1920X1080_30P_X4_SLOW _ = 15_


NIKON_1920X1080_50P _ = 4_


NIKON_1920X1080_60P _ = 3_


NIKON_3840X2160_100P _ = 51_


NIKON_3840X2160_120P _ = 50_


NIKON_3840X2160_24P _ = 2_


NIKON_3840X2160_25P _ = 1_


NIKON_3840X2160_30P _ = 0_


NIKON_3840X2160_50P _ = 23_


NIKON_3840X2160_60P _ = 22_


NIKON_3984X2240_100P _ = 63_


NIKON_3984X2240_120P _ = 62_


NIKON_3984X2240_24P _ = 68_


NIKON_3984X2240_25P _ = 67_


NIKON_3984X2240_30P _ = 66_


NIKON_3984X2240_50P _ = 65_


NIKON_3984X2240_60P _ = 64_


NIKON_4030X2268_24P _ = 61_


NIKON_4030X2268_25P _ = 60_


NIKON_4030X2268_30P _ = 59_


NIKON_4030X2268_50P _ = 58_


NIKON_4030X2268_60P _ = 57_


NIKON_5376X3024_24P _ = 73_


NIKON_5376X3024_25P _ = 72_


NIKON_5376X3024_30P _ = 71_


NIKON_5376X3024_50P _ = 70_


NIKON_5376X3024_60P _ = 69_


NIKON_6048X3402_24P _ = 56_


NIKON_6048X3402_25P _ = 55_


NIKON_6048X3402_30P _ = 54_


NIKON_6048X3402_50P _ = 53_


NIKON_6048X3402_60P _ = 52_


SONY_AVCHD _ = 0_


SONY_XAVC_HS_4K _ = 5_


SONY_XAVC_HS_8K _ = 4_


SONY_XAVC_S_4K _ = 2_


SONY_XAVC_S_HD _ = 3_


SONY_XAVC_S_I_4K _ = 8_


SONY_XAVC_S_I_HD _ = 9_


_class _ark.ark_camera.camera.ark_camera_interface.VideoFrameRate(_value_)

Bases: `IntEnum`
An enumeration.

BLACKMAGIC_23_98P _ = 200_


BLACKMAGIC_24P _ = 201_


BLACKMAGIC_25P _ = 202_


BLACKMAGIC_29_97P _ = 203_


BLACKMAGIC_30P _ = 204_


BLACKMAGIC_50P _ = 205_


BLACKMAGIC_59_94P _ = 206_


BLACKMAGIC_60P _ = 207_


SONY_100P _ = 2_


SONY_120P _ = 1_


SONY_24P _ = 7_


SONY_25P _ = 6_


SONY_30P _ = 5_


SONY_50P _ = 4_


SONY_60P _ = 3_

## Module contents
@Module : ark_camera
@Date : 2024/12/05
@Version : V1.0.0
The camera module is used to control camera devices to execute instructions such as formatting, taking pictures, and recording videos, so as to provide support for the automated testing of cameras.
