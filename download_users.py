import requests
import json
import vk
import math

token = "ptHdPeZ6hDVcqGwjcaeV"
userid = 18779389

session = vk.AuthSession(app_id="5163341", user_login="i.hun@ya.ru", user_password="Pshzyjdcr2")
api = vk.API(session)

user_fields = ["uid", "first_name", "last_name", "nickname", "sex", "bdate", "city", "country", "timezone", "photo", "photo_medium", "photo_big", "photo_rec", "contacts", "education", "connections"]

user = api.users.get(uids=userid, fields=user_fields)


def get_wall(userid):
    posts_list = []
    initial_posts = api.wall.get(owner_id=userid, count=100)
    posts_count = initial_posts[0]
    for post in initial_posts[1:]:
        posts_list.append(post)
    if posts_count > 100:
        offset = math.ceil(posts_count / 100)
        for i in range(1, offset):
            print(offset)
            posts = api.wall.get(owner_id=userid, count=100, offset=i*100)[1:]
            for post in posts:
                posts_list.append(post)
    return posts_list


def get_wall_execute(userid):
    code = 'return {'




print(len(get_wall(userid)))


