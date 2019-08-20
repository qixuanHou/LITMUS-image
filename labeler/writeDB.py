
import mysql.connector
from mysql.connector import Error


c = mysql.connector.connect(host='localhost',database='litmus2',user='root',password='')
cursor = c.cursor()

f = open("2018-01_class.txt",'r')
ls = f.readlines()
print(len(ls))
for l in ls:
    try:
        id, label = l[:-1].split("\t")

        sql = "update tweets set txt_label = '%s' where id = '%s';"%(label, id)
        #print(sql)
        cursor.execute(sql)
        c.commit()
    except:
        print(l)

c.close()

