# streamlit.py

import streamlit as st
from flask import Flask, request, jsonify

app = Flask(__name__)

# 데이터를 저장할 변수
stored_data = {}

# 업데이트 데이터를 처리하는 엔드포인트
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

# Streamlit 앱
def main():
    st.title('Streamlit App')
    
    # 저장된 데이터를 출력
    st.write('Stored Data:', stored_data)

if __name__ == '__main__':
    # Streamlit 앱 실행
    main()
