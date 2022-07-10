import unittest
from peewee import *

from app import TimelinePost, get_time_line_post

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        # Get timeline posts and assert that they are correct
        for p in TimelinePost:
            if p.id == 1:
                assert p.name == 'John Doe'
                assert p.email == 'john@example.com'
                assert p.content == 'Hello world, I\'m John!'
            elif p.id == 2:
                assert p.name == 'Jane Doe'
                assert  p.email == 'jane@example.com'
                assert p.content =='Hello world, I\'m Jane!' 
            else:
                pass
    