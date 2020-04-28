import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_DmoProg():
    msg = "hello"
    assert msg == "hi, failed bcoz assetrt failed"


def test_Dmo2Prog():
    a = 4
    b = 6
    assert a + 2 == 6, "Assert must pass"


