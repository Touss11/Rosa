def validate_promise_range(promise_range):
    if not isinstance(promise_range, (list, tuple)) or len(promise_range) != 2:
        raise ValueError("Promise range must be a list or tuple of two numeric values.")
    if promise_range[0] >= promise_range[1]:
        raise ValueError("The first value of the promise range must be less than the second value.")
    return promise_range

def generate_promise_values(promise_range, step=1):
    start, end = promise_range
    return list(range(start, end + 1, step))

def is_valid_promise(promise):
    return isinstance(promise, (int, float)) and promise >= 0

def filter_valid_promises(promises):
    return [p for p in promises if is_valid_promise(p)]