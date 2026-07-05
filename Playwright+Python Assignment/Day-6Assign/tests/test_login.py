import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from login_page import LoginPage


def test_valid_login(page):

    with open("data/test_data.json") as file:
        data = json.load(file)

    username = data["valid_login"]["username"]
    password = data["valid_login"]["password"]

    login = LoginPage(page)

    login.open()
    login.login(username, password)

    assert "inventory" in page.url