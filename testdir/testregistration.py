from selenium import webdriver
from Utilities.readconfigfile import Getinfoconfig
from Objref.Paraobjreferences import Registration
import time
# import pytest

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
    print(username)

    def testcleardb(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.Openbrowser.get(self.weburl)
        self.refobj = Registration(self.Openbrowser)
        self.refobj.adminpagelink()
        time.sleep(3)
        result= self.refobj.cleardatabase()
        self.Openbrowser.close()
        if result == True:
            assert True
        else:
            assert False


    def testregister(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.weburl)
        self.Openbrowser.maximize_window()
        self.refobj = Registration(self.Openbrowser)
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
        Act_title = "ParaBank | Customer Created"
        if Act_title==title:
            assert True
        else:
            assert False








