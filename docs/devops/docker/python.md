# Containerizing Python Applications with Docker

## Ignore Python-specific artifacts

Often, when you build a Docker image, you will end up copying Python code directly of the local machine into a Docker image. If you have previously executed your program, you might end up copying your `__pycache__` folders containing compiled `.pyc` files. PyTest is notorious for screaming at you, if you copy your code somewhere else and forget to clear the cache:

```text
import file mismatch:
...
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```

This is where a `.dockerignore` file comes handy. Similar to a `.gitignore` file, it will exclude directory/file patterns you put there from being copied onto the final Dcoker image. Here is a simple `.dockerignore` file you can add to the root of your Python project:[^dockerignore]

```text
.git/

**/*.pyc
**/__pycache__
```

[^dockerignore]: [Sample .dockerignore file for Python projects](https://github.com/docker/docker-py/blob/master/.dockerignore)
