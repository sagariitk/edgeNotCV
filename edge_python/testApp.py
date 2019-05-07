
# aws_access_key_id = 'AKIA2O5QQ2XD22262NWF',
# aws_secret_access_key = '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'

# session = boto3.Session(
#     aws_access_key_id = 'AKIA2O5QQ2XD22262NWF',
#     aws_secret_access_key = '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'
# )
# url = '{}/{}/{}'.format(client.meta.endpoint_url, bucket_name, filename)


# import boto3
# from os import listdir
# import os
# from os.path import isfile, join
# import db_operations

# file_path = os.getcwd()
# client = boto3.client('s3',
#     aws_access_key_id="AKIA2O5QQ2XD22262NWF",
#     aws_secret_access_key="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",
#     )
# bucket_name = 'edge-app'
# file_list = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# for filename in file_list:
#     if ".png" in filename: 
#         print(filename)
#         client.upload_file(filename, bucket_name, filename, ExtraArgs={'ACL':'public-read'})
#         location = client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
#         url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, filename)
#         db_operations.insertURL(filename, url)
#         print(url)


# import boto3
# from os import listdir
# import os
# from os.path import isfile, join
# import db_operations

# urlsDict = {} 
# urls = db_operations.getURLs()

# for url in urls:
#     filename = url[2]
#     urlsDict[filename] = url[1]
#     print(urlsDict[filename])





# client = boto3.client('s3',
#     aws_access_key_id="AKIA2O5QQ2XD22262NWF",
#     aws_secret_access_key="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",
#     )

# location = client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
# url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, filename)
# print(url)

# import boto3

# # Create an S3 client
# client = boto3.client('s3',
#     aws_access_key_id="AKIA2O5QQ2XD22262NWF",
#     aws_secret_access_key="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",
#     )

# filename = 'requirment.txt'
# bucket_name = 'test-bucket-sagar-yadav'

# # response = client.list_buckets()
# response = client.list_objects(
#     Bucket=bucket_name
# )
# # client.upload_file(filename,bucket_name,filename)

# print(response)


# import pymysql
# import base64

# db = pymysql.connect(host='vijay-app-db.ckv6z1bs6r16.us-east-2.rds.amazonaws.com',  # your host
#                      user='root',  # username
#                      passwd='12345678',  # password
#                      db='sampleDB')  # database name

# def convertToBinaryData(filename):
#     with open(filename, "rb") as image:
#         f = image.read()
#         b = base64.b64encode(f)
#     return b


# def convertFromBinaryData(blob_uri, filename):

#     with open(filename, 'wb') as f:
#         f.write(base64.b64decode(blob_uri))
#         return "ghj"


# def insertBLOB():
#     print('insertBLOB called')

#     filename = 'requirment.txt'
#     blob_uri = convertToBinaryData(filename)
#     clip_name = filename

#     sql = """INSERT INTO blobs ( blob_uri, clip_name) VALUES ( "%s", "%s")""" % (
#         blob_uri, clip_name)

#     result = db_operation(sql)
#     print(result)


# def fetchBLOB():
#     print('fetchBLOB called')
#     sql = """SELECT * from blobs"""
#     result = db_operation(sql)
#     convertFromBinaryData(result[0][1], 'abc.txt')
#     print(result)


# def db_operation(sql):
#     cursor = db.cursor()
#     try:
#         cursor.execute(sql)
#         db.commit()
#         return cursor.fetchall()
#     except Exception as e:
#         print(e)
#         db.rollback()


# if __name__ == '__main__':
#     insertBLOB()
#     fetchBLOB()

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