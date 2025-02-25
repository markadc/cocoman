import base64
import ctypes
import hashlib
import inspect
import json
import os
import random
import re
import string
import time
import uuid
from concurrent.futures import as_completed
from datetime import datetime, timedelta
from threading import Thread

from loguru import logger


def pv(*args, newline=True, sep="    ", rstrip=True):
    """打印变量的名称、值"""
    frame = inspect.currentframe().f_back
    vars = frame.f_locals
    s = ""
    for name, value in vars.items():
        if value in args:
            tail = "\n" if newline else sep
            part = f"{name}: {value!r}{tail}"
            s += part
    print(s.rstrip() if rstrip else s)


def ts2time(ts: float) -> str:
    """时间戳转时间"""
    date_fmt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))
    return date_fmt


def time2ts(date_fmt: str) -> int:
    """时间转时间戳"""
    ts = time.mktime(time.strptime(date_fmt, "%Y-%m-%d %H:%M:%S"))
    return int(ts)


def today_anytime_ts(hour: int, minute: int, second=0) -> float:
    """获取今天任意时刻的时间戳"""
    now = datetime.now()
    today_0 = now - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
    today_anytime = today_0 + timedelta(hours=hour, minutes=minute, seconds=second)
    ts = today_anytime.timestamp()
    return ts


def timef(ts: int | float) -> str:
    """时间戳（秒）转时间"""
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def wlog(msg: str, show: bool):
    if show:
        logger.warning(msg)


def nget(data: dict, *args, log=False, default=None):
    """字典多层取值，KEY不存在则返回<default>"""
    temp = data
    for i, a in enumerate(args):
        if a not in temp:
            wlog(f"KEY {a!r} miss", log)
            return default
        temp = temp.get(a)
        if i == len(args) - 1:
            return temp
        if not isinstance(temp, dict):
            wlog(f"KEY {a!r} VALUE {temp!r} not is dict", log)
            return default
    return temp


def kill_thread(thread: Thread):
    """强制杀死线程"""
    tid = thread.ident
    exctype = SystemExit
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))


def get_results(fs: list, timeout: int | float = None):
    """处理线程任务，有序获取（先返回的靠前）所有线程的返回值（异常的线程、假值除外）"""
    results = []
    try:
        for v in as_completed(fs, timeout=timeout):
            try:
                result = v.result()
                if result:
                    results.append(result)
            except Exception as e:
                logger.error(e)
    except Exception as e:
        logger.error(e)
    return results


now = lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")

color_codes = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "gray": "90",
    "light_red": "91",
    "light_green": "92",
    "light_yellow": "93",
    "light_blue": "94",
    "light_magenta": "95",
    "light_cyan": "96",
    "light_white": "97",
}


def print_color(content, color=None):
    """带颜色的打印"""
    code = color_codes.get(color)
    if code:
        print("\033[{}m{}  {}\033[0m".format(code, now(), content))
    else:
        print(f"{now()}  {content}")


def lprint(content, all_add_color=True, color=None):
    code = color_codes.get(color)
    if code:
        if all_add_color is True:
            print("\033[{}m{}  {}\033[0m".format(code, now(), content))
        else:
            print("\033[{}m{}\033[0m  {}".format(code, now(), content))
    else:
        print(f"{now()}  {content}")


def jsonp2json(jsonp: str):
    """jsonp转换为json"""
    data: dict = json.loads(re.match(".*?({.*}).*", jsonp, re.S).group(1))
    return data


def get_uuid():
    """获取uuid"""
    uuid4 = str(uuid.uuid4())
    return uuid4


def b64_encode(s: str):
    """base64加密"""
    encode_value = base64.b64encode(s.encode("utf-8")).decode("utf-8")
    return encode_value


def b64_decode(s: str):
    """base64解密"""
    decode_value = base64.b64decode(s).decode("utf-8")
    return decode_value


def rand_str(leng=9):
    """获取随机字符串，a-zA-Z0-9"""
    s = "".join(random.sample(string.ascii_letters + string.digits, leng))
    return s


def make_md5(src: str | bytes, *args: str) -> str:
    """获取md5"""
    hasher = hashlib.md5()
    data = src if isinstance(src, bytes) else src.encode("utf-8")
    hasher.update(data)
    for arg in args:
        hasher.update(str(arg).encode("utf-8"))
    md5_value = hasher.hexdigest()
    return md5_value


def current_timestamp(is_int=True):
    """当前时间戳"""
    now = time.time()
    return int(now) if is_int else now


def current_time():
    """当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_date():
    """当前日期"""
    return datetime.now().strftime("%Y-%m-%d")


def cookie_to_str(cookie: dict) -> str:
    """Cookie转换为str类型"""
    cookie_str = ""
    for key, value in cookie.items():
        cookie_str += "{}={}; ".format(key, value)
    return cookie_str.rstrip("; ")


def cookie_to_dict(cookie: str) -> dict:
    """Cookie转换为dict类型"""
    cookie_dict = {kv.split("=")[0]: kv.split("=")[1] for kv in cookie.split("; ")}
    return cookie_dict


def save_file(path: str, content: str | bytes, encoding="UTF-8"):
    """保存文件"""
    mode = "wb" if isinstance(content, bytes) else "w"
    p_dir = os.path.dirname(os.path.abspath(path))
    if not os.path.exists(p_dir):
        os.makedirs(p_dir)
    with open(path, mode, encoding=None if mode == "wb" else encoding) as f:
        f.write(content)


if __name__ == '__main__':
    msg = "猜猜我是谁"

    lprint(msg)

    lprint(msg, color="red")
    lprint(msg, color="yellow")
    lprint(msg, color="blue")

    lprint(msg, all_add_color=False, color="red")
    lprint(msg, all_add_color=False, color="yellow")
    lprint(msg, all_add_color=False, color="blue")
