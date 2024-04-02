import streamlit as st

st.write("Регистрация новой поездки")

TELEGRAM_SECRET_CODE_KEY_NAME = "tg_secret_code"
passed_params = st.query_params
default_secret_code = None
if TELEGRAM_SECRET_CODE_KEY_NAME in passed_params.keys():
    default_secret_code = passed_params[TELEGRAM_SECRET_CODE_KEY_NAME]

telegram_secret_code = st.text_input(
    "Телеграм код",
    default_secret_code
)

if telegram_secret_code is not None and len(telegram_secret_code) != 0:
    st.write("Going further")