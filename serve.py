from flask import Flask, request
import socket
import subprocess
app = Flask(__name__)
#subprocess.Popen(['python serve.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
       subprocess.Popen(['python serve.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
       return 'Initiated a sub-process'
   else:
       return socket.gethostname()

if __name__ == '__main__':
   app.run(debug = True)