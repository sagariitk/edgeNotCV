from flask import Flask, render_template, request, redirect, jsonify, Response
from flask_cors import CORS
import cv2
import datetime, time
import db_operations
from flask_jwt_extended import ( JWTManager, jwt_required, create_access_token, get_jwt_identity, jwt_refresh_token_required, create_refresh_token)
from binascii import a2b_base64
from PIL import Image
import boto3
from os import listdir
import os
from os.path import isfile, join
import db_operations

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secretkey'
jwt = JWTManager(app)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"msg": "Flask App Working"}), 200

@app.route('/capture', methods=['POST'])
@jwt_required
def capture():
    image_URI = request.json.get('image_URI', None)
    image_name = request.json.get('image_name', None)
    color_tone = request.json.get('color_tone', None)

    if(color_tone == 'gray'):
        data = image_URI.split(',')[1]
        binary_data = a2b_base64(data)
        fd = open(image_name, 'wb')
        fd.write(binary_data)
        fd.close()
        img = Image.open(image_name).convert('LA')
        img.save(image_name)
        uploadS3(image_name)
        return jsonify({"msg": "Image saved locally"}), 200
    else:
        data = image_URI.split(',')[1]
        binary_data = a2b_base64(data)

        fd = open(image_name, 'wb')
        fd.write(binary_data)
        fd.close()
        uploadS3(image_name)
        return jsonify({"msg": "Image saved locally"}), 200 

def uploadS3(filename):
    client = boto3.client('s3',
        aws_access_key_id="AKIA2O5QQ2XD22262NWF",
        aws_secret_access_key="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",
        )
    bucket_name = 'edge-app'
    file_path = os.getcwd()
    print(filename)
    print("uploading to S3...")
    client.upload_file(filename, bucket_name, filename, ExtraArgs={'ACL':'public-read'})
    print("Uploade done")
    os.rename(filename, "uploaded_" + filename)
    location = client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, filename)
    db_operations.insertURL(filename, url)



@app.route('/images', methods=['GET'])
@jwt_required
def images():

    urlsDict = []
    urls = db_operations.getURLs()
    try:       
        for url in urls:
            urlsDict.append(url[1])
    except:
        pass
    return jsonify(urlsDict), 200     

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    expires_token = datetime.timedelta(seconds=600)
    expires_refresh = datetime.timedelta(seconds=6000)
    if(username == 'admin' and password == 'admin'):
        ret = {
            'access_token': create_access_token(identity=username, expires_delta=expires_token),
            'refresh_token': create_refresh_token(identity=username, expires_delta=expires_refresh)
        }
        return jsonify(ret), 200
    elif(username == 'test' and password == 'test'):
        ret = {
            'access_token': create_access_token(identity=username, expires_delta=expires_token),
            'refresh_token': create_refresh_token(identity=username, expires_delta=expires_refresh)
        }
        return jsonify(ret), 200
    else:
        return jsonify({"msg": "Username or password is not valid"}), 401


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
