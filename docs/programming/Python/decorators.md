# Decorators

## Decorator Use Cases

### Wrap a function

There are situations, where it is helpful to apply the same logic to a function, without having to affect the logic of the function itself. The simplest example is measuring the execution time of a given function. The following code describes a simple `measure` decorator, which when applied to a function, would measure and log the time it took to execute this function:

```python
import logging
import time
from functools import partial, wraps

LOGGER = logging.getLogger("my_logger")


def measure(f=None, label=""):
    if f is None:
        return partial(measure, label=label)

    @wraps(f)
    def wrap(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)

        LOGGER.debug(
            f"{label} {f.__qualname__} -- execution time: {time.time() - start} s"
        )
        return result

    return wrap
```

The application of this decorator is extremely simple too:

```python
@measure
def my_func():
    # do something
```

```python
@measure(label="fancy label")
def my_func():
    # do something
```

Notice the use of `functool.wraps` and `functool.partial` in order to get this running. The use of `functools.partial` in this context is a topic for a whole post of its own, but here it should suffice to say that it _“freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature_.[^partial1][^partial2]

[^partial1]: [How to Write a Decorator with an Optional Argument?](https://pybit.es/decorator-optional-argument.html)
[^partial2]: [functools.partial | Python Docs](https://docs.python.org/3.6/library/functools.html#functools.partial)
