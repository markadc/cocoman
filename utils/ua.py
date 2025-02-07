
import random


def _gen_os() -> str:
    """生成一个随机的操作系统"""
    os_choices = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 6.1; WOW64",
        "Macintosh; Intel Mac OS X 10_15_6",
        "X11; Linux x86_64",
        "Windows NT 6.3; Trident/7.0",
    ]
    return random.choice(os_choices)


def _gen_browser() -> str:
    """生成一个随机的浏览器类型和版本"""
    browser_choices = [
        ("Chrome", random.randint(70, 100)),
        ("Firefox", random.randint(70, 100)),
        ("Edge", random.randint(80, 100)),
        ("Safari", random.randint(10, 14)),
        ("Opera", random.randint(60, 80)),
    ]
    browser, version = random.choice(browser_choices)
    return f"{browser}/{version}.0"


def gen_random_ua() -> str:
    """生成一个随机的UA"""
    os, browser = _gen_os(), _gen_browser()
    ua = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) {browser} Safari/537.36"
    return ua
