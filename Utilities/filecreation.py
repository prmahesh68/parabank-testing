import csv
import sys
import time
import datetime
import xls_writer
from os import fsync

def filecreate(filename):
    f2=open(filename,'w')
    f2.close()
