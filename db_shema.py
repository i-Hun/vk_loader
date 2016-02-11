from mongoengine import *
import vk
import time

vk.logger.setLevel('DEBUG')

session = vk.AuthSession(access_token="a99700af7dba22bc9d6224959a879db1382663867a132f6fa066123461ef714b48e9f3f92aac316fa9e77")
api = vk.API(session, v='5.35', lang='ru', timeout=1000)

def loadUser(user_id):
    return api.users.get(user_ids=user_id, fields=["first_name", "last_name", "deactivated",
                                             "verified", "sex", "bdate", "city", "country", "home_town",
                                             "photo_100", "education", "universities", "schools", "status", "last_seen",
                                             "followers_count", "counters"])

default_sleep = 0.25
with open("4_1_876.txt", "rt") as txt_ids:
    lines = txt_ids.readlines()
    for num, line in enumerate(lines):
        print(num)

        time.sleep(default_sleep)
        print(loadUser(line.rstrip()))



class User(Document):
    user_id = IntField(required=True)
    first_name = StringField()
    last_name = StringField()
    screen_name = StringField()
    sex = IntField()
    birth_date = DateTimeField()
    city = StringField()
    region = StringField()
    country = StringField()
    posts_count = IntField()
    comments_count = IntField(required=True)
    likes_count = IntField(required=True)
    recieved_comments_count = IntField(required=True)
    recieved_likes_count = IntField(required=True)
    recieved_comments_likes_count = IntField(required=True)
    mobile_phone = IntField(required=True)
    home_site = StringField(max_length=1000)
    univ = StringField(max_length=1000)
    faculty = StringField(max_length=1000)
    edu = StringField(max_length=1000)
    edu_status = StringField(max_length=1000)  #?
    friends_counts = IntField(required=True)
    groups_count = IntField(required=True)
    followers_count = IntField(required=True)
    timezone = StringField(max_length=1000)
    photo = StringField(max_length=1000)


class Comment(EmbeddedDocument):
    comment_id = IntField(required=True)
    authid = ReferenceField(User, required=True)
    from_id = ReferenceField(User, required=True)
    author_post = ReferenceField(User, required=True)
    date = DateTimeField(required=True)
    text = StringField()
    likes_count = IntField(required=True)
    likers = ListField(ReferenceField(User))


class Post(Document):
    post_id = IntField(required=True)
    owner_id = ReferenceField(User, required=True)  # идентификатор владельца стены, на которой размещена запись
    from_id = ReferenceField(User, required=True)  # идентификатор автора записи
    date = DateTimeField(required=True)  # время публикации записи в формате unixtime
    text = StringField()
    posts_count = IntField(required=True)
    reposts_count = IntField(required=True)
    likes_count = IntField(required=True)
    likers = ListField(ReferenceField(User))
    link_url = StringField()
    link_title = StringField()
    link_description = StringField()
    copy_owner = ReferenceField(User)  # идентификатор владельца стены, у которого была скопирована запись (если запись является копией записи с чужой стены).
    copy_text = StringField()  # текст комментария, добавленного при копировании (если запись является копией записи с чужой стены).
    comments = ListField(EmbeddedDocumentField(Comment))


