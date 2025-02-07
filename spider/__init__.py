import requests

from cocoman.spider.response import SelectorResponse
from cocoman.utils import *


class Spider:
    def __init__(self, keep=False):
        self.default_headers = {}
        self.default_proxies = {}
        self.default_timeout = None
        self.enable_random_ua = True
        self.enable_extra_headers = True
        self.extra_headers = {}
        self.client = requests.Session() if keep else requests
        self.raise_request_error = True

    def get_headers(self):
        headers = {"User-Agent": gen_random_ua()} if not self.default_headers and self.enable_random_ua else self.default_headers
        return headers

    def get_proxies(self):
        return self.default_proxies

    def get_timeout(self):
        return self.default_timeout

    def add_extra_headers(self, headers: dict):
        """为headers补充额外的字段"""
        for k, v in self.extra_headers.items():
            headers.setdefault(k, v)

    @staticmethod
    def elog(url: str, e: Exception, times: int):
        logger.error(
            """
            URL         {}
            ERROR       {}
            TIMES       {}
            """.format(url, e, times)
        )

    def do(self, url: str, params: dict = None, headers: dict = None, data: dict | str = None, json: dict = None, proxies: dict = None, timeout: int | float = None, retry=2, rest=1, raise_request_error=None, **kwargs) -> SelectorResponse:
        """默认为GET请求，传递了data或者json参数则为POST请求，自带重试"""
        for i in range(retry + 1):
            headers = self.get_headers() if headers is None else headers
            proxies = self.get_proxies() if proxies is None else proxies
            timeout = self.get_timeout() if timeout is None else timeout
            if self.enable_extra_headers:
                self.add_extra_headers(headers)
            same = dict(params=params, headers=headers, proxies=proxies, timeout=timeout, **kwargs)
            try:
                response = self.client.get(url, **same) if data is None and json is None else self.client.post(url, data=data, json=json, **same)
                return SelectorResponse(response)
            except Exception as e:
                self.elog(url, e, i + 1)
                time.sleep(rest)

        if raise_request_error:
            raise MaxRetryError(url)
        if raise_request_error is None and self.raise_request_error:
            raise MaxRetryError(url)
