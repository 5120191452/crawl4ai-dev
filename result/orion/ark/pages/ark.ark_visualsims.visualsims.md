---
title: "ark.ark_visualsims.visualsims package"
docname: "ark.ark_visualsims.visualsims"
source: "http://orion.longsys.com/ark.ark_visualsims.visualsims.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_visualsims.visualsims package
## Submodules
## ark.ark_visualsims.visualsims.ark_visualsims_factory module

_class _ark.ark_visualsims.visualsims.ark_visualsims_factory.ArkVisualsimsFactory(_* args_, _** kwargs_)

Bases: `object`

create_object(_is_update =False_, _ocr_model =OcrModel.Standard_, _use_angle_cls =False_, _use_gpu =False_, _screen_resolution =None_)


Brief:

Creates and returns a VisualSims object.

Parameters:

  * **is_update** – bool. If False (default), download models only when the local model directory is missing. If True, always download the latest models from the Orion server and overwrite existing local models.
  * **ocr_model** – OcrModel. OCR model type to use. Available options (in order of capability): Light: Fast, lightweight, lower accuracy. Not support angle classification (use_angle_cls) or GPU acceleration (use_gpu). Standard: Balanced speed and accuracy (recommended default). Enhanced: Better accuracy and stability than Standard (not yet implemented). Premium: Highest accuracy and robustness (licensed/paid, not yet implemented).
  * **use_angle_cls** – bool. Whether to enable angle classification during OCR processing.
  * **use_gpu** – bool. Whether to utilize GPU acceleration for model inference.
  * **screen_resolution** – Optional[Tuple[int, int]]. Test device screen resolution as `(width, height)` (e.g. `(1920, 1080)`). It assists in performing keyboard-mouse simulator (KMS) operations. Set to None if no test device is used.


Returns:

An instance of the corresponding VisualSims class.
## ark.ark_visualsims.visualsims.ark_visualsims_interface module

_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.ArkVisualSimsInterface

Bases: `ABC`
Abstract class that declares an interface for the visualsims component.

_abstract _absolute_move(_coord_ , _run_time =5000_, _step_max =80_)


Brief:

Move the mouse cursor to the specified absolute coordinates.

Parameters:

  * **coord** – List[float], Target position on the screen in [x, y] format. - x: float, X-coordinate relative to the top-left corner of the image (unit: pixels). - y: float, Y-coordinate relative to the top-left corner of the image (unit: pixels).
  * **run_time** – int, Total time for cursor movement in milliseconds (ms). The function will fail if the movement exceeds this time limit.
  * **step_max** – int, Maximum displacement per step (unit: pixels).


Returns:

Error code (int): 0 indicates success; non-zero indicates failure. Coordinates (List[float]): Final cursor position [x, y] after movement. Returns None on failure.

_abstract _barcode(_img =None_)


Brief:

Perform barcode detection and decoding on the input image.
If no image is provided, one frame will be captured automatically from the connected device via `get_frames()`.

Parameters:

**img** – Optional[Union[str, bytes, np.ndarray]]. Input image for barcode recognition. If None, a frame will be captured automatically using `get_frames()`. Supported input types: str: file path to an image (e.g. `D:/images/sample.png`). bytes: encoded image data (e.g. JPEG/PNG stream). np.ndarray: image matrix in OpenCV format (BGR or RGB).

Returns:

(Error code, barcode_results) Error code: int. 0 indicates success; non-zero indicates failure. barcode_results: List. Each detected barcode is represented by a tuple `(bbox, (text, conf), center)`. bbox: List[List[float]]. Four corner points of the barcode box in order top-left, top-right, bottom-right, bottom-left. text: str. Decoded content string. conf: Optional[float]. Confidence score; barcode decoding may not provide a stable confidence score and the value may be None. center: List[float]. Center coordinates `[cx, cy]` of the barcode box.

_abstract _close_capture_device()


Brief:

Disconnect and release the currently connected camera or capture device.

Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _close_kms_device()


Brief:

Close the keyboard and mouse simulation device

Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _close_usb_control_device()


Brief:

