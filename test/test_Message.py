# Duc Tung Le
# video demonstration

from unittest import TestCase
from Message import Message

class TestMessage(TestCase):

    #Setup
    def setUp(self):
        self.message = Message("Mentee","mentor","Hello",False,"1/1/2019")

    #Call Object
    def test_check_length(self):
        result = self.message.length_check()

   #Assertion
    def test_attachment(self):
        result = self.message.__str__()
        self.assertEqual(result,"You have no attachment in the message")