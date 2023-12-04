# streamlit.py

import streamlit as st

# 데이터를 저장할 변수
stored_data = {}

# 업데이트 데이터를 처리하는 엔드포인트
@st.experimental_singleton
def update_data(data):
    try:
        global stored_data
        # 기존 데이터에 추가
        stored_data.update(data)
        return {'message': 'Data received and updated successfully.'}
    except Exception as e:
        return {'error': str(e)}

# Streamlit 앱
def main():
    st.title('Streamlit App')
    
    # 저장된 데이터를 출력
    st.write('Stored Data:', stored_data)

if __name__ == '__main__':
    # 업데이트 데이터를 처리하는 함수를 호출하여 데이터를 업데이트
    result = update_data({"example_key": "example_value"})
    st.write(result)  # 업데이트 결과 출력

    # Streamlit 앱 실행
    main()
