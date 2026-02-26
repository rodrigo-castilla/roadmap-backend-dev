# Roadmap Backend Dev

## Ciclo 4 pasos

Metodología de estudio:

1. (30min) lectura / comprensión
2. (1h) código / puesta en práctica
3. (20min) documentación / obsidian
4. (10min) subir progreso / git

## Projects structure

Best practice for structuring a python project is to use `src/layout`. The code is organized in the **src** folder and tests, docs, bin, scripts... out of the code folder.
The basic structure for `src/layout` is the following one:

```txt
project_name/
├── bin/                  # Optional
│   └── project_name
├── docs/                 # Optional
│   ├── index.html
│   └── source.txt
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── __main__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py

│   └── test_module2.py
├── LICENSE
├── README.md
└── pyproject.toml
```
