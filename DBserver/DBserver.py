from flask import Flask, request, send_file


app = Flask(__name__)

@app.route('/DB', methods=['GET'])
def LLM() :
    if(request.method  == 'GET'):
        return send_file('./sample.db', as_attachment=True)
    else:
        return "this should be a get request"


if __name__ == "__main__":
    app.run(debug=True, port=5001)