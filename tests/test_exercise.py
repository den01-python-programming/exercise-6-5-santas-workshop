import pytest
import os

def test_exercise():
    os.chdir('src')

    from gift import Gift
    from package import Package

    book = Gift("Harry Potter and the Chamber of Secrets", 3)

    assert book.get_name() == "Harry Potter and the Chamber of Secrets"
    assert book.get_weight() == 3

    package = Package()
    package.add_gift(book)

    assert package.total_weight() == 3
