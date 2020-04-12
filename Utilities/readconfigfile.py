import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")
class Getinfoconfig:
    @staticmethod
    def wedurlget():
        Weburl=config.get("inputs","Weburl")
        return  Weburl

    @staticmethod
    def usernameget():
        username = config.get("inputs", "username")
        return username

    @staticmethod
    def passwordget():
        password = config.get("inputs", "password")
        return password

    @staticmethod
    def firstnameget():
        firstname = config.get("inputs", "firstname")
        return firstname

    @staticmethod
    def lastnameget():
        lastname = config.get("inputs", "lastname")
        return lastname

    @staticmethod
    def addressget():
        address = config.get("inputs", "address")
        return address

    @staticmethod
    def cityget():
        city = config.get("inputs", "city")
        return city

    @staticmethod
    def zipcodeget():
        zipcode = config.get("inputs", "zipcode")
        return zipcode

    @staticmethod
    def stateget():
        state = config.get("inputs", "state")
        return state

    @staticmethod
    def phoneget():
        phonenumber = config.get("inputs", "phone")
        return phonenumber

    @staticmethod
    def ssnget():
        ssn = config.get("inputs", "ssn")
        return ssn

    @staticmethod
    def payeenameget():
        payeename = config.get("inputs", "payeename")
        return payeename

    @staticmethod
    def payeeaddressget():
        payeeaddress = config.get("inputs", "payeeaddress")
        return payeeaddress

    @staticmethod
    def payeecityget():
        payeecity = config.get("inputs", "payeecity")
        return payeecity

    @staticmethod
    def payeestateget():
        payeestate = config.get("inputs", "payeestate")
        return payeestate

    @staticmethod
    def payeezipget():
        payeezip = config.get("inputs", "payeezip")
        return payeezip

    @staticmethod
    def payeephget():
        payeeph = config.get("inputs", "payeeph")
        return payeeph

    @staticmethod
    def payeeaccountget():
        payeeaccount = config.get("inputs", "payeeaccount")
        return payeeaccount

    @staticmethod
    def payeeamount():
        amount = config.get("inputs", "amount")
        return amount