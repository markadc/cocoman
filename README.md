# 安装

```bash
pip install cocoman
```

# 使用

## 演示

### 发送GET请求

- do 方法默认是 GET 请求

```python
from cocoman import Spider

s = Spider()
url = "https://www.baidu.com"
res = s.do(url)  # 发送 GET 请求，默认自带ua
title = res.xpath("//title/text()").get()
print(title)
```

### 发送POST请求

- do方法传递了 data 或者 json 参数则是 POST 请求

```python
from pprint import pprint

from cocoman import Spider

s = Spider()

api = "https://httpbin.org/post"
form_data = {"type": "请求表单"}
res = s.do(api, data=form_data)
pprint(res.json())

json_body = {"type": "JSON请求体"}
res = s.do(api, json=json_body)
pprint(res.json())

```