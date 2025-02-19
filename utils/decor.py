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
            err = None
            for i in range(times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error("{} => {}".format(e, func_name))
                    time.sleep(rest)
                    err = e
            if is_raise:
                raise MaxRetryError("{} => {}".format(err, func_name))
            logger.critical("重试也失败 => {}".format(func_name))
            return failed

        return inner

    return outer