Close the control device.

Parameters:

**device_index** – The index of control device.

Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _contrast_img(_org_img_ , _ocr_result_ , _name ='draw_ocr.jpg'_)


Brief:

Visualize OCR results on the original image and save the annotated output image.

Parameters:

  * **org_img** – Union[str, np.ndarray]. The original image. Can be provided as a file path or an OpenCV image array.
  * **ocr_result** – List. OCR result data obtained from the `ocr()` interface. Expected structure is a list of detected text items. Each item is represented by a tuple `(bbox, (text, conf), center)`. bbox: List[List[float]]. Four corner points of the detected text box. text: str. Recognized text content. conf: float. Confidence score. center: List[float]. Center coordinates `[cx, cy]` of the text box.
  * **name** – str. Output file name for the visualized image. Default value is `draw_ocr.jpg`.


Returns:

Error code Error code: int. 0 indicates success; non-zero indicates failure.

_abstract _detect_and_correct_orientation(_img_)


Brief:

Detect the orientation of the input image and apply rotation to correct it.

Parameters:

**img** – Union[str, bytes, numpy.ndarray], Input image for orientation detection. - str: Path to the image file (e.g., “./images/sample.png”). - bytes: Encoded image data (e.g., JPEG/PNG stream). - numpy.ndarray: Image matrix in OpenCV format (BGR or RGB).

Returns:

(Error code, correction_img) Error code: int. 0 indicates success; non-zero indicates failure. correction_img: numpy.ndarray. The image matrix after applying the necessary rotation to correct its orientation.

_abstract _evaluate_device_status()


Brief:

Evaluate the overall device setup quality and return a single normalized score.
This method evaluates device setup quality based on camera pose alignment, visible screen coverage, and OCR timestamp reliability.

Returns:

(Error code, evaluation_score) Error code: int. 0 indicates success; non-zero indicates failure. evaluation_score: float. Final evaluation score in [0.0, 1.0]. Higher values indicate better device setup quality.

Note:

If pose evaluation or OCR evaluation fails, this method returns the corresponding error code immediately and `evaluation_score` is 0.0.

_abstract _get_frames(_frame_count_ , _frame_size_)


Brief:

Capture a specified number of frames from the opened capture device.

Parameters:

  * **frame_count** – int, Number of frames to capture.
  * **frame_size** – tuple[int, int], Desired output frame size (width, height).


Returns:

Error code. 0 indicates success, non-zero indicates failure. frames: List[np.ndarray], list of captured image frames.

_abstract _get_usb_mode()


Brief:

Query the current USB mode.

Returns:

(Error code, USB mode) Error code: int. 0 indicates success; non-zero indicates failure. USB mode: USBMode. Current USB mode. Supported values include: USBMode.ADB: Connected as ADB (debug mode). USBMode.OTG: Connected as OTG (peripheral mode). USBMode.OFF: USB connection disabled.

_abstract _img_similarity(_src_img_ , _tar_img_)


Brief:

Calculate the similarity score between two input images.

Parameters:

  * **src_img** – Union[str, bytes, numpy.ndarray], Source image. - str: Path to the source image file (e.g., “./images/src.png”) - bytes: Encoded image data (e.g., JPEG/PNG stream) - numpy.ndarray: Image matrix in OpenCV format (BGR or RGB)
  * **tar_img** – Union[str, bytes, numpy.ndarray], Target image. - str: Path to the target image file (e.g., “./images/tar.png”) - bytes: Encoded image data - numpy.ndarray: Image matrix in OpenCV format


Returns:

Error code (int): 0 indicates success, non-zero indicates failure. Similarity score (float): Ranges from 0.0 to 1.0, where higher values indicate greater similarity; None on failure.

_abstract _img_template_matching(_template_img_ , _target_img_ , _threshold =0.8_)


Brief:

Locate the position of the template image within the target image using template matching.

