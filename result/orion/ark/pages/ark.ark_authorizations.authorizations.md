---
title: "ark.ark_authorizations.authorizations package"
docname: "ark.ark_authorizations.authorizations"
source: "http://orion.longsys.com/ark.ark_authorizations.authorizations.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_authorizations.authorizations package
## Submodules
## ark.ark_authorizations.authorizations.ark_authorizations_factory module
@Project :Orion @File :ark_camera_factory.py @IDE :PyCharm @Author :xiaoze @Date :2024/7/15 10:42

_class _ark.ark_authorizations.authorizations.ark_authorizations_factory.ArkAuthorizationsFactory(_* args_, _** kwargs_)

Bases: `object`

create_object()

## ark.ark_authorizations.authorizations.ark_authorizations_interface module
@Project ：OrionProject @File ：ark_authorizations_interface.py @IDE ：PyCharm @Author ：xiaoze @Date ：2024/6/19 09:40

_class _ark.ark_authorizations.authorizations.ark_authorizations_interface.ArkAuthorizationsInterface

Bases: `object`

_abstract _get_machine_code()


Brief:

Retrieves the unique machine code of the current device.

Returns:

tuple[int, str] Returns a tuple containing: - int: Error code, 0 indicates success, non-zero indicates failure. - str: The machine code string if retrieval is successful; None otherwise.

_abstract _offline_authorization(_authorization_code_)


Brief:

Performs offline authorization using a provided authorization code.

Parameters:

**authorization_code** – str The authorization code obtained from the server or Orion web, based on the device’s machine code.

Returns:

int Returns 0 if offline authorization succeeds, otherwise returns an error code indicating the failure reason.

_abstract _online_authorization()


Brief:

Performs online authorization by communicating with the authorization server.

Returns:

int Returns 0 if online authorization succeeds, otherwise returns an error code indicating the failure reason.

_abstract _validate_authorization()


Brief:

Validates whether the current device has been authorized.

Returns:

int Returns 0 if the device is authorized, otherwise returns an error code indicating the reason for failure.
## Module contents
