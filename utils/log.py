from datetime import datetime

now = lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")

codes = {
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
    "light_white": "97"
}

log_priority = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "SUCCESS": 4
}

color_level = {
    "blue": "DEBUG",
    "yellow": "WARNING",
    None: "INFO",
    "red": "ERROR",
    "green": "SUCCESS",
}


class Log:
    def __init__(self, level="DEBUG"):
        self.level = level

    def debug(self, msg):
        self.print_color(msg, "blue")

    def info(self, msg):
        self.print_color(msg)

    def warning(self, msg):
        self.print_color(msg, "yellow")

    def error(self, msg):
        self.print_color(msg, "red")

    def success(self, msg):
        self.print_color(msg, "green")

    def print_color(self, content, color=None):
        """带颜色的打印"""
        level = color_level.get(color)
        if log_priority.get(level) < log_priority.get(self.level):
            return
        code = codes.get(color)
        if code:
            print("\033[{}m{}  {}\033[0m".format(code, now(), content))
        else:
            print(f"{now()}  {content}")


if __name__ == '__main__':
    log = Log(level="WARNING")
    log.debug("hello")
    log.info("hello")
    log.warning("hello")
    log.error("hello")
    log.success("hello")
