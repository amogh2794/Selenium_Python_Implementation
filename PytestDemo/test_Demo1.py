
import pytest
#@pytest.mark.smoke
def test_fstProg():
    print("hello")
#test_fstProg()

@pytest.mark.xfail
def test_sndProg():
    print("Second Method")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
