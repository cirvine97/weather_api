import sys
import pytest
# setting path
sys.path.append('../weather_api')
# importing
from app import get_weather
import config

def test_good_input():
    input = 'NYC'
    result = get_weather(input, config.API_key)
    assert type(result) is dict

def test_borderline_input():
    input = '    NYC '
    result = get_weather(input, config.API_key)
    assert type(result) is dict

def test_bad_input():
    input = ' ubefihwbefw222 '
    with pytest.raises(ValueError) as exception_info:
        result = get_weather(input, config.API_key)
    # Ensure the error message is right. 
    assert exception_info.match("Invalid city name")

def test_bad_API_key():
    input = 'Sydney'
    with pytest.raises(NameError) as exception_info:
        result = get_weather(input, 0)
    assert exception_info.match("Invalid API Key")