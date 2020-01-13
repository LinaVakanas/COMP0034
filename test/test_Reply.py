# Mahdi

from unittest import TestCase
from Reply_Module import Reply

class TestReply(TestCase):

    #Part 1: Setup
    def setUp(self):
        self.reply = Reply("Author", "Text", False, "Parent title", "Parent author")

    #Part 2: Call object

    def test_check_length(self):
        result = self.reply.check_length()

    #Part 3: assertion

    def test__str__(self):
        result = self.reply.__str__()
        self.assertEqual(result, "{} is replying to {}\n".format(self.reply.author, self.reply.parent_author))