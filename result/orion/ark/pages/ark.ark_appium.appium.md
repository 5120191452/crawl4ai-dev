---
title: "ark.ark_appium.appium package"
docname: "ark.ark_appium.appium"
source: "http://orion.longsys.com/ark.ark_appium.appium.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_appium.appium package
## Submodules
## ark.ark_appium.appium.ark_appium_factory module
@Project :Orion @File :ark_appium_factory.py @IDE :PyCharm @Author :xiaoze @Date :2024/11/01 10:42

_class _ark.ark_appium.appium.ark_appium_factory.ArkAppiumFactory(_* args_, _** kwargs_)

Bases: `object`

create_object()

## ark.ark_appium.appium.ark_appium_interface module
@Project ：OrionProject @File ：ark_appium_interface.py @IDE ：PyCharm @Author ：xiaoze @Date ：2024/10/14 09:40

_class _ark.ark_appium.appium.ark_appium_interface.ArkAppiumInterface

Bases: `ABC`

_abstract _click_element(_element : WebElement_)


Brief:

Click on the WebElement object.

Parameters:

**element** – WebElement Objects.

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _close()


Brief:

Release control app.

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _close_system_notifications()


Brief:

Close the pop-up window of the system, for example, when a prompt appears on the phone page asking whether to grant certain permissions to the XX application, you can directly close it through this interface.

Returns:

Return err_ok upon successful closure, error code upon failure closure.

_abstract _drag_and_drop(_origin_el : WebElement_, _destination_el : WebElement_)


Brief:

Drag an element to another element.

