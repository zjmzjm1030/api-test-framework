"""pytest 公共夹具（D5 作业）。

D5 在这里实现：
- pytest_addoption：注册 --env 命令行参数（配合 D2 的配置加载）
- settings 夹具：全局唯一的配置对象
- http_client 夹具：每个测试会话复用一个 HttpClient
- post_api 夹具：用例里直接 def test_xxx(post_api) 就能用
"""
import pytest
from core.config import load_settings
from core.http_client import HttpClient
from apis.post_api import PostApi

def pytest_addoption(parser):
    parser.addoption(
        "--env",action="store",default="dev",help="env:dev/test"
    )
        


@pytest.fixture(scope="session")
def settings(request):
    env = request.config.getoption("--env")
    return load_settings(env)

@pytest.fixture(scope="session")
def http_client(settings):
    return HttpClient(
        settings.base_url,
        settings.timeout,
        settings.retry_times
    )


@pytest.fixture(scope="session")
def post_api(http_client):
    return PostApi(http_client)
