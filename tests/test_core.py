from transpi import trans


def test_trans():
    result = trans("human")
    assert result["origin"] == "human"
    assert result["pronounce"]
