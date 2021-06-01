from transpi import trans


def test_trans():
    youdao = trans("human")
    assert youdao["origin"] == "human"
    assert "[ˈhjuːmən]" in youdao["pronounce"][0]
    assert youdao["trans"]
    assert youdao["examples"]

    bing = trans("human", engine="bing")
    assert bing["pronounce"]
    assert bing["trans"]
    assert bing["examples"]


def test_no_exists_trans():
    empty = trans("wrod")
    assert not empty["origin"]
    assert not empty["pronounce"]
    assert not empty["trans"]
    assert not empty["examples"]
