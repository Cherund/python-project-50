# Difference generator


### Hexlet tests and linter status:
[![Actions Status](https://github.com/Cherund/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cherund/python-project-50/actions)
[![Self written tests](https://github.com/Cherund/python-project-50/actions/workflows/diff-check.yml/badge.svg)](https://github.com/Cherund/python-project-50/actions/workflows/diff-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/5e796ed120db98e38c50/maintainability)](https://codeclimate.com/github/Cherund/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5e796ed120db98e38c50/test_coverage)](https://codeclimate.com/github/Cherund/python-project-50/test_coverage)

## Description


Difference generator is a program that determines difference between two data structures.
Supported formats:  ```json```, ```yml``` and ```yaml```.


## Installation


Clone the repository and use this commands:

```
make install
make build
make package-install
```


## Optional arguments

1. **-h, --help**  `gendiff -h` - launch help
2. **-f, --format** `gendiff -f` - set format of output. **Available styles:**
* `-f stylish` - default format
* `-f plain`
* `-f json`


### Comparison of flat files (JSON)

`gendiff file1.json file2.json`

[![asciicast](https://asciinema.org/a/631993.svg)](https://asciinema.org/a/631993)

### Comparison of flat files (YAML, YML)

`gendiff file1.yml file2.yml`

[![asciicast](https://asciinema.org/a/631994.svg)](https://asciinema.org/a/631994)

### Comparison of two files with a nested structure (JSON)

`gendiff nested_file1.json nested_file2.json`

[![asciicast](https://asciinema.org/a/631995.svg)](https://asciinema.org/a/631995)

### Comparison of two files with a nested structure (YML, YAML)

`gendiff nested_file1.yml nested_file2.yml`

[![asciicast](https://asciinema.org/a/631997.svg)](https://asciinema.org/a/631997)

### Work example formatter PLAIN

`gendiff -f plain nested_file1.json nested_file2.json`

[![asciicast](https://asciinema.org/a/631998.svg)](https://asciinema.org/a/631998)

### Work example formatter JSON

`gendiff -f json filepath1.json filepath2.json`

[![asciicast](https://asciinema.org/a/631999.svg)](https://asciinema.org/a/631999)
