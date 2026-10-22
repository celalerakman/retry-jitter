# Retry Jitter

Bounded exponential backoff with injectable full jitter.

An injected random source makes retry scheduling reproducible in tests. The exponential cap reaches 300 seconds.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
