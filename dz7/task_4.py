import time
from typing import Callable, Any


def function_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        time_for_func = end - start
        print(f"The function took {time_for_func:.4f} seconds to execute")
        return res

    return wrapper


@function_time
def sum_numbers(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


result = sum_numbers(5647678)
print(f"Result: {result}")
