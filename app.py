from flask import Flask, request, jsonify
from module import calculate_priority

app = Flask(__name__)

@app.route('/api/v1/prioritize', methods=['POST'])
def prioritize():
    data = request.json
    result = calculate_priority(
        tier=data.get("tier"),
        urgency=data.get("urgency"),
        problem_type=data.get("problem_type")
    )
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)