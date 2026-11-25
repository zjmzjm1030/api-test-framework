import pytest 
from core.http_client import HttpClient
from apis.post_api import PostApi


client = HttpClient("https://jsonplaceholder.typicode.com",timeout=30, retry_times=2)
api = PostApi(client)

def test_list_posts():
    resp = api.list_posts()
    assert resp.status_code == 200
    assert len(resp.json())>0

def test_get_post():
    resp = api.get_post(1)
    assert resp.status_code == 200
    assert resp.json()["id"] == 1

def test_create_post():
    resp = api.create_post(title="测试标题",body="测试内容",userId=1)
    assert resp.status_code == 201
    assert resp.json()["title"]=="测试标题"
    assert resp.json()["userId"]==1

def test_update_post():
    resp = api.update_post(1,title="新标题",body="新内容")
    assert resp.status_code == 200
    assert resp.json()["title"] == "新标题"
    assert resp.json()["body"] == "新内容"

def test_delete_post():
    resp =  api.delete_post(1)
    assert resp.status_code ==200
    