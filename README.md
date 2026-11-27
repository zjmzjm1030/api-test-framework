# api-test-framework

从零搭建的接口自动化测试框架（10 天冲刺项目）。

- 被测系统：[JSONPlaceholder](https://jsonplaceholder.typicode.com)（免费公开 REST API）
- 技术栈：pytest + requests + PyYAML + pydantic + Allure + GitHub Actions + DeepSeek（AI 失败归因）

## 架构分层

```
tests/   用例层：只写"调哪个接口、断言什么"
  ↓
apis/    业务封装层：接口语义化（PostApi.list_posts ...）
  ↓
core/    能力层：HttpClient（超时/重试/日志）、配置加载
  ↓
requests 最底层：真正发 HTTP 请求
ai/      横切能力：失败用例的大模型根因归因
```

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                            # D1 验收：3 条 smoke 用例全绿
```

## 进度看板

- [X] D1 项目骨架 + 本地环境
- [x] D2 多环境配置（`--env` 切换 + pydantic 校验）
- [x] D3 HttpClient（超时/重试/统一日志）
- [x] D4 业务接口层 + 第一条 CRUD 用例
- [x] D5 全局fixture + 数据驱动+用例重构
- [x] D6 Allure 报告 + 失败重跑
- [x] D7 AI 失败归因（调用DEEPSEEK的API分析）
- [x] D8 失败自动触发AI归因+写入Allure报告
- [x]  GitHub Actions CI
- [ ] D9 README 完善 + 模拟面试
- [ ] D10 缓冲 / 简历项目段落定稿

## 设计取舍（D9 前补全，面试重点）

- 为什么重试逻辑放在 HttpClient 而不是用例层？
- 密钥为什么只走环境变量，不允许写进配置文件？
- AI 归因失败时为什么必须降级、不能阻塞主测试流程？
