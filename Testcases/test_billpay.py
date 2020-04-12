from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
from Utilities import xlutils
import time
import pytest

class Testbillpay:
    weburl = Getinfoconfig.wedurlget()
    username = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()
    payeename = Getinfoconfig.payeenameget()
    payeeaddress = Getinfoconfig.payeeaddressget()
    payeecity = Getinfoconfig.payeecityget()
    payeestate = Getinfoconfig.payeestateget()
    payeezip = Getinfoconfig.payeezipget()
    payeeph = Getinfoconfig.payeephget()
    payeeaccount = Getinfoconfig.payeeaccountget()
    amount = Getinfoconfig.payeeamount()


    def testpaybill(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        self.refobj.login(self.username,self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        self.refobj.clickpaybill()
        time.sleep(3)
        self.refobj.inputpayeename(self.payeename)
        self.refobj.inputpayeeaddres(self.payeeaddress)
        self.refobj.inputpayeecity(self.payeecity)
        self.refobj.inputpayeestate(self.payeestate)
        self.refobj.inputpayeezipcode(self.payeezip)
        self.refobj.inputpayeeph(self.payeeph)
        self.refobj.inputpayeeaccount(self.payeeaccount)
        self.refobj.inputpayeeverify(self.payeeaccount)
        self.refobj.inputpayeeamount(self.amount)
        time.sleep(3)
        accountnumber= xlutils.readfromxl(filename,"Sheet1",2,1)
        self.refobj.selectbillpayaccount(accountnumber)
        time.sleep(3)
        self.refobj.clickpaymentbutton()
        time.sleep(3)
        msg = self.Openbrowser.find_element_by_xpath("//h1[contains(text(),'Bill Payment Complete')]").text
        if msg == "Bill Payment Complete":
            print ("Bill Payment to ",self.payeename, "in the amount of ",self.amount, "from account ",accountnumber," was successful.")
            assert True
        else:
            print("Payment failure")
            assert False


