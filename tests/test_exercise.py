import pytest
from src.gift import Gift
from src.package import Package

def test_exercise():
    book = Gift("Harry Potter and the Chamber of Secrets", 3)

    assert book.get_name() == "Harry Potter and the Chamber of Secrets"
    assert book.get_weight() == 3

    package = Package()
    package.add_gift(book)

    assert package.total_weight() == 3
