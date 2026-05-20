from datetime import datetime


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {datetime.now()} - {func.__name__} was called")
        return func(*args, **kwargs)
    return wrapper