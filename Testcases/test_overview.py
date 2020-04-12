from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
import os.path
import time
import pytest

class Testoverview:
    weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()

    def testaccountoverview(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        self.refobj.login(self.username,self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        self.refobj.logout()
        time.sleep(3)
        if os.path.exists(filename) == True:
            assert True
        else:
            assert False


