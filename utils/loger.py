from cocoman.utils.func import print_color


class Log:
    def debug(self, msg):
        print_color(msg, "blue")

    def info(self, msg):
        print_color(msg)

    def warning(self, msg):
        print_color(msg, "yellow")

    def error(self, msg):
        print_color(msg, "red")

    def success(self, msg):
        print_color(msg, "green")
