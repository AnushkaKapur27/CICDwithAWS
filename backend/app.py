from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details')
def student():
    return jsonify({
        "name": "Anushka Kapur",
        "roll": "2023BCS0149"
    })

app.run(host='0.0.0.0', port=5000)