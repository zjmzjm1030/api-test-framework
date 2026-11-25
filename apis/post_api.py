"""业务接口层（D4 作业）。

把 /posts 相关接口包装成语义化方法，用例层不出现 URL 和 HTTP 细节，
这就是你在 testauto2 里学过的「业务封装层」。
"""


class PostApi:
    def __init__(self, client):
        # client 是 D3 实现的 HttpClient 实例
        self.client = client

    def list_posts(self):
        """GET /posts —— TODO(D4) 实现"""
        return self.client.get("/posts")

    def get_post(self, post_id: int):
        """GET /posts/{id} —— TODO(D4) 实现"""
        return self.client.get(f"/posts/{post_id}")

    def create_post(self, title: str, body: str, user_id: int):
        """POST /posts —— TODO(D4) 实现，思考 body 用 dict 怎么传"""
        return self.client.post("/posts",json={"title": title, "body": body, "userId": user_id})

    def update_post(self, post_id: int, **fields):
        """PUT /posts/{id} —— TODO(D4) 实现"""
        return self.client.put(f"/posts/{post_id}",json=fields)

    def delete_post(self, post_id: int):
        """DELETE /posts/{id} —— TODO(D4) 实现"""
        return self.client.delete(f"/posts/{post_id}")