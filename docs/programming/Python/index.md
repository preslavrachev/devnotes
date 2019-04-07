# Python Basics
## Iterators
### Iterator vs. Iterable
This is a commonly asked question. In general, an `Iterable` object can be anything, as long as it implements the standard `__iter()__` method. Python lists, tuples, maps, and of course, iterators, all implement this method. You can think of `Iterable` as an interface or protocol.

The `Iterator` on the other hand, is a one specific implementation of the `Iterable` protocol, which tries to be memory-efficient, thus its values can be accessed one at a time. Iterators implement an additional method called `__next()__`, which gets called upon every pass, and returns one value at a time. Iterators are all over the placein Python, and pretty much every collection type (e.g. map, list, etc) can be turned into and Iterator, by wrapping the collection with the `iter()` function. Additionaly, `map`, `filter`, and also, functions using `yield`, all return Iterator instances.

### Accessing the Index of an Iterable Row
If you are looping over an iterator or a list, often you'd like to get the index of the particular row you're on. This is where the `enumerate` function comes handy:

```python
# assuming that items is an iterable object
for idx, item in enumerate(items):
    print(idx, item)
```

!!! info "enumerate[^enumerate_docs]"
    Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The `__next__()` method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

[^enumerate_docs]: [enumerate | Python Docs](https://docs.python.org/3/library/functions.html#enumerate)

## Setup and Installing Dependencies
### requirements.txt
#### Requirements files can invoke other requirements files
In a very simple form of inheritance `requirements.txt` can get the dependencies of other `requiements.txt` files, and add additional ones on top. How is this useful? Let's say that you keep your common dependencies in `requirements.txt` and have additional tooling and dependencies in a separate file, let's call it `requirements-dev.txt`. When you do your local setup instead of doing the usual drill:

```bash
pip install -r requirements.txt
```

you will do the following:


```bash
pip install -r requirements-dev.txt
```

All you need to do, in order for you to get all the original dependencies listed in `requirements.txt`, is to add one line to `requirements-dev.txt`:


```bash
-r requirements.txt

# Add your other developer and tooling dependencies underneath
```

