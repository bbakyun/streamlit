import streamlit as st
import requests

# Streamlit 앱
def main():
    st.title('Streamlit App')
    
    # 저장된 데이터를 출력
    response = requests.get("http://localhost:5000/get_data")
    stored_data = response.json()
    st.write('Stored Data:', stored_data)

# Streamlit 앱 실행
if __name__ == '__main__':
    # Streamlit 앱 실행
    main()
