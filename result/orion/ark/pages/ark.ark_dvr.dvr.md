---
title: "ark.ark_dvr.dvr package"
docname: "ark.ark_dvr.dvr"
source: "http://orion.longsys.com/ark.ark_dvr.dvr.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_dvr.dvr package
## Submodules
## ark.ark_dvr.dvr.ark_dvr_factory module
## ark.ark_dvr.dvr.ark_dvr_interface module
@Project ：OrionProject @File ：ark_appium_interface.py @IDE ：PyCharm @Author ：xiaoze @Date ：2025/04/08 09:40

_class _ark.ark_dvr.dvr.ark_dvr_interface.ArkDvrInterface

Bases: `ABC`

_abstract _connect_dvr_db()


Brief:

Connect to a database.

Returns:

Successful connection returns err_ok+None, failed connection returns error code+reason for error.

_abstract _disconnect_dvr_db()


Brief:

Close the currently connected database.

Returns:

Successful closure returns err_ok+None, failure closure returns error code+error reason.

_abstract _get_cap()


Brief:

Get the cap object, which is a camera object that can be used to obtain real-time images, etc. This camera object comes from the VideCapture class in the cv2 library, which has many methods that can be called,Such as open/isOpened/release/grub, etc.Can be found in the __init__ of cv2 again

Returns:

Successfully returned err_ok+object, failed returned error code+None.

_abstract _init_error_data()


Brief:

Initialization error data source.

Returns:

success returns err_ok, failure returns error code.

_abstract _init_rebot_notification()


Brief:

Read the DingTalk robot configuration from the configuration file.

Returns:

err_ok for Successful, error code for failure.

_abstract _matching(_error_texts_ , _threshold =0.7_)


Brief:

Error text comparison, calculating the degree of match between the current text and the text in the error list.

Param:

error_texts： The incorrect text to be compared.

Param:

threshold： Matching threshold, the higher the threshold, the higher the matching requirements, default is 0.7.

Returns:

Successfully returns err_ok+matching situation (dictionary), which can be approximate match/perfect match/mismatch. Failed to return error code+None.

_abstract _open_camera(_camera_index_)


Brief:

Used to open a specified camera.

Param:

camera_index: The index l of the camera is an integer that can be found in the device manager.

Returns:

Successful returns err_ok, failure returns error code

_abstract _robot_send_message(_text_)


Brief:

Send a message to the DingTalk robot.

Param:

text： text: is a string type, error notification, must contain keywords such as “dvr”/”matches”, otherwise the alarm cannot be sent.

Returns:

success returns err_ok, failure returns error code.

_abstract _set_camera_parameter(_resolution =None_, _luminance =30_, _brightness =0_, _contrast_ratio =1_, _saturation =64_, _chroma =0_, _gain =-1_, _exposure =-4_)


Brief:

Adjust the parameters of the opened camera. The default parameters are only defined for the “LeXi 2K autofocus camera”.

Param:

resolution: The resolution list must be an integer list, with a default value of 480 * 360, defined based on the current DVR scene.

Param:

luminance: Set the target frame rate, the default value is 30. Here, we only expect its target frame rate to be 30. If it is due to insufficient performance or other reasons, it may not be possible to achieve its expected value.

Param:

brightness: Set the brightness to ‘0’ by default. Generally, camera devices come with pre installed brightness at the factory, so the default brightness is not increased for the device.

Param:

contrast_ratio: Set the contrast, with a default alue of 1, based on the camera used in the current DVR scene.

Param:

saturation: Set saturation, default value is 64, based on the default value of the camera used in the current DVR scene.

Param:

chroma: Set the chromaticity, the default value is 0. Generally, camera devices have calibrated chromaticity at the factory, so the chromaticity is not adjusted by default.

Param:

gain: Set the gain value, the default value is -1, -1 indicates non automatic gain, and the specific value usually depends on the camera. In DVR scenarios, camera -1 indicates non automatic gain.

Param:

exposure: Set the exposure value, the default value is -4, -4 indicates automatic exposure, and the specific value usually depends on the camera. In the DVR scene, camera -4 indicates automatic exposure.

Returns:

Error code returned for Successful and error code returned for failure.
## Module contents
