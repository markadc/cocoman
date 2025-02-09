import os
import re
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

import cocoman

coco = cocoman.Spider()
coco.default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "Referer": "https://www.doutub.com"
}


class DoutubSpider:
    """表情包爬虫"""

    def __init__(self, keyword: str, save_dir="emos", max_page=1, speed=10):
        self.keyword = keyword
        self.save_dir = save_dir
        self.max_page = max_page
        self.speed = speed

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    def download_emo(self, one):
        name, link = one
        bdata = coco.do(link).content
        with open(os.path.join(self.save_dir, name) + ".jpg", "wb") as f:
            f.write(bdata)
        logger.success("文件 《{}》 下载成功".format(name))

    def start(self):
        tasks = []
        for i in range(self.max_page):
            url = "https://www.doutub.com/search/{}/{}".format(self.keyword, i + 1)
            res = coco.do(url)
            task = re.findall('<img alt="(.+?)" data-src="(.+?)" data', res.text, re.S)[1:]
            logger.info("从第 {} 页获取到 {} 个任务".format(i + 1, len(task)))
            tasks.extend(task)
        pool = ThreadPoolExecutor(self.speed)
        pool.map(self.download_emo, tasks)
        pool.shutdown()


if __name__ == '__main__':
    spider = DoutubSpider("哈哈", max_page=5)
    spider.start()
