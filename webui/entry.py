import streamlit as st
from st_pages import Page, show_pages, hide_pages

from constants import *

st.set_page_config(
    layout="wide",
)

show_pages(
    [
        Page(PAGE_MAIN, "Главная", "🏠"),
        Page(PAGE_EXISTING_TRIPS, "Найти собеседника", "🙏"),
        Page(PAGE_CREATE_NEW_TRIP, "Создать поездку", "🌏"),
        Page(PAGE_SPECIFIC_TRIP, "Просмотр заявки", "📃"),
    ]
)
hide_pages(["Просмотр заявки"])

title_alignment="""
<style>
#the-title {
  text-align: center
}
</style>
"""
st.title(APP_NAME)
st.header(APP_SLOGAN)
st.markdown("Добро пожаловать в мир новых знакомств и незабываемых приключений! "
            "Наша платформа предназначена для тех, кто любит путешествовать и ищет новых друзей на своем пути. "
            "Мы знаем, как трудно найти единомышленников в большом мире, поэтому создали приложение, которое поможет вам встретить интересных людей, "
            "готовых поделиться своими историями и открыть новые горизонты.")
# st.image("PeopleTalkingInTrain.webp")
#
# st.markdown(
#     """
# <style>
# button[kind="primary"] {
#     height: auto;
#     width: auto;
#     padding-top: 10px !important;
#     padding-bottom: 10px !important;
#     background-color: red;
# }
# </style>
# """,
#     unsafe_allow_html=True,
# )
#
# st.markdown(f'<p class="params_text">CHART DATA PARAMETERS', unsafe_allow_html = True)
# st.markdown("""<div background-color="red" class="mydiv"> HELLO! </div>""", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # if st.button(label="Создать поездку", type="primary"):
        if st.button(label="Создать поездку"):
            st.switch_page(PAGE_CREATE_NEW_TRIP)
    with col2:
        # if st.button(label="Найти собеседника", type="primary"):
        if st.button(label="Найти собеседника"):
            st.switch_page(PAGE_EXISTING_TRIPS)
