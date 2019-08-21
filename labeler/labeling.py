import mysql.connector
from mysql.connector import Error
import csv

c = mysql.connector.connect(host='localhost',database='litmus2',user='root',password='')
cursor = c.cursor()

def getText():
    sql = "select id, text, img from tweets where date like '%2018-01%';"
    cursor.execute(sql);
    rows = cursor.fetchall()
    fp = open('2018-01.csv'%date, 'w')
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()


def getLabels():
    sql = "select id, img from tweets where date like '%2018-01%' and img != 'None' and labels is null limit 500;"
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        image.source.image_uri = r[-1]
        response = client.label_detection(image=image)
        labels = response.label_annotations
        labelList = []
        for l in labels:
            labelList.append(l.description)
        sql = "update tweets set labels = '%s' where id = '%s'"%(str(labelList).replace("'","")[1:-1],r[0])
        cursor.execute(sql)
        c.commit()

def exportLabels():
    sql = "select * from tweets where labels is not null;"
    cursor.execute(sql);
    rows = cursor.fetchall()
    fp = open('2018-01-labels.csv', 'w')
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()

exportLabels()
cursor.close()
c.close()
