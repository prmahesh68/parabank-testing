from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
from Utilities import xlutils
import time
import pytest

class Testcreateaccount:
    weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()

    def testcheckingaccont(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        self.refobj.login(self.username,self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        newaccount = self.refobj.accountcreation("checking",filename)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        self.refobj.logout()
        rows= xlutils.getrowcount(filename,"Sheet1")
        for row in range(2,rows):
            accountnumber= xlutils.readfromxl(filename,"Sheet1",row,1)
            #print(accountnumber, newaccount)
            if newaccount==accountnumber:
                mark = "sucess"
                break
            else:
                mark = "not found"
                continue
        if mark == "sucess":
            print ("Checking account- ",newaccount," created sucessfully")
            assert True
        else:
            print ("failure to create a new account")
            assert False


    def testsavingsaccont(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        self.refobj.login(self.username,self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        newaccount = self.refobj.accountcreation("savings",filename)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        self.refobj.logout()
        rows= xlutils.getrowcount(filename,"Sheet1")
        for row in range(2,rows):
            accountnumber= xlutils.readfromxl(filename,"Sheet1",row,1)
            #print(accountnumber,newaccount)
            if newaccount==accountnumber:
                mark = "sucess"
                break
            else:
                mark = "not found"
                continue
        if mark == "sucess":
            print ("Savings account- ",newaccount," created sucessfully")
            assert True
        else:
            print ("failure to create a new account")
            assert False



