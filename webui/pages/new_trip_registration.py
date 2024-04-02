import streamlit as st

from webui.common import *
from webui.constants import *
from datetime import date

confirm_button_is_visible = False
st.title("Вы на шаг ближе к тому, чтобы найти себе приятного собеседника!")
st.header("Заполните, пожалуйста информацию о поездке:")

available_transport_types = get_available_transport_types()
chosen_transport = st.selectbox(
    "Транспорт",
    available_transport_types,
    index=None,
    placeholder="Выберите транспорт, на котором планируете добираться...",
    format_func=transport_type_get_readable_view
)

chosen_date = st.date_input(
    "Выберите дату отправления",
    value="today",
    min_value=date.today(),
)

available_path_types = get_available_path_types()
chosen_path_type = st.selectbox(
    "Тип маршрута",
    available_path_types,
    index=None,
    placeholder="Выберите вид маршрута, который хотите указать...",
    format_func=path_type_get_readable_view
)

def path_type_code_flow():
    code = st.text_input()

def path_type_from_to_flow():
    chosen_time = st.time_input(
        "Укажите время начала поездки",
        value=None
    )
    st.write("FROM_TO")


match chosen_path_type:
    case PathType.CODE:
        path_type_code_flow()
    case PathType.FROM_TO:
        path_type_from_to_flow()

if chosen_transport is not None:
    confirm_button_is_visible = True

st.divider()
if st.button("Создать поездку", disabled=not confirm_button_is_visible):
    st.switch_page(PAGE_MAIN)
