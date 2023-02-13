from time import perf_counter
import functools

class ProcessDurationManager:
    """ TP n° 5 : Context manager """

    def __init__(self, name):
        self.func_name = name
        self.now = 0
        self.duration = 0

    def __enter__(self):
        self.now = perf_counter()
        return self.now

    def __exit__(self, exc_type, exc_value, traceback):
        self.duration = perf_counter() - self.now
        print(f'\t>>> [Duration for {self.func_name} : {self.duration} s]')


def duration(f):
    """ Decorator """
    @functools.wraps(f)
    def wrapper(final_args):
        processDurationManager = ProcessDurationManager(f.__name__)
        with processDurationManager:
            f(final_args)
        return f(final_args)
    return wrapper