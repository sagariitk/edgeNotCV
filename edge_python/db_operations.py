import pymysql
import base64

db = pymysql.connect(host='vijay-app-db.ckv6z1bs6r16.us-east-2.rds.amazonaws.com',  # your host
                     user='root',  # username
                     passwd='12345678',  # password
                     db='sampleDB')  # database name

def insertURL(filename, URL):
    print('insertURL called')

    sql = """INSERT INTO blobsURLs ( URL, filename) VALUES ( "%s", "%s")""" % (
        URL, filename)
    result = db_operation(sql)
    print(result)

def getURLs():
    print('getURLs called')
    sql = """SELECT * from blobsURLs"""
    result = db_operation(sql)
    return result


def db_operation(sql):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print(e)
        db.rollback()





# def convertToBinaryData(filename):
#     with open(filename, "rb") as image:
#         f = image.read()
#         b = base64.b64encode(f)
#     return b


# def convertFromBinaryData(blob_uri, filename):
#     with open(filename, 'wb') as f:
#         f.write(base64.b64decode(blob_uri))
#         return "ghj"


# def insertBLOB(filename):
#     print('insertBLOB called')

#     blob_uri = convertToBinaryData(filename)
#     clip_name = filename

#     sql = """INSERT INTO blobs ( blob_uri, clip_name) VALUES ( "%s", "%s")""" % (
#         blob_uri, clip_name)

#     result = db_operation(sql)
#     print(result)


# def getBLOBS():
#     print('getBLOBS called')
#     sql = """SELECT * from blobs"""
#     result = db_operation(sql)
#     return result