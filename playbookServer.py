from flask import Flask, request, send_file


app = Flask(__name__)

@app.route('/playbook', methods=['GET'])
def getPlayBook():
    if(request.method == "GET"):
        return send_file('./playbook.py', as_attachment=True)
    else:
        return "this should be a get request"
    

if __name__ == "__main__":
    app.run(debug=True, port=5002)
