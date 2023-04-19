from utils.api_utils import APIUtils
import unittest
from datetime import datetime
import re

class TestAPIWeather(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_utils = APIUtils()

    def test_validate_negative_weather_date(self):
        content = self.api_utils.get_weather(latitude="FFF", longitude=30.7411902151, expected_code=400)

    def test_validate_weather_date(self):
        content = self.api_utils.get_weather(latitude=46.486, longitude=30.7411902151)

        date_time = content['realtimeWeather']['items'][0]['date']
        current_date = str(datetime.now())
        response_date = re.findall(r'(.*)T', date_time) [0]
        current_date_time = re.findall(r'(.*)\s', current_date)[0]
        assert response_date == current_date_time, f"Current date: {response_date} doesn't match with expected: {current_date_time}"

#latitude=46.486, longitude=30.7411902151