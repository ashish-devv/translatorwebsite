from translate import Translator
# create flask app
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import time



app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    #return index.html file
    return render_template('index.html')


@app.route("/translate", methods=['POST'])
def trans():
    # get from request body
    alldetails=request.json
    print(alldetails)
    translator= Translator(to_lang=str(alldetails['lang']))
    output=translator.translate(str(alldetails['input']))
    return jsonify({"output":output})





if __name__ == "__main__":
  app.run(debug=True)

