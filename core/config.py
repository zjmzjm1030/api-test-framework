"""配置加载模块（D2 作业）。

目标：
1. 读取 config/{env}.yaml
2. 通过 pytest 命令行参数 --env=dev|test 决定加载哪个文件
3. 用 pydantic 校验配置，缺字段/类型错误时抛出可读异常
"""
from pathlib import Path

import yaml
from pydantic import BaseModel

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


class Settings(BaseModel):
    """配置模型。TODO(D2)：理解每个字段为什么需要，后续 D3 的 HttpClient 会依赖它。"""
    env: str
    base_url: str
    timeout: int
    retry_times: int
    log_level: str


def load_settings(env: str = "dev") -> Settings:
    """根据环境名加载 yaml 并转成 Settings 对象。

    TODO(D2) 自己实现：
        1. 拼出配置文件路径 CONFIG_DIR / f"{env}.yaml"
        2. 用 yaml.safe_load 读取
        3. return Settings(**data)
    """
    raise NotImplementedError("D2 作业：实现配置加载")
