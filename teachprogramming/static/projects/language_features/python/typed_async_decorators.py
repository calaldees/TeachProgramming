import asyncio

#from typing import Awaitable, Callable, ParamSpec, TypeVar
from typing import Awaitable
from collections.abc import Callable
import logging


def decorator[T,**P](fn: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    async def decorated(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{fn.__name__} was called')
        return await fn(*args, **kwargs)

    return decorated


@decorator
async def add_two(x: float, y: float) -> float:
    '''Add two numbers together.'''
    return x + y


async def main():
    print(await add_two(1, 2))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())