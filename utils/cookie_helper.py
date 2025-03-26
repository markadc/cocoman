import re


class CookieHelper:
    def __init__(self, cookie: str | dict):
        assert isinstance(cookie, (str, dict)), "Cookie must be str or dict"
        if isinstance(cookie, str):
            self.cookie_str = cookie
            self.cookie_dict = self.cookie_to_dict(cookie)
        else:
            self.cookie_str = self.cookie_to_str(cookie)
            self.cookie_dict = cookie

    @staticmethod
    def cookie_to_str(cookie: dict) -> str:
        """Cookie 转换为 str 类型"""
        cookie_str = ""
        for key, value in cookie.items():
            cookie_str += "{}={}; ".format(key, value)
        return cookie_str.rstrip("; ")

    @staticmethod
    def cookie_to_dict(cookie: str) -> dict:
        """Cookie 转换为 dict 类型"""
        cookie = cookie.rstrip().rstrip(";")
        cookie_dict = {kv.split("=")[0]: kv.split("=")[1] for kv in cookie.split("; ")}
        return cookie_dict

    def get_value(self, key: str) -> str:
        """获取 Cookie 中某个字段的值"""
        rule = key + "=([^;]+)"
        match = re.search(rule, self.cookie_str)
        return match.group(1)

    def remove_value(self, key: str) -> str:
        """删除 Cookie 中某个字段，然后返回新的 Cookie"""
        self.cookie_dict.pop(key)
        self.cookie_str = self.cookie_to_str(self.cookie_dict)
        return self.cookie_str
