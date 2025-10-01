import sys
sys.path.insert(0, "./src")
from massh import __version__

def test_version_is_non_empty_string():
    assert type(__version__) == str
    assert __version__ != ""