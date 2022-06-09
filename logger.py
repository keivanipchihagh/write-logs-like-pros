import logging

# Create the logging module
logging.basicConfig(
    format = '%(asctime)s - %(levelname)s - %(message)s',       # Format of the log
    datefmt = '%m/%d/%Y %I:%M:%S %p',                           # The format of the date
    filename = 'logs.log',                                      # The name of the file
    level = logging.DEBUG                                       # The minimum level of the log
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
def logger(func, on_success = None, on_failure = None):
    '''
    A decorator that logs the running of a function.

    Parameters:
        on_success (function): A function to be called when the function is successful.
        on_failure (function): A function to be called when the function fails.
    '''

    def run(*args, **kwargs):
        try:
            _return = func(*args, **kwargs)
            
            if on_success: _logger.info(on_success)

            if _return is not None:
                return _return

        except Exception as ex:
            if on_failure:
                _logger.error(on_failure)
            else:
                _logger.error(ex)

    return run