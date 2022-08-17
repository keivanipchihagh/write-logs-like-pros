import os
import logging
import time


if not os.path.exists('logs'):
    os.makedirs('logs')


# Create the logging module
logging.basicConfig(
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%m/%d/%Y %I:%M:%S %p',
    filename = f'{os.getcwd()}/logs/{time.strftime("%Y-%m-%d_%H-%M-%S")}.log',
    level = logging.INFO,
    filemode = "w"
)
_logger = logging.getLogger(__name__)


# A Meta-Decorator (A decorator that can be used to decorate other decorators) is used on top of decorates to enable them to be parametrized
def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


# A logger decorator
@parametrized
def logger(func, on_failure: str = None, on_success: str = None, raise_err: bool = True):
    """
        A decorator that logs the function's execution status onto a file

        parameters:
            func: The function to be logged.
            on_failure (str): Failure message if the function fails. If None, the message will be the actual error message.
            on_success (str): Success message if the function executes successfully. (optional)
            raise_err (bool): Whether to raise an error if the function fails. It doesn't effect the 'on_failure' parameters behavior. (default: True)
    """

    def run(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            if on_success:
                _logger.info(on_success)
            
            # Return the return value of the function
            return None if result is None else result

        except Exception as ex:            
            _logger.error(on_failure if on_failure else ex)

            # Raise exception if raise_err is True
            if raise_err:
                raise ex

    return run