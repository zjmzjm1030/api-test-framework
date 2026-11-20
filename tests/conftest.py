"""pytest 公共夹具（D5 作业）。

今晚不用动。D5 在这里实现：
- pytest_addoption：注册 --env 命令行参数（配合 D2 的配置加载）
- settings 夹具：全局唯一的配置对象
- http_client 夹具：每个测试会话复用一个 HttpClient
- post_api 夹具：用例里直接 def test_xxx(post_api) 就能用
"""
import pytest


def pytest_addoption(parser):
    # TODO(D5)：parser.addoption("--env", default="dev", choices=["dev", "test"])
    pass


@pytest.fixture(scope="session")
def settings():
    # TODO(D5)：读取 --env 参数，调用 core.config.load_settings
    raise NotImplementedError("D5 作业")


@pytest.fixture(scope="session")
def http_client(settings):
    # TODO(D5)：用 settings 构造 core.http_client.HttpClient
    raise NotImplementedError("D5 作业")


@pytest.fixture(scope="session")
def post_api(http_client):
    # TODO(D5)：from apis.post_api import PostApi，return PostApi(http_client)
    raise NotImplementedError("D5 作业")