Parameters:

  * **template_img** – Union[str, bytes, numpy.ndarray], Template image to be searched. - str: Path to the template image file (e.g., “./images/template.png”) - bytes: Encoded image data (e.g., JPEG/PNG stream) - numpy.ndarray: Image matrix in OpenCV format (BGR or RGB)
  * **target_img** – Union[str, bytes, numpy.ndarray], Target image in which the template is to be located. - str: Path to the target image file (e.g., “./images/target.png”) - bytes: Encoded image data - numpy.ndarray: Image matrix in OpenCV format
  * **threshold** – float, default=0.8. Matching confidence threshold. The value range: 0.0 ~ 1.0 The detected match is considered valid only if the matching score is greater than or equal to this value.


Returns:

Error code (int): 0 indicates success, non-zero indicates failure. Matched coordinates (tuple[float, float]): The (x, y) center position of the best-matched region; None on failure.

Notes:

  * A return of (0, None) means “no valid match found” and should be handled as a normal outcome.
  * Callers MUST check both error_code and matched coordinates.


_abstract _keyboard_hotkey(_keys_)


Brief:

Simulate pressing a single function key or a key combination (hotkey). All specified keys are pressed sequentially and then released in reverse order, enabling combinations such as Ctrl+Shift+S or Alt+Tab.

Parameters:

**keys** – Union[List[KeyboardKey], KeyboardKey], The key or combination of keys to execute. - List of keys (e.g., [KeyboardKey.CTRL, KeyboardKey.C]) - Single key (e.g., KeyboardKey.ENTER) The logical behavior of key press and release is consistent with keyboard_keydown and keyboard_keyup.

Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _keyboard_keydown(_key_)


Brief:

Simulate pressing (without releasing) a keyboard key. This is typically used for key combination or long-press scenarios.

Parameters:

**key** – enum, Keyboard key type (KeyboardKey). Supported standard key values include: - Control keys: CTRL, SHIFT, ALT, WIN - Function keys: F1 ~ F12 - Alphabet keys: A ~ Z - Numeric keys: KEY_0 ~ KEY_9 - Arrow keys: UP, DOWN, LEFT, RIGHT - Editing keys: ENTER, TAB, ESC, BACKSPACE, DELETE, INSERT - System keys: CAPSLOCK, NUMLOCK, SCROLLLOCK, PRINTSCREEN - Space and symbol keys: SPACE, MINUS, EQUAL, COMMA, PERIOD, SLASH, SEMICOLON, QUOTE, BACKQUOTE, BRACKET_LEFT, BRACKET_RIGHT, BACKSLASH Example: KeyboardKey.CTRL, KeyboardKey.SHIFT, KeyboardKey.A, KeyboardKey.F5, KeyboardKey.UP

Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _keyboard_keyup(_key =None_)


Brief:

Release a specified key or all pressed keys. When a specific key is provided, only that key will be released. When key is None, all currently pressed keys will be released. This method should be used together with keyboard_keydown to simulate realistic keyboard input sequences following HID protocol behavior.

Parameters:

**key** – enum or None. - If enum: the specific KeyboardKey to release. - If None: release all pressed keys (send an all-zero HID report).

Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _keyboard_text_write(_text : str_)


Brief:

Simulate typing plain text input without interpreting any modifier or control keys. If the text contains uppercase letters, the system automatically triggers the Shift combination to output the correct character. For example, passing “Ctrl” will type the text “Ctrl” rather than pressing the Ctrl key.

Parameters:

**text** – str, Text string to be input.

Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _mouse_click(_button_ , _hold_time =0_, _click_count =1_, _interval_time =0_)


Brief:

Perform mouse click operation at the current cursor position for a specified number of times.

Parameters:

  * **button** – enum, Mouse button type. Supported values: - MouseButton.LEFT : Left-click. - MouseButton.MIDDLE : Middle-click. - MouseButton.RIGHT : Right-click.
  * **hold_time** – int, Duration to hold the button for each click (ms).
  * **click_count** – int, Number of consecutive clicks to perform.
  * **interval_time** – int, Time interval between multiple clicks (ms).


Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _mouse_drag(_source_coord_ , _target_coord_ , _run_time =5000_, _step_max =80_)


Brief:

Perform a mouse drag operation from the source coordinate to the target coordinate.

