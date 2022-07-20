import sqlite3
import unittest
from peewee import *

from app import TimelinePost, get_timeline_post

MODELS = [TimelinePost]

#using an in-memory SQLite for tests
#SQlite database connection
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        #Bind model classes to test_db. Since we have a complete list of all models, we needn't bind dependencies recursively
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        #Although this line is unecessary bc SQLite DBs only live for the duration of the connection, it's still good practice
        test_db.drop_tables(MODELS)

        #Close db connection
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello World, I\'m John!')
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane!')
        assert second_post.id == 2

        #get a list of timeline posts and assert that they are correct
        postsList = []
        for p in TimelinePost.select():
            postsList.append(p)

        for p in postsList:
            if p.id == 1:
                assert p.name == 'John Doe'
                assert p.email == 'john@example.com'
                assert p.content == 'Hello World, I\'m John!'
            if p.id == 2:
                assert p.name == 'Jane Doe'
                assert p.email == 'jane@example.com'
                assert p.content == 'Hello World, I\'m Jane!'
