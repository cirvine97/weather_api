import sys
import pytest
# setting path
sys.path.append('../weather_api')
# importing
from app import get_lat_lon
import config

def test_good_input():
    input = 'London'
    result = get_lat_lon(input, config.API_key)
    expected = [51.5073219, -0.1276474]
    assert result == expected

def test_borderline_input():
    input = '    london '
    result = get_lat_lon(input, config.API_key)
    expected = [51.5073219, -0.1276474]
    assert result == expected

def test_bad_input():
    input = ' *292 ii '
    with pytest.raises(ValueError) as exception_info:
        get_lat_lon(input, config.API_key)
    # Ensure the error message is right. 
    assert exception_info.match("Invalid city name")

def test_bad_API_key():
    input = 'New York City'
    with pytest.raises(NameError) as exception_info:
        get_lat_lon(input, 0)
    assert exception_info.match("Invalid API Key")