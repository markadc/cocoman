import time
from functools import wraps

from loguru import logger

from cocoman.spider.errors import MaxRetryError


def retry(times=2, rest=1, is_raise=True, failed=None):
    """重试（当函数异常时，触发重试）"""

    def outer(func):
        func_name = func.__name__

        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error("{} => {}".format(e, func_name))
                    if i == times:
                        if is_raise:
                            raise MaxRetryError("{}. {}".format(e, func_name))
                        break
                    time.sleep(rest)

            logger.critical("Trying again also failed. {}".format(func_name))
            return failed

        return inner

    return outer


if __name__ == '__main__':
    @retry(3, 1, is_raise=True)
    def test():
        return 1 / 0


    test()
