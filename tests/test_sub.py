import logging

from dll.sub import my_factorial


def test_factorial(caplog):
    caplog.set_level(logging.INFO)
    assert my_factorial(4) == 24
    assert caplog.messages == ["factorial_ext() imported via os.add_dll_directory()"]
