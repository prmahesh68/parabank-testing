from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
import time
import pytest

class TestLogin:
    weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()

    def testlogin(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        result = self.refobj.login(self.username,self.password)
        time.sleep(5)
        self.refobj.logout()
        if result == True:
            assert True
        else:
            assert False
