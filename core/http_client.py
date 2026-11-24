"""统一 HTTP 客户端（D3 作业，整个框架最核心的文件）。

职责：
- 封装 requests.Session，对上层只暴露 get/post/put/delete 语义化方法
- 统一处理：base_url 拼接、超时、默认 header、鉴权、重试、请求/响应日志
- 用例层永远不直接 import requests，只通过这里发请求
"""
import requests


class HttpClient:
    def __init__(self, base_url: str, timeout: int = 10, retry_times: int = 0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retry_times = retry_times
        self.session = requests.Session()

    def request(self, method: str, path: str, **kwargs):
        for attempt in range(self.retry_times + 1):
            try:
                return self.session.request(method, self.base_url + path, timeout=self.timeout, **kwargs)
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                if attempt == self.retry_times:   # 已经是最后一轮
                    raise
                print(f"第{attempt+1}次尝试失败，准备重试")

    # TODO(D3)：用 request() 包装出 get/post/put/delete 四个方法
    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)
