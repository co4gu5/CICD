import pytest

from cicd_demo.greeting import greet


def test_greet_returns_formatted_message():
    assert greet("World") == "Hello, World!"


def test_greet_trims_whitespace():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError, match="non-empty"):
        greet("   ")
