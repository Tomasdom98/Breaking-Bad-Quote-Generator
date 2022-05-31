from bbquote883.lib import get_quote

def test_string():
    assert type(get_quote()) == tuple

def test_len():
    assert len(get_quote()) > 0
