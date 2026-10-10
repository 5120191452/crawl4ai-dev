---
title: "ark.ark_common.decorator package"
docname: "ark.ark_common.decorator"
source: "http://orion.longsys.com/ark.ark_common.decorator.html"
depth: 1
crawled_at: "2026-10-10T03:24:13.408473+00:00"
---

# ark.ark_common.decorator package
## Submodules
## ark.ark_common.decorator.decorator module

ark.ark_common.decorator.decorator.close_new_explorer_windows(_process_name_)


Brief:

A decorator factory that returns a decorator to monitor and close new windows created by explorer.exe.

Returns:

Callable: A decorator that can be applied to a function to track and close new explorer.exe windows that are opened during the function’s execution.

ark.ark_common.decorator.decorator.decorator_factory(_other_decorator_ , _* other_decorator_args_, _** other_decorator_kwargs_)


Brief:

Create a decorator factory that produces a new decorator by applying another decorator.

Parameters:

  * **other_decorator** – The decorator function to be applied first to the target function.
  * ***other_decorator_args** – Positional arguments to be passed to the other_decorator.
  * ****other_decorator_kwargs** – Keyword arguments to be passed to the other_decorator.


Returns:

callable: A new decorator function that takes a function as an argument and returns a new function that combines the functionality of other_decorator and additional logic.

ark.ark_common.decorator.decorator.lock_decorator_with_lock(_lock_)


Brief:

A decorator factory that returns a decorator that locks a function using the provided lock.

Parameters:

**lock** – A lock object to be used for synchronizing access to the decorated function.

Returns:

Callable: A decorator that can be applied to a function to make it safe by acquiring the lock before execution.

ark.ark_common.decorator.decorator.record_execution_info_decorator(_record_param =False_, _record_time =False_, _record_result =False_)


Brief:

A decorator factory that returns a decorator to record execution information of a function.

Parameters:

  * **record_param** – Whether to record the function’s parameters. Defaults to False.
  * **record_time** – Whether to record the function’s execution time. Defaults to False.
  * **record_result** – Whether to record the function’s return result. Defaults to False.


Returns:

Callable: A decorator that can be applied to a function to record its execution information based on the provided options.
## Module contents
@Module ：ark_common_decorator
@Date ：2024/5/16 16:27
@Version ： V1.0.0
  *

describe：

    * The decorator is a Python package designed to provide a series of powerful and flexible decorators for enhancing the functionality of functions. These decorators simplify code, improve readability, and allow developers to handle common programming tasks in a more elegant manner.
  *

Key Features:

    * Feature-rich: The decorator package includes various types of decorators that cover common needs such as locking and logging execution information.
    * Easy to Use: Each decorator provides clear documentation and examples, enabling developers to quickly understand and utilize them.
    * Composability: Decorators can be combined to create more complex behaviors.
    * Performance Optimization: During the design of the decorators, performance factors are taken into account to ensure they do not negatively impact the program’s efficiency.
  *

How to Use:

    * To utilize the decorators from the decorator_utils package, simply import them into your Python project and apply them to functions or classes. For example:

```
from decorator_utils.record_execution_info_decorator import record_execution_info_decorator

@record_execution_info_decorator()
def expensive_function(x, y):
    # Function implementation...
    pass

```
Copy to clipboard
    * In the above example, the expensive_function is decorated with the record_execution_info_decorator, which enables it to record execution information.
