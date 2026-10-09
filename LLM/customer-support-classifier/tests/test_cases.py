
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validator import parse_json, validate_category


def test_valid_categories():
    categories = ["billing", "refund", "technical", "other"]

    for category in categories:
        data = parse_json('{"category": "' + category + '"}')
        assert data is not None
        assert validate_category(data)


def test_missing_category():
    data = parse_json('{"reason": "refund"}')
    assert not validate_category(data)


def test_invalid_category():
    data = parse_json('{"category": "payment"}')
    assert not validate_category(data)


def test_invalid_json():
    data = parse_json("this is not json")
    assert data is None


def test_non_dictionary_json():
    data = parse_json('["billing"]')
    assert not validate_category(data)


if __name__ == "__main__":
    test_valid_categories()
    test_missing_category()
    test_invalid_category()
    test_invalid_json()
    test_non_dictionary_json()

    print("All tests passed!")