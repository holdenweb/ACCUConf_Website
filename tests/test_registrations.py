#!/usr/bin/env python
import pytest
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from accuconf.models import *
from accuconf.database import db, create_db, drop_db
from accuconf import app, init_sec_ctxt


@pytest.fixture
def registrationData(key = "valid"):
    data = {

        "valid": dict(email="a@b.c",
                      password="Password1",
                      firstname="User",
                      lastname="Name",
                      phone="+011234567890",
                      pincode="123456",
                      salutation="Mr.",
                      suffix="",
                      country="India",
                      state="TamilNadu",
                      captcha="1",
                      question="12"
                      ),
        "valid2": dict(email="test@test.dom",
                       pssword="passworD13",
                       firstname="User2",
                       lastname="Name2",
                       phone="+011234567890",
                       pincode="123456",
                       salutation="Dr.",
                       suffix="Jr.",
                       country="India",
                       state="TamilNadu",
                       captcha="1",
                       question="12"
                       ),
        "shortpass": dict(email="test@std.dom",
                          password="Pass1",
                          firstname="User2",
                          lastname="Name2",
                          phone="+011234567890",
                          pincode="123456",
                          salutation="Dr.",
                          suffix="Jr.",
                          country="India",
                          state="TamilNadu",
                          captcha="1",
                          question="12"
                          ),
        "invalidpass": dict(email="test@std.dom",
                            password="password",
                            firstname="User2",
                            lastname="Name2",
                            phone="+011234567890",
                            pincode="123456",
                            salutation="Dr.",
                            suffix="Jr.",
                            country="India",
                            state="TamilNadu",
                            captcha="1",
                            question="12"
                          ),
        "invaliduser": dict(email="testing.test.dom",
                            password="passworD13",
                            firstname="User2",
                            lastname="Name2",
                            phone="+011234567890",
                            pincode="123456",
                            salutation="Dr.",
                            suffix="Jr.",
                            country="India",
                            state="TamilNadu",
                            captcha="1",
                            question="12"
                            )
    }
    return data[key]


class TestUserRegistration:

    def setup_method(self, method):
        self.app = app.test_client()
        with app.app_context():
            drop_db()
            create_db()
            init_sec_ctxt()

    def teardown_method(self, method):
        drop_db()

    def test_user_reg_basic(self):
        rv = self.app.post('/register', data=registrationData())
        print (type(rv.data))
        assert rv.data is not None
        assert "You have successfully registered" in rv.data.decode("utf-8")

    def test_user_reg_dup(self):
        rv1 = self.app.post('/register', data=registrationData("valid"))
        assert rv1.data is not None
        assert "You have successfully registered" in rv1.data.decode("utf-8")
        rv2 = self.app.post('/register', data=registrationData("valid"))
        assert rv1.data is not None
        assert "Duplicate user id" in rv2.data.decode("utf-8")

    def test_password_short(self):
        rv = self.app.post('/register', data=registrationData("shortpass"))
        print (type(rv.data))
        assert rv.data is not None
        assert "Password did not meet checks" in rv.data.decode("utf-8")

    def test_password_invalid(self):
        rv = self.app.post('/register', data=registrationData("invalidpass"))
        print (type(rv.data))
        assert rv.data is not None
        assert "Password did not meet checks" in rv.data.decode("utf-8")

    def test_username_invalid(self):
        rv = self.app.post('/register', data=registrationData("invaliduser"))
        print (type(rv.data))
        assert rv.data is not None
        assert "Invalid/Duplicate user id" in rv.data.decode("utf-8")
