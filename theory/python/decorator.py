import asyncio


def decorator(func):
    """
    sync decorator
    """

    def wrapper(*args, **kwargs):
        print("decorator")
        result = func(*args, **kwargs)
        return result

    return wrapper


def async_decorator(async_func):
    """
    python decorator
    """

    async def wrapper(*args, **kwargs):
        print("python decorator")
        result = await async_func(*args, **kwargs)
        return result

    return wrapper


def decorator_with_param(param):
    """
    sync decorator with param
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"decorator with param: {param}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def async_decorator_with_param(param):
    """
    python decorator with param
    """

    def decorator(async_func):
        async def wrapper(*args, **kwargs):
            print(f"python decorator with param: {param}")
            result = await async_func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@decorator
def my_func(a, b):
    return a + b


@async_decorator
async def my_async_func(a, b):
    return a + b


@decorator_with_param("PARAM")
def my_func_with_param(a, b):
    return a + b


@async_decorator_with_param("PARAM")
async def my_async_func_with_param(a, b):
    return a + b


if __name__ == '__main__':
    assert 2 == my_func(1, 1)
    assert 2 == asyncio.run(my_async_func(1, 1))
    assert 2 == my_func_with_param(1, 1)
    assert 2 == asyncio.run(my_async_func_with_param(1, 1))
