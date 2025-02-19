from cocoman import Spider
from cocoman.utils import retry, pv

s = Spider()


@retry(is_raise=False)
def demo1():
    return 1 / 0


@retry(times=1, rest=0)
def demo2():
    return 1 / 0


if __name__ == '__main__':
    v1 = demo1()
    pv(v1)
    v2 = demo2()
    pv(v2)
