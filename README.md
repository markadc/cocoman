# 安装

```bash
pip install cocoman
```

# 使用

## 演示

### do 方法

- 参数跟 `requests` 的参数保持一致
- 默认自带`重试`、`ua`
- 请求失败时，可以通过 `raise_request_error` 参数选择不抛出异常

### 发送GET请求

- do 方法默认是 GET 请求，默认自带ua

```python
from cocoman import Spider

coco = Spider()
url = "https://www.baidu.com"
res = coco.do(url)
title = res.xpath("//title/text()").get()
print(title)
```

### 发送POST请求

- do 方法传递了 data 或者 json 参数则是 POST 请求

```python
from pprint import pprint

from cocoman import Spider

coco = Spider()

api = "https://httpbin.org/post"
form_data = {"type": "请求表单"}
res = coco.do(api, data=form_data)
pprint(res.json())

json_body = {"type": "JSON请求体"}
res = coco.do(api, json=json_body)
pprint(res.json())
```