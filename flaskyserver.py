import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import os, ssl
UPLOAD_FOLDER = '/home/<>/demo/'

certfile = "/<PATH>/fullchain.pem"
keyfile = "/<PATH>//privkey.pem"\

sslcontext = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
sslcontext.options = ssl.OP_NO_TLSv1
sslcontext.options = ssl.OP_NO_TLSv1_1
sslcontext.protocol = ssl.PROTOCOL_TLSv1_2
sslcontext.load_cert_chain(certfile, keyfile)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file = request.get_data()
        with open('sensitive.docx', 'a') as the_file:
            the_file.write(file)
        return "success"
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
       <form action = "" method = "post" enctype="multipart/form-data">  
        <input type="file" name="file" />  
        <input type = "submit" value="Upload">  
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=sslcontext, threaded=True, debug=True)
   
