import Config
import pymysql

def db_select(sql):
    print (sql)
    try:
        conn=pymysql.connect(Config.MYSQL_HOST,Config.MYSQL_USER,Config.MYSQL_PASSWD,Config.MYSQL_DBNAME,charset='utf8')
        cursor=conn.cursor()
        cursor.execute(sql)
        res=cursor.fetchall()
    except Exception as e:
        print ('error :',e)
    finally:
        conn.close()
    return res



