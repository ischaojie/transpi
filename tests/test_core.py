import pytest
from transpi import trans
from transpi.core import Trans
from transpi.core import YoudaoTrans
from transpi.exception import NotEnglishWordException


def test_trans_class():

    with pytest.raises(NotImplementedError):

        class TestTrans(Trans):
            pass


@pytest.mark.parametrize("word", ["hello", "translation", "test"])
def test_youdao_trans(word):
    trans = YoudaoTrans(word)
    assert trans.translation
    assert trans.pronounce
    assert trans.sentences


@pytest.mark.parametrize("word", ["hello", "translation", "test"])
def test_youdao_trans_get_voice(word):
    trans = YoudaoTrans(word)
    assert trans.pronounce[0].get("voice")


@pytest.mark.parametrize("word", ["hello"])
def test_trans(word):
    r = trans(word, "youdao")
    assert r.get("translation")
    assert r.get("pronounce")
    assert r.get("sentences")


def test_not_word():
    with pytest.raises(NotEnglishWordException):
        r = trans("test me")