Parameters:

  * **origin_el** – The element to be dragged.
  * **destination_el** – The target element to drop to.


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _find_element(_way : [LocatorType](ark.ark_appium.appium.md#ark.ark_appium.appium.ark_appium_interface.LocatorType "ark.ark_appium.appium.ark_appium_interface.LocatorType")_, _path : str_, _retry_count : int_, _error_screenshot =False_)


Brief:

Find element on the app.

Parameters:

  * **way** – is an enumerated variable of LocatorType. LocatorType.ID = Find IDs in elements, For example “com.videogo:id/username_et” LocatorType.XPATH = Using xpath to find elements requires the developer to be familiar with the xpath syntax. LocatorType.TEXT = Using text to find UI elements. If text is used, then path only needs to be passed the text content, for example, to find the UI element whose local name is “Login”, then path=“Login”.
  * **path** – The path or identifier to find the elements.
  * **retry_count** – The number of attempts to search for the element if not immediately found.
  * **error_screenshot** – Automatically retain on-site screenshots of the phone when elements cannot be found.


Returns:

Returns the found element object if successful, otherwise returns False and logs an error.

_abstract _find_elements(_way : [LocatorType](ark.ark_appium.appium.md#ark.ark_appium.appium.ark_appium_interface.LocatorType "ark.ark_appium.appium.ark_appium_interface.LocatorType")_, _path : str_, _retry_count : int_, _error_screenshot =False_)


Brief:

Locate multiple elements on the app using the specified strategy.

Parameters:

  * **way** – is an enumerated variable of LocatorType. LocatorType.ID = Find IDs in elements, For example “com.videogo:id/username_et” LocatorType.XPATH = Using xpath to find elements requires the developer to be familiar with the xpath syntax LocatorType.TEXT = Using text to find UI elements. If text is used, then path only needs to be passed the text content, for example, to find the UI element whose local name is “Login”, then path=“Login”.
  * **path** – The path or identifier to find the elements.
  * **retry_count** – The number of attempts to search for the elements if not immediately found.
  * **error_screenshot** – Automatically retain on-site screenshots of the phone when elements cannot be found.


Returns:

Returns the err_ok error code and the WebElement’s object if it succeeds, and the error code and None if it fails.

_abstract _get_current_activity()


Brief:

Obtain the current activity name.

Returns:

Return the current activity name.

_abstract _get_element_center_coordinate(_element : WebElement_)


Brief:

Get the center coordinates of the WebElement object.

Parameters:

**element** – WebElement object.

Returns:

If successful, return the found center coordinates (tuple) and error code; otherwise, return the error code and record the error.

_abstract _get_page_source()


Brief:

Get the page structure of the current page, which is an HTML data.

Returns:

Return HTML data.

_abstract _get_text(_element : WebElement_)


Brief:

Get the text of the WebElement object.

Parameters:

**element** – WebElement object.

Returns:

If successful, return the object text and error code; otherwise, return the error code and record the error.

_abstract _hide_keyboard()


Brief:

Hide the keyboard that pops up on the page.

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _input_text(_element : WebElement_, _input_text : str_)


Brief:

Sending text values to WebElement objects.

Parameters:

  * **element** – The element where text in put is required.
  * **input_text** – The text string to input into the element.


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _monitor_app(_interval_time : int_)


Brief:

Start monitoring of the control app and force termination of all time-consuming operations on WebElement objects if the app is flashing.

Parameters:

**interval_time** – Interval of monitoring

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _open(_udid : str_, _package_name : list_)


Brief:

Open the controlled app.

Parameters:

  * **udid** – Device Unique Identification.
  * **package_name** – is a list of application names + page names.


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _press_and_hold_at_coordinate(_x : int_, _y : int_, _duration : int = 1000_)


Brief:

Long press on the page according to the coordinates to pause and then release the long press.

Parameters:

  * **x** – The x coordinate where the hold should occur.
  * **y** – The y coordinate where the hold should occur.
  * **duration** – The duration for which the press is held.


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _replacement_control(_udid : str_, _package_name : list_)


Brief:

Toggle control app.

Parameters:

  * **udid** – Device Unique Identification.
  * **package_name** – is a list of application names + page names.


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _screenshot()


Brief:

Screenshot, return byte data.

Returns:

Successfully returned err_ok+byte data, failed returned error code and None.

_abstract _scroll(_origin_el : WebElement_, _destination_el : WebElement_)


Brief:

Scrolling from one element to another.

Parameters:

  * **origin_el** – The element to start scrolling from.
  * **destination_el** – The element to scroll to.


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _start_service()


Brief:

Start the appium service, if appium is not installed in the environment, it will fail to start, if the service is already started in the environment, then the interface will not be started again.

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _stop_monitoring()


Brief:

After starting monitoring, you can stop monitoring by changing the interface.

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _stop_service()


Brief:

Stop the appium service started by start_service. If the appium service in your environment is not started by start_service, then changing the interface will not stop the appium service.

Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _swipe(_start_x : int_, _start_y : int_, _end_x : int_, _end_y : int_, _duration : int = 1000_)


Brief:

Slide on the page according to the coordinates.

Parameters:

  * **start_x** – The starting x coordinate of the swipe.
  * **start_y** – The starting y coordinate of the swipe.
  * **end_x** – The ending x coordinate of the swipe.
  * **end_y** – The ending y coordinate of the swipe.
  * **duration** – The time taken to perform the swipe action (optional).


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _tap(_x : int_, _y : int_, _count : int = 1_, _duration : int = 1000_)


Brief:

Click on the page according to the coordinates.

Parameters:

  * **x** – The x coordinate to tap.
  * **y** – The y coordinate to tap.
  * **count** – The number of times to tap (default is 1).
  * **duration** – Interval time


Returns:

Returns err_ok error code for success and other error codes for failure.

_abstract _zoom_element(_pinch_type : [PinchType](ark.ark_appium.appium.md#ark.ark_appium.appium.ark_appium_interface.PinchType "ark.ark_appium.appium.ark_appium_interface.PinchType")_, _element_ , _percent =0.75_)


Pinch_type:

PinchType.IN -> pinch-in (zoom-out, uses ‘mobile: pinchCloseGesture’) PinchType.OUT -> pinch-out (zoom-in, uses ‘mobile: pinchOpenGesture’)

Element:

The element already located by Appium.

Percent:

Strength of the pinch gesture in the range (0, 1]. The higher the value, the stronger the zoom-out. Default is 0.75.

Returns:

Error code. 0 means success, non-zero means failure.

_class _ark.ark_appium.appium.ark_appium_interface.LocatorType(_value_)

Bases: `Enum`
An enumeration.

ID _ = 'ID'_


TEXT _ = 'TEXT'_


XPATH _ = 'XPATH'_


_class _ark.ark_appium.appium.ark_appium_interface.PinchType(_value_)

Bases: `Enum`
An enumeration.

IN _ = 'mobile: pinchCloseGesture'_


OUT _ = 'mobile: pinchOpenGesture'_

## Module contents
