import streamlit as st

from webui.constants import SPECIFIC_USER_ID_KEY_NAME

st.set_page_config(
    layout="wide",
)


st.title("Узнайте человека получше!")

if SPECIFIC_USER_ID_KEY_NAME in st.session_state:
    author = st.session_state[SPECIFIC_USER_ID_KEY_NAME]
    st.header(author.nick)
    st.write(f"ФИО: {author.fullName}")
    st.write(f"Описание: {author.description}")
    st.write(f"Ссылка на телеграм: https://t.me/{author.tgUsername}")

# TELEGRAM_SECRET_CODE_KEY_NAME = "trip_info"
# passed_params = st.query_params
# default_trip = None
# if TELEGRAM_SECRET_CODE_KEY_NAME in passed_params.keys():
#     default_secret_code = passed_params[TELEGRAM_SECRET_CODE_KEY_NAME]

