from flask import Flask, jsonify

# 데이터를 저장할 변수
stored_data = {}

# 업데이트 데이터를 처리하는 엔드포인트
app = Flask(__name__)

@app.route('/update_data', methods=['POST'])
def update_data():
    try:
        data = request.get_json()
        global stored_data
        # 기존 데이터에 추가
        stored_data.update(data)
        return jsonify({'message': 'Data received and updated successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_data', methods=['GET'])
def get_data():
    global stored_data
    return jsonify(stored_data)

# Flask 앱 실행
if __name__ == '__main__':
    app.run(debug=True)
