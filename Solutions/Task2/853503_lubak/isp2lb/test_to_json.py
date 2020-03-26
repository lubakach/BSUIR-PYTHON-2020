from unittest import TestCase
from isp2lb import to_json


class Test(TestCase):
    def test_to_json(self):
        ellie = to_json.Model()
        ellie.name = "Ellie"
        ellie.surname = "Bill"
        ellie.height = 180.2

        self.assertEqual(to_json.to_json(ellie), '{"name": "Ellie"  "surname": "Bill"  "height": 180.2  }')

    def test_wrong_to_json(self):
        ellie = to_json.Model()
        ellie.name = "Ellie"
        ellie.surname = "18"
        ellie.height = "hi"
        self.assertNotEqual(to_json.to_json(ellie), '{"name": "Ellie"  "surname": 18  "height": "Hello"}')
