from logger import logger # Our logger.py file that goes along our project files

# Our function but with a decorator with custome success/error messages
@logger(on_success = 'Success', on_failure = 'Cannot multiply non-int values')
def square(value: int) -> int:
  return (value * value)

square('Whoops!') # We can't multiple string to string