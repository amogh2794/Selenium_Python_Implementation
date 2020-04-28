import pytest
@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I am executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return["Amogh", "Vaidya"]
@pytest.fixture(params=[("chrome","Amogh"),"Firefox","IE"])
def crossBrowser(request):
    return request.param