Parameters:

  * **source_coord** – List[float], Starting position of the drag [x, y].
  * **target_coord** – List[float], Ending position of the drag [x, y].
  * **run_time** – int, Total time for the drag movement (ms). Used to control the drag speed. The function will fail if the duration is exceeded.
  * **step_max** – int, Maximum number of movement steps. A higher value results in smoother movement but slower execution.


Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _mouse_scroll(_step =-1_)


Brief:

Execute a mouse wheel scrolling operation.

Parameters:

**step** – int, Scroll step value. Positive for upward scrolling, negative for downward scrolling. - Positive value : Scroll up (equivalent to scrolling content upward for the user). - Negative value : Scroll down (equivalent to scrolling content downward for the user). The effective scrolling distance depends on system and hardware factors. For small scrolls, a step value between 1 and 3 is recommended.

Returns:

Error code. 0 indicates success; non-zero indicates failure.

_abstract _normalize_ocr_result(_ocr_result_)


Brief:

Normalize raw OCR results and convert them into a structured object-oriented format.

Parameters:

**ocr_result** – List. OCR raw results returned by `ocr()`. Each item represents one detection and has the form: `[bbox, (text, conf)]`. bbox: List[List[float]]. Four corner points `[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]`. text: str. Recognized text content. conf: float. Confidence score.

Returns:

List[OcrItem]. Normalized OCR items. Each `OcrItem` contains: text: str. Recognized text. confidence: float. Confidence score. corners: List[List[float]]. Box corner points. center: List[float]. Center coordinates `[cx, cy]`.

_abstract _ocr(_img =None_)


Brief:

Perform OCR on the input image.

Parameters:

**img** – Optional[Union[str, bytes, np.ndarray]]. The input image. If None, a frame will be captured automatically via `get_frames()`. Supported input types: str: file path to an image (e.g. `D:/images/sample.png`). bytes: encoded image data (e.g. JPEG/PNG stream). np.ndarray: image matrix (OpenCV format, BGR or RGB).

Returns:

(Error code, ocr_result) Error code: int. 0 indicates success; non-zero indicates failure. ocr_result: List. OCR results list; each input image corresponds to one sub-list. Each detected text item is represented by a tuple `(bbox, (text, conf), center)`. bbox: List[List[float]]. Four corner points `[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]` in order top-left, top-right, bottom-right, bottom-left. text: str. Recognized text content. conf: float. Confidence score. center: List[float]. Center coordinates `[cx, cy]` of the text box.

_abstract _open_capture_device(_device_index_ , _capture_resolution =(1920, 1080)_, _capture_frame_rate =20_, _stream_format =StreamFormat.MJPG_, _camera_type =CameraType.OPENCV_)


Brief:

Open the specified camera or capture device for image acquisition.

Parameters:

  * **device_index** – int, Index of the camera or capture device.
  * **capture_resolution** – tuple[int, int], (Optional) Capture resolution in pixels (width, height).
  * **capture_frame_rate** – int, (Optional) Frame rate in frames per second.
  * **stream_format** – StreamFormat, (Optional) Video stream format. Available options include: - StreamFormat.YUY2 : YUYV422 format - StreamFormat.MJPEG : Motion JPEG compressed format - StreamFormat.H264 : H.264 compressed format - StreamFormat.NV12 : Semi-planar YUV format - StreamFormat.RAW : Raw frame data format
  * **camera_type** – CameraType, (Optional) Type of the camera. Available options include: - CameraType.OPENCV : Use OpenCV library for video capture, suitable for most standard cameras. - CameraType.CONSUMER : Consumer-grade cameras (e.g., Sony cameras) that require specific SDKs.


Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _open_kms_device(_device_index_)


Brief:

Open the keyboard and mouse simulation device

Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _open_usb_control_device(_device_index_)


Brief:

Open the control device.

Parameters:

**device_index** – The index of control device.

Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _qrcode(_img =None_)


Brief:

Perform QR code detection and decoding on the input image.
If no image is provided, one frame will be captured automatically from the connected device via `get_frames()`.

Parameters:

