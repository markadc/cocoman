import time
from datetime import datetime, timedelta


class TimeHelper:
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


if __name__ == '__main__':
    th = TimeHelper()
    ts = th.today_anytime_ts(12, 0, 0)
    print(th.ts2time(ts))
    print(th.now())
    print(th.time2ts("2025-01-01 12:00:00"))
