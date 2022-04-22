import pymysql
from Bean import *
import Bean

class markDao():

    def nextPk(self):
        r = 0
        connection = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port = 3307)
        with connection.cursor() as cursor:
            sql = "select max(id) from info"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
        connection.close()
        for d in result:
            r = d[0]
        return r+1

    def add(self, mb):
        pk = markDao.nextPk(mb)
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query = "insert into info values (%s, %s, %s, %s, %s)"
            data = (pk , mb.getname(), mb.getemail(), mb.getpwd(), mb.getadr())
            crs.execute(query, args=data)
            conn.commit()
        conn.close()


    def search_single(self, mb):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            sql = "select * from info where id = %s"
            data = mb.getid()
            crs.execute(sql, args=data)
            result = crs.fetchall()
            conn.commit()
        crs.close()
        for d in result:
            print("|", d[0], "|", "\t", d[1], "|", "\t", d[2], "|", "\t", d[3], "|", "\t", d[4])

    def search_all(self):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query = "select * from info"
            crs.execute(query)
            result = crs.fetchall()
            conn.commit()
        crs.close()
        for d in result:
            print("|",d[0],"|","\t", d[1],"|","\t",d[2],"|","\t",d[3],"|","\t",d[4],"|",)


    def update(self,mb):
        conn = pymysql.connect(host="localhost", user= "root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query= "update info set name = %s, email = %s, pwd = %s, adr = %s where id = %s"
            data = (mb.getname(), mb.getemail() , mb.getpwd(),mb.getadr(), mb.getid())
            crs.execute(query, args=data)
            conn.commit()
        crs.close()


    def delete(self,mb):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query= "delete from info where id = %s"
            data = mb.getid()
            crs.execute(query, args=data)
            conn.commit()
        crs.close()

