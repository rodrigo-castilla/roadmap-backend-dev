# Logging

The `logs` are objects that recap actions, errors, messages...

In Python we use de module `logging`, it includes create Object _logger_, setters and getters, Handlers, Formatters...

Its subdivided in:

- Object _logger_ -> `logging.getLogger("nameLogger")`
- Handler -> `logging.StreamHandler()` / `logging.FileHandler(<opts>)`
- Formatter -> `logging.Formatter(<opts>)`

Important, for use Handlers and Formatters in an Object Logger we have to add it:

```bash
logger.addHandler(handler)
logger.addFormatter(formatter)
```

## Resources

[logging realpython](https://realpython.com/python-logging/)
