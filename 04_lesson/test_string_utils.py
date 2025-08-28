import pytest
from StringUtils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   Skypro", "Skypro"),
    (" Skypro", "Skypro"),
    ("     HELLO", "HELLO"),
    (" HeLLo", "HeLLo"),
    (" Привет", "Привет"),
    (" Привет    ", "Привет    "),
    ("    hello world", "hello world"),
    ("    123456", "123456"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123"),
    ("", ""),
    ("   ", ""),
    ("%;?@", "%;?@"),
    ("/hello", "/hello"),
    ("   /hello", "/hello"),
    ("   hello_world!   ", "hello_world!   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("Skypro1", "1", True),
    ("/HELLO", "/H", True),
    ("HeLLo", "e", True),
    ("Привет", "П", True),
    (" Привет_1", "_", True),
    ("hello world, hello", "w", True),
    ("12345", "3", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("Skypro1345", "2", False),
    ("HELLO", "@", False),
    ("HeLLo", " ", False),
    ("   ", "T", False),
    ("", "1", False),
    ("hello world, hello", " Y", False),
    ("привет", "Д", False),
    ("hello world, hello", "W", False),
    ("12345", "6", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", "kyPro"),
    ("Skypro1", "1", "Skypro"),
    ("12345", "1", "2345"),
    ("12345PYT", "PYT", "12345"),
    ("hello world", "h", "ello world"),
    ("HELLOLOLOH", "LO", "HELH"),
    ("HELLOLOLOH", "O", "HELLLLH"),
    ("&^%$#@", "@", "&^%$#"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "W", "SkyPro"),
    ("____", "", "____"),
    ("", "1", ""),
    ("SkyPro", "1", "SkyPro"),
    ("SkyPro1234568", "10", "SkyPro1234568"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected



