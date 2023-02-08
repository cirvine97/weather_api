import sys
import pytest
# setting path
sys.path.append('../weather_api')
# importing
from app import surfaced_values
import config
import json

def test_good_input():
    input = 'Edinburgh'
    result = surfaced_values(input,
                            config.API_key,
                            config.temperature_unit)
    result = json.loads(result)
    assert len(result) == 3

def test_borderline_input():
    input = '    edinburgh '
    result = surfaced_values(input,
                             config.API_key,
                             config.temperature_unit)
    result = json.loads(result)
    assert len(result) == 3

def test_bad_input():
    input = ' &^829 '
    with pytest.raises(ValueError) as exception_info:
        surfaced_values(input,
                        config.API_key,
                        config.temperature_unit)
    # Ensure the error message is right. 
    assert exception_info.match("Invalid city name")

def test_bad_API_key():
    input = 'Edinburgh'
    with pytest.raises(NameError) as exception_info:
        surfaced_values(input,
                        0,
                        config.temperature_unit)
    assert exception_info.match("Invalid API Key")

def test_borderline_celsius():
    input = 'Edinburgh'
    result = surfaced_values(input,
                             config.API_key,
                             " 23 ceLsiUs ? ")
    result = json.loads(result)
    assert result['Temperature'][-1] == 'C'

def test_borderline_farenheit():
    input = 'Edinburgh'
    result = surfaced_values(input,
                             config.API_key,
                             " 23 fareNheiT ? ")
    result = json.loads(result)
    assert result['Temperature'][-1] == 'F'

def test_bad_temp_unit():
    input = 'Edinburgh'
    result = surfaced_values(input,
                             config.API_key,
                             " 23 88* jj ? ")
    result = json.loads(result)
    assert result['Temperature'][-1] == 'C'