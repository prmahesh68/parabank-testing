import mysql.connector
dbconnect = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="Ramya123",database="ramya")
# dbconnect.cursor().execute("insert into python values('mahesh3',12);") # insert
# dbconnect.cursor().execute("update python set name='mahesh5' where name='mahesh4';") # update
# dbconnect.cursor().execute("delete from python where name='mahesh2';") # delete
# dbconnect.commit() # commit for each DML operation
cur = dbconnect.cursor()
cur.execute("select * from python;")
# Cols = dbconnect.cursor().execute("select count(column_name) as Number from information_schema.columns where table_name='data';")
for cl in cur:
    print (cl[0],cl[1])


dbconnect.close()