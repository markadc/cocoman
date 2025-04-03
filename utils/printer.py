from datetime import datetime


class ColorPrinter:
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"
    MAGENTA = "\033[35m"
    BLACK = "\033[30m"
    WHITE = "\033[37m"
    RESET = "\033[0m"

    def output(self, text: str, mode: str):
        print(f"{mode}{text}{self.RESET}")


class Printer(ColorPrinter):
    def now(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, text: str, mode: str):
        print(f"{mode}{self.now()}  {text}{self.RESET}")

    def add_time(self, text: str):
        return "{}  {}".format(self.now(), text)

    def red(self, text: str):
        self.output(self.add_time(text), self.RED)

    def yellow(self, text: str):
        self.output(self.add_time(text), self.YELLOW)

    def blue(self, text: str):
        self.output(self.add_time(text), self.BLUE)

    def green(self, text: str):
        self.output(self.add_time(text), self.GREEN)

    def cyan(self, text: str):
        self.output(self.add_time(text), self.CYAN)

    def gray(self, text: str):
        self.output(self.add_time(text), self.GRAY)

    def magenta(self, text: str):
        self.output(self.add_time(text), self.MAGENTA)

    def black(self, text: str):
        self.output(self.add_time(text), self.BLACK)

    def white(self, text: str):
        self.output(self.add_time(text), self.WHITE)


if __name__ == '__main__':
    p = Printer()
    p.red("红色")
    p.yellow("黄色")
    p.blue("蓝色")
    p.green("绿色")
