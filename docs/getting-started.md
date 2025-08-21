# Getting Started

## Installation & Build


### From source code via {==uv==}

``` zsh
git clone 
cd ChewPy
uv sync
uv build --refresh
uv tool install --refresh . #uv tool install .
uv tool uninstall chewpy
```

### From Pypi via {==uv==}

```
uvx install chewpy
```

## How to Run

### As a library

```python
import chewpy

# Example usage
chewpy.do_something()
```

### As a module

```
python -m chewpy --help
```

### As a ClI Tool

```
uvx chewpy --help 
```

## Project layout

    src/          # 
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        assets/   # Images and other files.
        ...       # Other markdown pages.

## Docs

``` zsh
uv run mkdocs serve #Start the live-reloading docs server.
uv run mkdocs build #Build the documentation site.
```