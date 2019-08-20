import mysql.connector
from mysql.connector import Error

c = mysql.connector.connect(host='localhost',database='litmus2',user='root',password='')
cursor = c.cursor()


def createTable(cursor):
    sql = """
        create table tweets (
            username TEXT,
            date DATETIME,
            retweets INT,
            favorites INT,
            text TEXT,
            geo TEXT,
            mentions TEXT,
            hashtags TEXT,
            id CHAR(40) PRIMARY KEY NOT NULL,
            permalink TEXT,
            img TEXT); """
    cursor.execute(sql);


# ;2018-01-29 23:55;4;41;"Kesha deserved to win not only because of how strong she is, but praying is musically, lyrically, and vocally better than shape of you by a landslide";;;;"958126592827551750";https://twitter.com/emmasdaisies/status/958126592827551750;None

def insertLine(cursor, l):
    itemA = l.split(';"')[0]
    itemA = itemA.split(";")
    text = l.split(';"')[1].split('";')[0]
    img = l[:-1].split(";")[-1]
    link = l[:-1].split(";")[-2]
    id = l[:-1].split(";")[-3].replace('"',"")
    
    sql = "insert into tweets (username, date, retweets, favorites, text, geo, mentions, hashtags, id, permalink, img) values ('%s','%s',%s,%s,\"%s\",'%s','%s','%s','%s','%s','%s');"%(itemA[0],itemA[1],itemA[2],itemA[3],text.replace('"',""),'','','',id,link,img)
    try:    
        cursor.execute(sql);
    except: 
        print(l)
        print(sql)

#createTable(cursor)

f = open('landslide_2018-12.txt','r')
f.readline()
ls = f.readlines()
for l in ls:
    insertLine(cursor,l);

c.commit()
cursor.close()
c.close()
