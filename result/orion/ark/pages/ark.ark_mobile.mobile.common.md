---
title: "ark.ark_mobile.mobile.common package"
docname: "ark.ark_mobile.mobile.common"
source: "http://orion.longsys.com/ark.ark_mobile.mobile.common.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_mobile.mobile.common package
## Submodules
## ark.ark_mobile.mobile.common.error_contract module
Create structured failures and enforce the public error contract.

ark.ark_mobile.mobile.common.error_contract.cause_fail(_code_ , _stage_ , _cause =None_, _message =''_)

Pass through an existing structured cause or create the local failure.

ark.ark_mobile.mobile.common.error_contract.command_fail(_stage_ , _result_ , _message =''_, _details =None_)


ark.ark_mobile.mobile.common.error_contract.fail(_code_ , _stage_ , _message =''_, _source ='ark_mobile'_, _** kwargs_)


ark.ark_mobile.mobile.common.error_contract.failure(_stage_ , _code_ , _message =''_, _source ='ark_mobile'_, _native_return_code =None_, _raw_message =''_, _details =None_)


ark.ark_mobile.mobile.common.error_contract.helper_fail(_code_ , _stage_ , _data_ , _message =''_)

Create one failure from the documented FileHelper error dictionary.

ark.ark_mobile.mobile.common.error_contract.public_contract(_interface_)

Validate public arguments and assert response shape without rewriting it.

ark.ark_mobile.mobile.common.error_contract.validate_response(_operation_ , _response_)

## ark.ark_mobile.mobile.common.errors module
ark_mobile error-code helpers.

ark.ark_mobile.mobile.common.errors.describe(_code : int_) → str

Return a stable diagnostic summary for a public error code.

ark.ark_mobile.mobile.common.errors.mobile_error(_reason : int_) → int

## ark.ark_mobile.mobile.common.validation module
Validate public interface arguments before device-specific code runs.

ark.ark_mobile.mobile.common.validation.validate_call(_signature_ , _args_ , _kwargs_)

## Module contents
Cross-platform error handling and public-contract validation.
