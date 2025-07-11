from os import getenv

from pytest import mark


@mark.xfail(
    getenv("ALUMNIUM_DRIVER", "selenium") == "appium",
    reason="Synchrnoization is not implemented in Appium yet",
)
def test_waiting_for_loading_content(al, navigate):
    navigate("https://the-internet.herokuapp.com/dynamic_content")
    assert al.get("the total number of profile images") == 3


@mark.xfail(
    getenv("ALUMNIUM_DRIVER", "selenium") == "appium",
    reason="Synchrnoization is not implemented in Appium yet",
)
def test_waiting_for_requests_and_form_updates(al, navigate):
    navigate("https://the-internet.herokuapp.com/forgot_password")
    al.do("type test@example.com in the email field")
    al.do("click Retrieve password button")
    al.check("should see Internal Server Error")
