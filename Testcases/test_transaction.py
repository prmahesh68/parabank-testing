from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
import os.path
import time
import pytest

class Testtransaction:
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



