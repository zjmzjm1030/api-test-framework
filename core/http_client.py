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
        # TODO(D3)：初始化 requests.Session()，思考为什么用 Session 而不是每次 requests.get
        self.session = None

    def request(self, method: str, path: str, **kwargs):
        """统一请求入口。

        TODO(D3) 自己实现：
            1. url = self.base_url + path
            2. 注入 timeout
            3. 发送请求，捕获超时/连接异常并按 retry_times 重试
            4. 打印请求方法、URL、状态码、耗时（这就是 D6 报告附件的素材）
            5. 返回 response 对象
        """
        raise NotImplementedError("D3 作业：实现统一请求与重试")

    # TODO(D3)：用 request() 包装出 get/post/put/delete 四个方法
    def get(self, path, **kwargs):
        raise NotImplementedError

    def post(self, path, **kwargs):
        raise NotImplementedError

    def put(self, path, **kwargs):
        raise NotImplementedError

    def delete(self, path, **kwargs):
        raise NotImplementedError
