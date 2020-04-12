from selenium import webdriver
import csv
import datetime
from Utilities.dateconverter import Date_spilt
from Utilities import filecreation
from Utilities import xlutils
from selenium.webdriver.support.ui import Select
from Utilities.CustomLogger import Logsetup
import time

class Registration:
    adminpagelink_xpath = "//a[contains(text(),'Admin Page')]"
    dbclean_xpath = "//button[contains(text(),'Clean')]"
    registerlink_xpath = "//a[contains(text(),'Register')]"
    inputfirstname_name = "customer.firstName"
    inputlastname_name = "customer.lastName"
    inputaddress_name= "customer.address.street"
    inputcity_name= "customer.address.city"
    inputstate_name = "customer.address.state"
    inputzipcode_name = "customer.address.zipCode"
    inputphone_name= "customer.phoneNumber"
    inputssn_name = "customer.ssn"
    inputusername_name = "customer.username"
    inputpassword_name = "customer.password"
    inputpasswordconfirm_name = "repeatedPassword"
    clickregister_xpath = "//table[@class='form2']//input[@class='button']"
    loginusername_name = "username"
    loginpassword_name = "password"
    clicklogin_xpath = "//input[@class='button']"
    overviewtable_xpath = "//table[@id='accountTable']//tbody"
    accountoverview_xpath = "//a[contains(text(),'Accounts Overview')]"
    linkopenaccount_xpath = "//a[contains(text(),'Open New Account')]"
    selectaccounttype_id= "type"
    fromaccount_id = "fromAccountId"
    clickopenaccount_xpath ="//input[@class='button']"
    newaccountid_xpath = "//a[@id='newAccountId']"
    linklogout_xpath = "//*[@id='leftPanel']/ul/li[8]/a"
    linktransfer_xpath = "//a[contains(text(),'Transfer Funds')]"
    inputtransferamount = "//input[@id='amount']"
    selectfromaccount_xpath = "//select[@id='fromAccountId']"
    selecttoaccount_xpath = "//select[@id='toAccountId']"
    clicktransferbutton = "//input[@class='button']"
    fillpayeename_name = "payee.name"
    fillpayeeaddress_name = "payee.address.street"
    fillpayeecity_name="payee.address.city"
    fillpayeestate_name="payee.address.state"
    fillpayeezip_name="payee.address.zipCode"
    fillpayeeph_name="payee.phoneNumber"
    fillpayeeaccount_name="payee.accountNumber"
    fillpayeeverify_name="verifyAccount"
    inputpayeetransferamount_name ="amount"
    selectfromaccountpayee_xpath ="//select[@name='fromAccountId']"
    sendpayment_xpath="//input[@class='button']"
    linkbillpay_xpath ="//a[contains(text(),'Bill Pay')]"
    fillpayeeamount_name = "amount"
    logger = Logsetup.getlogparabank()

    def __init__(self,Openbrowser):
        self.Openbrowser = Openbrowser
    def registerpage(self):
        self.Openbrowser.find_element_by_xpath(self.registerlink_xpath).click()
    def fillfirsname(self,firstname):
        self.Openbrowser.find_element_by_name(self.inputfirstname_name).send_keys(firstname)
    def filllastname(self,lastname):
        self.Openbrowser.find_element_by_name(self.inputlastname_name).send_keys(lastname)
    def filladdress(self,address):
        self.Openbrowser.find_element_by_name(self.inputaddress_name).send_keys(address)
    def fillcity(self,city):
        self.Openbrowser.find_element_by_name(self.inputcity_name).send_keys(city)
    def fillstate(self,state):
        self.Openbrowser.find_element_by_name(self.inputstate_name).send_keys(state)
    def fillzipcode(self,zipcode):
        self.Openbrowser.find_element_by_name(self.inputzipcode_name).send_keys(zipcode)
    def fillphone(self,phonenumber):
        self.Openbrowser.find_element_by_name(self.inputphone_name).send_keys(phonenumber)
    def fillssn(self,ssn):
        self.Openbrowser.find_element_by_name(self.inputssn_name).send_keys(ssn)
    def fillusername(self,username):
        self.Openbrowser.find_element_by_name(self.inputusername_name).send_keys(username)
    def fillpassword(self,password):
        self.Openbrowser.find_element_by_name(self.inputpassword_name).send_keys(password)
    def fillpasswordagain(self,password):
        self.Openbrowser.find_element_by_name(self.inputpasswordconfirm_name).send_keys(password)
    def registersubmit(self):
        self.Openbrowser.find_element_by_xpath(self.clickregister_xpath).click()
    def adminpagelink(self):
        self.Openbrowser.find_element_by_xpath(self.adminpagelink_xpath).click()
    def cleardatabase(self):
        msg = "Database Cleaned"
        self.Openbrowser.find_element_by_xpath(self.dbclean_xpath).click()
        bodytext = self.Openbrowser.find_element_by_tag_name("Body").text
        if msg in bodytext:
            self.logger.info("Database cleaned")
            return True
        else:
            self.logger.info("Database not cleaned")
            return False
    def login(self,username,password):
        self.Openbrowser.find_element_by_name(self.loginusername_name).send_keys(username)
        self.Openbrowser.find_element_by_name(self.loginpassword_name).send_keys(password)
        self.Openbrowser.find_element_by_xpath(self.clicklogin_xpath).click()
        msg = "ParaBank | Accounts Overview"
        title = self.Openbrowser.title
        if msg == title:
            self.logger.info("Login Sucessful")
            return True
        else:
            self.logger.info("Login Sucessful")
            return False

    def logout(self):
        self.Openbrowser.find_element_by_xpath(self.linklogout_xpath).click()
        self.logger.info("Logout Sucessful")
        time.sleep(3)
        self.logger.info("Closing browser")
        self.Openbrowser.close()


    def accountoverview(self):
        self.Openbrowser.find_element_by_xpath(self.accountoverview_xpath).click()
        time.sleep(5)
        # date1 = datetime.date.today()
        # date1 = Date_spilt.dateconverter(date1)
        # date1 =str(date1)
        date1= Date_spilt.datetimeconverter(self)
        filename="C:\\Users\\Ramya\\PycharmProjects\\parabank practice\\data\\"+date1+".xlsx"
        xlutils.filecreate(filename)
        # print (date1)
        # print (filename)
        coln = len(self.Openbrowser.find_elements_by_xpath("//table[@id='accountTable']//thead/tr/th"))
        row = len(self.Openbrowser.find_elements_by_xpath("//*[@id='accountTable']/tbody/tr"))
        # print (coln,row)
        for c in range(1,coln+1):
            data = self.Openbrowser.find_element_by_xpath("//table[@id='accountTable']//thead/tr/th["+str(c)+"]").text
            xlutils.writetoxl(filename,"Sheet1",1,c,data)
        for r in range(1,row+1):
            for c in range(1,coln+1):
                data1 = self.Openbrowser.find_element_by_xpath("//table[@id='accountTable']//tbody//tr["+str(r)+"]//td["+str(c)+"]").text
                xlutils.writetoxl(filename,"Sheet1",r+1,c,data1)
        self.logger.info("account overview written to xls file")
        return filename

    def accountcreation(self,type,filename):
        self.Openbrowser.find_element_by_xpath(self.linkopenaccount_xpath).click()
        time.sleep(3)
        select = Select(self.Openbrowser.find_element_by_id(self.selectaccounttype_id))
        if type == "checking":
            select.select_by_visible_text("CHECKING")
        elif type == "savings":
            select.select_by_visible_text("SAVINGS")
        rows =xlutils.getrowcount(filename,"Sheet1")
        columns = xlutils.getcolumnount(filename,"Sheet1")
        for row in range(2,rows):
            Amount = xlutils.readfromxl(filename,"Sheet1",row,2)
            accountnumber = xlutils.readfromxl(filename,"Sheet1",row,1)
            amount =float(str.replace(Amount,'$',''))
            if amount >= 200:
                select = Select(self.Openbrowser.find_element_by_id(self.fromaccount_id))
                select.select_by_visible_text(accountnumber)
                self.Openbrowser.find_element_by_xpath(self.clickopenaccount_xpath).click()
                time.sleep(3)
                newaccountnumber = self.Openbrowser.find_element_by_xpath(self.newaccountid_xpath).text
                break
            else:
                newaccountnumber = 00000
                continue
        return newaccountnumber

    def transferaccount(self,filename):
        self.Openbrowser.find_element_by_xpath(self.linktransfer_xpath).click()
        time.sleep(3)
        rows = xlutils.getrowcount(filename,"Sheet1")
        columns = xlutils.getcolumnount(filename,"Sheet1")
        sourceaccount = xlutils.readfromxl(filename,"Sheet1",2,1)
        sourceamount = xlutils.readfromxl(filename,"Sheet1",2,2)
        sourceamount1 = float(str.replace(sourceamount, '$', ''))
        targetaccount = xlutils.readfromxl(filename,"Sheet1",3,1)
        targetaccountamount = xlutils.readfromxl(filename,"Sheet1",3,2)
        targetaccountamount1 = float(str.replace(targetaccountamount,'$',''))
        if sourceamount1 >200:
            self.Openbrowser.find_element_by_xpath(self.inputtransferamount).send_keys("100")
            select = Select(self.Openbrowser.find_element_by_xpath(self.selectfromaccount_xpath))
            select.select_by_visible_text(sourceaccount)
            select = Select(self.Openbrowser.find_element_by_xpath(self.selecttoaccount_xpath))
            select.select_by_visible_text(targetaccount)
            self.Openbrowser.find_element_by_xpath(self.clicktransferbutton).click()
            time.sleep(3)
            msg = self.Openbrowser.find_element_by_xpath("//*[@id='rightPanel']/div/div/h1").text
            if msg == "Transfer Complete!":
                print ("$100 transferred from ",sourceaccount," to ",targetaccount)
                self.logger.info("100 transferred")
                return True
            else:
                print("Transfer failed")
                self.logger.info("transfer failed")
                return False
        else:
            print("Insufficent balance")
            self.logger.info("Insufficent funds")
            return False

    def clickpaybill(self):
        self.Openbrowser.find_element_by_xpath(self.linkbillpay_xpath).click()
    def inputpayeename(self,payeename):
        self.Openbrowser.find_element_by_name(self.fillpayeename_name).send_keys(payeename)
    def inputpayeeaddres(self,payeeaddress):
        self.Openbrowser.find_element_by_name(self.fillpayeeaddress_name).send_keys(payeeaddress)
    def inputpayeecity(self,payeecity):
        self.Openbrowser.find_element_by_name(self.fillpayeecity_name).send_keys(payeecity)
    def inputpayeestate(self,payeestate):
        self.Openbrowser.find_element_by_name(self.fillpayeestate_name).send_keys(payeestate)
    def inputpayeezipcode(self,payeezip):
        self.Openbrowser.find_element_by_name(self.fillpayeezip_name).send_keys(payeezip)
    def inputpayeeph(self,payeeph):
        self.Openbrowser.find_element_by_name(self.fillpayeeph_name).send_keys(payeeph)
    def inputpayeeaccount(self,payeeaccount):
        self.Openbrowser.find_element_by_name(self.fillpayeeaccount_name).send_keys(payeeaccount)
    def inputpayeeverify(self,payeeaccount):
        self.Openbrowser.find_element_by_name(self.fillpayeeverify_name).send_keys(payeeaccount)
    def clickpaymentbutton(self):
        self.Openbrowser.find_element_by_xpath(self.sendpayment_xpath).click()
    def inputpayeeamount(self,amount):
        self.Openbrowser.find_element_by_name(self.fillpayeeamount_name).send_keys(amount)
    def selectbillpayaccount(self,accountnumber):
        select = Select(self.Openbrowser.find_element_by_xpath(self.selectfromaccountpayee_xpath))
        select.select_by_visible_text(accountnumber)












