# write-logs-like-pros
## What and Why?
Every automated module and scheduled code will at some point run into problems that will cause exceptions to occur. Often times, we want to log our code to monitor its progress. Using _Try-Catch_ the classic way works fine, but is messy and often ruins the flow of the code.

## Clean-Code Architecture
> As you've probably read elsewhere, a function should do one thing, and only one thing. “Functions should do something, or answer something, but not both.” As he states, a function should change the state of an object, or return some information about that object, but not both. - [Clean Code](https://alvinalexander.com/programming/clean-code-quotes-robert-c-martin#:~:text=As%20you've%20probably%20read,that%20object%2C%20but%20not%20both.)

## How it Works
We learned from the previous quote from **Martin C.Roberts** that every function has only one task to do and can only succeed/fail at that spesific task; So, only one exception can happen and one success message if nothing goes wrong.

## Usage
We have a simple module in _logger.py_ that writes logs into a file:
```python
import logging

# Create the logging module
logging.basicConfig(
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%m/%d/%Y %I:%M:%S %p',
    filename = 'logs.log',
    level = logging.DEBUG
)
_logger = logging.getLogger(__name__)
```

Using the classic _Try-Catch_ architecture:
```python
from logger import _logger # Our logger.py file that goes along our project files

# Our function
def square(value: int): return (value * value)

try:
    result = square('Whoops!') # We can't multiple string to string
except:
    print('Cannot multiply non-int values')                       # Print on console
    _logger.error('Cannot multiply non-int values')               # Write logs in file
```

Using decorators:
```python
from logger import logger # Our logger.py file that goes along our project files

# Our function but with a decorator with custome success/error messages
@logger(on_success = 'Success', on_failure = 'Cannot multiply non-int values')
def square(value: int) -> int:
  return (value * value)

square('Whoops!') # We can't multiple string to string
```

## Further Customizations
You can of course customize the decorator body and parameters according to your needs.
