from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
from Utilities import xlutils
import time
import pytest

class Testtransferamount:
    weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()


    def testamounttransfer(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        self.refobj.login(self.username,self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        result = self.refobj.transferaccount(filename)
        if result == True:
            assert True
        else:
            assert False


