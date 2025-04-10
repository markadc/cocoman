import time
from datetime import datetime, timedelta


class TimeConvert:
    @staticmethod
    def ts2time(ts: float) -> str:
        """时间戳转时间"""
        date_fmt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))
        return date_fmt

    @staticmethod
    def time2ts(date_fmt: str) -> int:
        """时间转时间戳"""
        ts = time.mktime(time.strptime(date_fmt, "%Y-%m-%d %H:%M:%S"))
        return int(ts)

    @staticmethod
    def today_anytime_ts(hour: int, minute: int, second=0) -> float:
        """获取今天任意时刻的时间戳"""
        now = datetime.now()
        today_0 = now - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        today_anytime = today_0 + timedelta(hours=hour, minutes=minute, seconds=second)
        ts = today_anytime.timestamp()
        return ts

    @staticmethod
    def now():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Timer:
    def __init__(self, desc: str):
        self.desc = desc

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.end_time = time.time()
        print(f"{self.desc}: cons {self.end_time - self.start_time:.2f} sec")


if __name__ == '__main__':
    t = TimeConvert()
    ts = t.today_anytime_ts(12, 0, 0)
    print(t.ts2time(ts))
    print(t.now())
    print(t.time2ts("2025-01-01 12:00:00"))

    with Timer("计时器-1"):
        lis = [i for i in range(1000000)]

    with Timer("计时器-2"):
        lis2 = []
        for i in range(1000000):
            lis2.append(i)
