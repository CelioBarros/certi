from flask import Flask, jsonify
from auxiliar_function import number_to_word

app = Flask(__name__)

@app.route("/<number>")
def hello(number):
  try:
    number = int(number)
    return jsonify({"extenso": number_to_word(number) })
  except:
    return jsonify({"error": 'bad request!' }), 400

if __name__ == '__main__':
	app.run(port=3000,use_reloader=True,host='0.0.0.0')
