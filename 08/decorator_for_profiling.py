import cProfile
from functools import wraps
import pstats


def profile_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'profiler'):
            wrapper.calls = 1
            wrapper.profiler = cProfile.Profile()
        else:
            wrapper.calls += 1
        ans = wrapper.profiler.runcall(func, *args, **kwargs)
        return ans

    def print_stat():
        stats = pstats.Stats(wrapper.profiler)
        stats.print_stats()

    wrapper.print_stat = print_stat
    return wrapper


@profile_deco
def add(a, b):
    for _ in range(0, 1000000):
        1 + 1
    return a + b


@profile_deco
def sub(a, b):
    for _ in range(0, 1000000):
        1 + 1
    return a - b


add(1, 2)
add(4, 5)
sub(4, 5)

add.print_stat()
sub.print_stat()