**img** – Optional[Union[str, bytes, np.ndarray]]. Input image for QR code recognition. If None, a frame will be captured automatically using `get_frames()`. Supported input types: str: file path to an image (e.g. `D:/images/sample.png`). bytes: encoded image data (e.g. JPEG/PNG stream). np.ndarray: image matrix in OpenCV format (BGR or RGB).

Returns:

(Error code, qrcode_results) Error code: int. 0 indicates success; non-zero indicates failure. qrcode_results: List. Each detected QR code is represented by a tuple `(bbox, (text, conf), center)`. bbox: List[List[float]]. Four corner points of the QR code box in order top-left, top-right, bottom-right, bottom-left. text: str. Decoded content string. conf: Optional[float]. Confidence score; QR decoding may not provide a stable confidence score and the value may be None. center: List[float]. Center coordinates `[cx, cy]` of the QR code box.

_abstract _relative_move(_dx_ , _dy_ , _run_time =5000_, _step_max =80_)


Brief:

Move the mouse cursor by the specified relative offset from its current position.

Parameters:

  * **dx** – float, Offset along the X-axis (unit: pixels). Positive values move right; negative values move left.
  * **dy** – float, Offset along the Y-axis (unit: pixels). Positive values move down; negative values move up.
  * **run_time** – int, Total time for cursor movement in milliseconds (ms). The function will fail if the movement exceeds this time limit.
  * **step_max** – int, Maximum displacement per step (unit: pixels).


Returns:

Error code (int): 0 indicates success; non-zero indicates failure. Coordinates (List[float]): Final cursor position [x, y] after movement. Returns None on failure.

_abstract _save_frame(_frame_ , _photo_path_)


Brief:

Save an image frame to the specified directory.

Parameters:

  * **frame** – np.ndarray, The frame to be saved, represented as a NumPy array.
  * **photo_path** – str, Target directory path where the image will be saved. If the directory does not exist, it will be automatically created. Example: “./output/test.png” (relative path) or “/tmp/test.png” (absolute path)


Returns:

Error code. 0 indicates success, non-zero indicates failure. save_path: str, path of the saved image file.

_abstract _switch_usb_mode(_usb_mode =USBMode.ADB_)


Brief:

Switch the USB mode to the specified mode.

Parameters:

**rec_type** – enum, USB mode. Supported values: - USBMode.ADB : Connect as ADB (debug mode). - USBMode.OTG : Connect as OTG (peripheral mode). - USBMode.OFF : Disable USB connection.

Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _take_photo(_frame_size =None_, _photo_path =None_)


Brief:

Capture a photo and save it to the specified path.

Parameters:

  * **frame_size** – Optional[Tuple[int, int]]. (width, height): resize the captured frame to the specified resolution before saving. None: keep the original capture resolution; no resize is performed.
  * **photo_path** – Optional[str]. Output file path. Non-empty string: use the given path. Supports relative paths (e.g. `./output/test.png`) and absolute paths (e.g. `C:/tmp/test.png` or `/tmp/test.png`). Parent directories will be created automatically if they do not exist. None or empty string: automatically generate a filename (e.g. `capture_YYYYMMDD_HHMMSS.jpg`) under the current working directory returned by `os.getcwd()`.


Returns:

(Error code, saved_path) Error code: int. 0 indicates success; non-zero indicates failure. saved_path: str. Absolute path of the saved photo file when success; empty string on failure.

_abstract _video_recorder(_file_path_ , _frame_size_ , _frame_rate_ , _frame_count_)


Brief:

Record a video sequence from the capture device and save it to the specified path.

Parameters:

  * **file_path** – str, File path where the recorded video will be saved.
  * **frame_size** – tuple[int, int], Resolution of the video frames (width, height).
  * **frame_rate** – int, Frame rate (frames per second).
  * **frame_count** – int, Number of frames to record.


Returns:

Error code. 0 indicates success, non-zero indicates failure.

_abstract _wait_element(_element_ , _timeout_ , _rec_type =RecType.OCR_)


Brief:

Wait for a target element (text or image template) to appear in the video stream, and return the detected position.

