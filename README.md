# Price Formatter

Formats the price in a readable form.

# Descriprion

It can be used from the console as well as in third-party programs.
To connect you need to import the function
```python
from format_price import format_price
```
A string of numbers is passed as a function parameter. Returns a function of a ``formatted
 string`` or ``None`` if the string cannot be converted to a positive floating point number

# Example

```bash
$ python image_resize.py 3245.000000# possibly requires call of python3 executive instead of just python
3 245    

$ python image_resize.py f2345
None
```

Running on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
