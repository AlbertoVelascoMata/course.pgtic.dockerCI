
from . import BaseTestClass

class SensorsTestClass(BaseTestClass):
    def test_sensors_get(self):
        result = self.client.get('/sensors')
        self.assertEqual(200, result.status_code)
        self.assertIsInstance(result.json, dict)

    def test_sensors_post_defaults(self):
        result = self.client.post('/sensors')
        self.assertEqual(200, result.status_code)
        self.assertIsInstance(result.json, dict)
        self.assertIn('name', result.json)
        self.assertIn('version', result.json)

    def test_sensors_post_info(self):
        result = self.client.post('/sensors?name=TestName&version=3.0')
        self.assertEqual(200, result.status_code)
        self.assertIsInstance(result.json, dict)
        self.assertIn('name', result.json)
        self.assertEqual(result.json['name'], 'TestName')
        self.assertIn('version', result.json)
        self.assertEqual(result.json['version'], '3.0')
    
    def test_sensors_created(self):
        result = self.client.post('/sensors?name=TestSensor&version=3.0')
        self.assertEqual(201, result.status_code)

        result = self.client.get('/sensors')
        self.assertIsInstance(result.json, dict)
        self.assertIn({'name': 'TestSensor', 'version': '3.0'}, result.json.values())

