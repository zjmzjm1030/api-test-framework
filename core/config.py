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
    """配置模型。"""
    env: str
    base_url: str
    timeout: int
    retry_times: int
    log_level: str


def load_settings(env: str = "dev") -> Settings:
    """根据环境名加载 yaml 并转成 Settings 对象。

    """
    CONFIG_PATH = CONFIG_DIR / f"{env}.yaml"
    with open(CONFIG_PATH,encoding="utf-8") as f:#safe_load() 的参数必须是文件对象或 yaml 文本内容，不是文件路径，用with 把文件打开
        cfg_data = yaml.safe_load(f)
    return Settings(**cfg_data)#**按 key 拆成一个个字段