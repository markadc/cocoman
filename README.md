# 安装

```bash
pip install cocoman
```

# 使用

- 简单演示

```python
from cocoman import Spider

s = Spider()
url = "https://www.baidu.com"
res = s.do(url)
title = res.xpath("//title/text()").get()
print(title)
```