
import unittest

from src.app import create_app

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
