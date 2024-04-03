from typing import Optional

import streamlit as st

from webui.constants import *
from datetime import date

from webui.server_communication import *

st.set_page_config(
    layout="wide",
)

trip = None
st.title("Вы на шаг ближе к тому, чтобы найти себе приятного собеседника!")

TELEGRAM_ID_KEY_NAME = "tgID"
passed_params = st.query_params
default_tgId = None
if TELEGRAM_ID_KEY_NAME in passed_params.keys():
    default_tgId = passed_params[TELEGRAM_ID_KEY_NAME]

st.header("Введите, пожалуйста, свой секретный код из телеграма:")

telegram_id = st.text_input(
    "Телеграм код",
    default_tgId
)

if telegram_id is not None and len(telegram_id) != 0:
    st.divider()
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


    def path_type_code_flow() -> Optional[str]:
        code = st.text_input(
            "Номер рейса",
            placeholder="Введите номер рейса, на котором собираетесь добираться..."
        )
        if code is not None and len(code) != 0:
            return code


    def path_type_from_to_flow():
        chosen_time = st.time_input(
            "Укажите время начала поездки",
            value=None
        )

        available_locations = get_available_locations()
        point_from = st.selectbox(
            "Пункт отправления",
            available_locations,
            index=None,
            placeholder="Выберите пункт отправления...",
        )

        point_to = st.selectbox(
            "Пункт прибытия",
            available_locations,
            index=None,
            placeholder="Выберите пункт прибытия...",
        )

        if chosen_time is not None and point_from is not None and point_to is not None:
            return chosen_time, point_from, point_to
        return None

    match chosen_path_type:
        case PathType.CODE:
            code = path_type_code_flow()
            if code is not None:
                trip = None
        case PathType.FROM_TO:
            from_to_info = path_type_from_to_flow()
            if from_to_info is not None:
                chosen_time, point_from, point_to = from_to_info
                trip = None
    if trip is not None:
        print(trip.to_json())


st.divider()
if st.button("Создать поездку", disabled=trip is not None):
    register_trip(trip)
    st.switch_page(PAGE_MAIN)
