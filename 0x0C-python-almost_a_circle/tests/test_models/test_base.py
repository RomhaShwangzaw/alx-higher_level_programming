#!/usr/bin/python3
import unittest
from models.base import Base



class TestBase(unittest.TestCase):

    def setUp(self):
        self.a = Base()
        self.b = Base(12)

    def test_id_none(self):
        self.assertEqual(self.a.id, 1)

    def test_id_int(self):
        self.assertEqual(self.b.id, 12)

    def tearDown(self):
        del self.a
        del self.b
