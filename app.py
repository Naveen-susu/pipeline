from flask imort Flask, jsonify

app = Flask(__name__)

@app.route('/', method=['get'])
def welcome():
    return jsonify(message="you are welcome!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=Flask)
