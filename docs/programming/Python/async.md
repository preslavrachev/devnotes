# Asynchronous Processing

Despite the fair biit of controversy, Python **does** support various means of achieving concurrency: `processes`, `threads`, and, as of recently `async IO` support, based on an event-loop. 

## What to use where

```python
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
       print("Use Threads")
else:
    print("Multi Processing")
```

via [Async Python: The Different Forms of Concurrency](http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/)