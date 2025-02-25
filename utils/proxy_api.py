import random
import time
from abc import ABC, abstractmethod

from cocoman.utils.log import Log

log = Log()

currts = lambda: time.time()


class ProxyAPI(ABC):
    """每次获取一个代理"""

    def __init__(self, interval=10):
        self.proxies = None
        self.latest_time = None
        self.rest = interval

    @abstractmethod
    def get_proxy(self):
        pass

    def update_proxies(self):
        proxy = self.get_proxy()
        self.proxies = {"http": proxy, "https": proxy}
        self.latest_time = currts()
        log.debug("代理更新成功")

    def get_one(self):
        if self.latest_time is None:
            self.update_proxies()
            return self.proxies
        if currts() - self.latest_time > self.rest:
            self.update_proxies()
            return self.proxies
        else:
            return self.proxies


if __name__ == '__main__':
    class DemoProxyAPI(ProxyAPI):
        def get_proxy(self):
            return "{:.2f}".format(random.uniform(1, 100))


    demo = DemoProxyAPI(interval=3)
    while True:
        ip = demo.get_one()
        print("代理 => {}".format(ip))
        time.sleep(1)
