import asyncio
import inspect

"""
При 

"""


async def success_func():
    print(inspect.currentframe().f_code.co_name)


async def error_func1():
    func_name = inspect.currentframe().f_code.co_name
    raise ValueError(func_name)


async def error_func2():
    func_name = inspect.currentframe().f_code.co_name
    raise ValueError(func_name)


async def main_try_catch():
    try:
        await error_func1(),
    except Exception:
        print(f"catch: {error_func1.__name__}")

    try:
        await error_func2(),
    except Exception:
        print(f"catch: {error_func2.__name__}")

    try:
        await success_func(),
    except Exception:
        print(f"catch: {success_func.__name__}")


async def main_gather():
    await asyncio.gather(
        error_func1(),
        error_func2(),
        success_func(),
    )


async def main_shield():
    await asyncio.shield(success_func())
    await asyncio.shield(error_func1())
    await asyncio.shield(error_func2())


if __name__ == '__main__':
    asyncio.run(main_try_catch())