Parameters:

  * **element** – Union[str, bytes], Element to detect. - str : Text content. The method uses OCR to check whether the text appears. - bytes : Image template (encoded image data). The method uses template matching to check presence.
  * **timeout** – int, Maximum waiting time in milliseconds. If the target is not detected within the specified time window, the function returns failure.
  * **rec_type** – enum, Detection mode. Supported values: - RecType.OCR : Use OCR to detect whether the str element appears. - RecType.QRCODE : Use a QR-code recognizer to detect whether the str element appears. - RecType.BARCODE : Use a barcode recognizer to detect whether the str element appears.


Returns:

Error code (int): 0 indicates success; non-zero indicates failure (e.g., not detected). Coordinates: (x, y) center of the detected element when successful; None on failure.

_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.CameraType(_value_)

Bases: `Enum`
摄像头类型

CONSUMER _ = 'Consumer'_


OPENCV _ = 'OpenCV'_


_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.KeyboardKey(_value_)

Bases: `Enum`
An enumeration.

A _ = 4_


B _ = 5_


BACKSPACE _ = 42_


C _ = 6_


CAPSLOCK _ = 57_


D _ = 7_


DELETE _ = 76_


DOWN _ = 81_


E _ = 8_


END _ = 77_


ENTER _ = 40_


ESC _ = 41_


F _ = 9_


F1 _ = 58_


F10 _ = 67_


F11 _ = 68_


F12 _ = 69_


F2 _ = 59_


F3 _ = 60_


F4 _ = 61_


F5 _ = 62_


F6 _ = 63_


F7 _ = 64_


F8 _ = 65_


F9 _ = 66_


G _ = 10_


H _ = 11_


HOME _ = 74_


I _ = 12_


INSERT _ = 73_


J _ = 13_


K _ = 14_


KEY_0 _ = 39_


KEY_1 _ = 30_


KEY_2 _ = 31_


KEY_3 _ = 32_


KEY_4 _ = 33_


KEY_5 _ = 34_


KEY_6 _ = 35_


KEY_7 _ = 36_


KEY_8 _ = 37_


KEY_9 _ = 38_


L _ = 15_


LALT _ = 226_


LCTRL _ = 224_


LEFT _ = 80_


LGUI _ = 227_


LSHIFT _ = 225_


M _ = 16_


N _ = 17_


O _ = 18_


P _ = 19_


PAGEDOWN _ = 78_


PAGEUP _ = 75_


PRINTSCREEN _ = 70_


Q _ = 20_


R _ = 21_


RALT _ = 230_


RCTRL _ = 228_


RGUI _ = 231_


RIGHT _ = 79_


RSHIFT _ = 229_


S _ = 22_


SCROLLLOCK _ = 71_


SPACE _ = 44_


T _ = 23_


TAB _ = 43_


U _ = 24_


UP _ = 82_


V _ = 25_


W _ = 26_


X _ = 27_


Y _ = 28_


Z _ = 29_


_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.MouseButton(_value_)

Bases: `Enum`
An enumeration.

LEFT _ = 'left'_


MIDDLE _ = 'middle'_


RIGHT _ = 'right'_


_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.OcrModel(_value_)

Bases: `Enum`
An enumeration.

Enhanced _ = 2_


Light _ = 0_


Premium _ = 3_


Standard _ = 1_


_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.RecType(_value_)

Bases: `Enum`
An enumeration.

BARCODE _ = 'BARCODE'_


OCR _ = 'OCR'_


QRCODE _ = 'QRCODE'_


_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.StreamFormat(_value_)

Bases: `Enum`
图像数据流格式

H264 _ = 'H264'_


MJPG _ = 'MJPG'_


NV12 _ = 'NV12'_


RAW _ = None_


YUY2 _ = 'YUY2'_


_class _ark.ark_visualsims.visualsims.ark_visualsims_interface.USBMode(_value_)

Bases: `Enum`
An enumeration.

ADB _ = 'ADB'_


OFF _ = 'OFF'_


OTG _ = 'OTG'_

## Module contents
