# Lina Vakanas

from unittest import TestCase
from Post_Module import Post
from Reply_Module import Reply


class TestPost(TestCase):

    def setUp(self):
        self.post = Post("Author", "title", "text", False)

    def test__str__(self):
        result = self.post.__str__()
        self.assertEqual(result, "author is: {} \ntitle is: {}\n".format(self.post.author, self.post._title))

    def test_create_reply(self):
        reply = self.post.create_reply("Reply author", "Reply text", "N")
        result = reply.__str__()
        self.assertEqual(result, Reply("Reply author", "Reply text", False, self.post._title, self.post.author).__str__())