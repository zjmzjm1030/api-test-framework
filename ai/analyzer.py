"""AI 失败归因模块（D7 作业，本项目的差异化亮点）。

设计思路：
- 用例失败时，把失败上下文（请求 URL、状态码、响应体、断言信息）发给大模型
- 让模型归类根因：环境问题 / 用例数据问题 / 疑似真实 Bug / 框架问题
- 结论写进 Allure 报告，体现「大模型 API 工程化调用」完整链路
"""
import os
import requests

class FailureAnalyzer:
    def __init__(self, api_key: str | None = None, model: str = "deepseek-flash"):
        # 密钥只从环境变量读，绝不硬编码——这是面试必考点
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        self.model = model

    def analyze(self, failure_context: dict) -> str:
        """对一次失败做根因归因。

        TODO(D7) 自己实现：
            1. 校验 api_key 存在，缺失时降级返回「AI 归因跳过：未配置 LLM_API_KEY」
            2. 构造 prompt：system 规定只输出四类标签 + 一句话理由
            3. 调用 Chat Completions 接口（requests POST，不要用 SDK，更能展示基本功）
            4. 处理超时、非 200、限流 429 三类异常，保证 AI 挂了不影响主测试流程
            5. 返回模型文本结论
        """
        if not self.api_key:
            return "AI 归因跳过：未配置 LLM_API_KEY"
        system_prompt = "你是一个测试失败归因助手，只能输出四类之一：环境问题/用例数据问题/疑似真实Bug/框架问题，并附一句话理由"    
        user_prompt = f"请分析这次失败：{failure_context}"
        messages = [
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_prompt}
        ]
        
        try:
            resp = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.api_key}",
                },
            json={
                "model":self.model,
                "messages":messages
            },
        timeout=30,
        )
            if resp.status_code == 429:
                return f"AI 归因限流，跳过"
            elif resp.status_code != 200:
                return f"AI归因失败http{resp.status_code}"
            return resp.json()["choices"][0]["message"]["content"]
        except requests.exceptions.Timeout:
            return f"AI归因超时,跳过"
        except requests.exceptions.ConnectionError:
            return f"AI链接不上,跳过"
        except Exception as e:
            return f"AI 归因异常：{e}"
        
            