from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/app/getDB', methods=['GET'])
def getLLM() :
    if(request.method  == 'GET'):
        LLM = requests.get("http://localhost:5001/DB")
        with open("localDB.db", "w") as file:
            file.write(LLM.text)
        return "File received successfully!"
    else:
        return "this should be a get request"
        

@app.route('/app/getPlaybook', methods=['GET'])
def getPlayBook():
    if(request.method == "GET"):
        playbook = requests.get("http://localhost:5002/playbook")
        with open("localPlaybook.py", "w") as file:
            file.write(playbook.text)
        return "File received successfully!"
    else:
        return "this is a get request"

    
if __name__ == "__main__":
    app.run(debug=True)