"""D1 验收用例：只验证本地环境，不发网络请求，今晚必须全部通过。"""
import pytest
import requests
import yaml


@pytest.mark.smoke
def test_python_runs():
    """证明 pytest 本身工作正常。"""
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_dependencies_importable():
    """证明 requirements.txt 里的依赖都装好了。"""
    assert requests.__version__
    assert yaml.safe_load("a: 1") == {"a": 1}


@pytest.mark.smoke
def test_project_structure():
    """证明目录骨架完整。"""
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    expected = [
        "config/dev.yaml",
        "config/test.yaml",
        "core/config.py",
        "core/http_client.py",
        "apis/post_api.py",
        "tests/conftest.py",
        "requirements.txt",
        "pytest.ini",
    ]
    missing = [p for p in expected if not (root / p).exists()]
    assert not missing, f"缺少文件：{missing}"
