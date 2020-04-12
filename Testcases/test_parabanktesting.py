from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
import time
import pytest
from Utilities import xlutils
import os.path
from Utilities.CustomLogger import Logsetup

class Testbank:
    weburl = Getinfoconfig.wedurlget()
    firstname = Getinfoconfig.firstnameget()
    lastname = Getinfoconfig.lastnameget()
    address = Getinfoconfig.addressget()
    city = Getinfoconfig.cityget()
    state = Getinfoconfig.stateget()
    zipcode = Getinfoconfig.zipcodeget()
    phonenumber = Getinfoconfig.phoneget()
    ssn = Getinfoconfig.phoneget()
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
    logger = Logsetup.getlogparabank()

    @pytest.fixture()
    def browserhandling(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.logger.info("Browser Opening")
        self.Openbrowser.maximize_window()
        self.refobj = Registration(self.Openbrowser)
        # yield self.refobj.logout()

    def testcleardb(self,browserhandling):
        self.refobj.adminpagelink()
        time.sleep(3)
        result= self.refobj.cleardatabase()
        self.Openbrowser.close()
        if result == True:
            assert True
        else:
            assert False


    def testregister(self,browserhandling):
        self.refobj.registerpage()
        time.sleep(3)
        self.refobj.fillfirsname(self.firstname)
        self.refobj.filllastname(self.lastname)
        self.refobj.filladdress(self.address)
        self.refobj.fillcity(self.city)
        self.refobj.fillstate(self.state)
        self.refobj.fillzipcode(self.zipcode)
        self.refobj.fillphone(self.phonenumber)
        self.refobj.fillssn(self.ssn)
        self.refobj.fillusername(self.username)
        self.refobj.fillpassword(self.password)
        self.refobj.fillpasswordagain(self.password)
        self.refobj.registersubmit()
        title = self.Openbrowser.title
        time.sleep(3)
        self.refobj.logout()
        Act_title = "ParaBank | Customer Created"
        if Act_title==title:
            assert True
        else:
            assert False


    def testlogin(self,browserhandling):

        self.refobj = Registration(self.Openbrowser)
        result = self.refobj.login(self.username,self.password)
        time.sleep(5)
        self.refobj.logout()
        if result == True:
            assert True
        else:
            assert False

    def testaccountoverview(self,browserhandling):

        self.refobj = Registration(self.Openbrowser)
        self.refobj.login(self.username, self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        self.refobj.logout()
        time.sleep(3)
        if os.path.exists(filename) == True:
            assert True
        else:
            assert False

    def testcheckingaccont(self,browserhandling):

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
            self.logger.info("Checking account created")
            assert True
        else:
            print ("failure to create a new account")
            self.logger("Checking account not created")
            assert False


    def testsavingsaccont(self,browserhandling):

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
            self.logger.info("Savings account created")
            assert True
        else:
            print ("failure to create a new account")
            self.logger.info("Saving account not created")
            assert False

    def testpaybill(self,browserhandling):

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
        time.sleep(3)
        self.refobj.logout()
        if msg == "Bill Payment Complete":
            self.logger.info("Bill pay sucessful")
            print ("Bill Payment to ",self.payeename, "in the amount of ",self.amount, "from account ",accountnumber," was successful.")
            assert True
        else:
            print("Payment failure")
            self.logger.info("Bill payment failed")
            assert False

    def testamounttransfer(self,browserhandling):

        self.refobj.login(self.username,self.password)
        filename = self.refobj.accountoverview()
        time.sleep(3)
        result = self.refobj.transferaccount(filename)
        time.sleep(3)
        self.refobj.logout()
        if result == True:
            assert True
            self.logger.info("Account transfer sucessful")
        else:
            self.logger.info("Account transfer not sucessful")
            assert False

