import dateutil
import datetime
from datetime import date,datetime
import time
import dateutil.parser
class Date_spilt:

    def dateconverter(date1):
        date1 = str(date1)
        date1 = date1.split()[0]
        # date1= datetime.date(date1)
        # print (date1)
        # print (type(date1))
        return date1
    def dataconverter1(date2):
        return (date2.strftime('%m/%d/%Y'))

    def datetimeconverter(self):
        ts = time.time()  # get the time, to use in a filename
        ds = datetime.fromtimestamp(ts).strftime('%d%m%Y%H%M')
        return ds

    def month_numbertostring (month):
        m = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
         }
        try:
            monthname = m[month]
            return monthname
        except:
            raise ValueError('Not a month')







