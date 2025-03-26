class DictConvertObject:
    """
    dict 转换为对象
    object.name 等同于 dict["name"]
    """

    def __init__(self, src: dict):
        self._src = src

    def __getattr__(self, key):
        if key in self._src:
            value = self._src[key]
            if isinstance(value, dict):
                return DictConvertObject(value)
            elif isinstance(value, list):
                return [DictConvertObject(v) if isinstance(v, dict) else v for v in value]
            return value
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")


def test():
    src = {
        "data": {
            "list": [
                {
                    "name": "Thomas",
                    "age": 55,
                    "other": [
                        {
                            "mark": "记号"
                        }
                    ]
                },
                {
                    "name": "Mark",
                    "age": 22
                }
            ]
        },
        "status": 0,
        "code": 200
    }
    data = DictConvertObject(src)
    print(data.data.list[1].name)
    print(data.data.list[0].other[0].mark)
    print(data.status)
    print(data.code)


if __name__ == '__main__':
    test()
