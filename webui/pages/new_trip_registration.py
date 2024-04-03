from typing import Optional

import streamlit as st
from st_pages import hide_pages

from webui.constants import *
from datetime import date

from webui.server_communication import *

st.set_page_config(
    layout="wide",
)

hide_pages(["Просмотр заявки"])

trip = None
st.title("Вы на шаг ближе к тому, чтобы найти себе приятного собеседника!")

TELEGRAM_ID_KEY_NAME = "tgID"
passed_params = st.query_params
default_tgId = None
if TELEGRAM_ID_KEY_NAME in passed_params.keys():
    default_tgId = passed_params[TELEGRAM_ID_KEY_NAME]

st.header("Введите, пожалуйста, свой код из телеграма:")

telegram_id = st.text_input(
    "Телеграм код",
    default_tgId
)

user_uuid = None
if telegram_id is not None and len(telegram_id) != 0:
    user_resp = auth(telegram_id)
    if user_resp is not None:
        user_uuid = user_resp.user.id
    else:
        st.error("Пользователь с таким id не найден")
if user_uuid is not None:


    st.divider()
    st.header("Заполните, пожалуйста информацию о поездке:")

    available_transport_types = get_available_transport_types()
    chosen_transport_type = st.selectbox(
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

    if chosen_transport_type is not None and chosen_date is not None:
        chosen_transport_api_name = transport_type_get_api_view(chosen_transport_type)
        chosen_transport_uuid = get_transport_by_name(chosen_transport_api_name).id
        available_stations = get_stations_by_type(chosen_transport_type)
        available_stations_id_name_pairs = [StationIdNamePair(station.station_code, station.short_name) for station in available_stations]

        point_from = st.selectbox(
            "Пункт отправления",
            available_stations_id_name_pairs,
            index=None,
            placeholder="Выберите пункт отправления...",
            format_func=station_id_name_pair_get_readable_view
        )

        point_to = st.selectbox(
            "Пункт прибытия",
            available_stations_id_name_pairs,
            index=None,
            placeholder="Выберите пункт прибытия...",
            format_func=station_id_name_pair_get_readable_view
        )

        code = st.text_input(
            "Номер рейса",
            placeholder="Введите номер рейса, на котором собираетесь добираться...",
            help="Можете оставить это поле пустым, если не знаете номер рейса"
        )

        if code is None:
            # HACK: default value for code.
            code = ""

        chosen_time = st.time_input(
            "Укажите время начала поездки",
            value="now"
        )

        if point_from is not None and point_to is not None:
            trip = AddTripRequest(
                point_from.id,
                point_to.id,
                chosen_date.strftime("%d-%m-%Y"),
                chosen_time.strftime("%H:%M:%S+05:00"),
                code,
                chosen_transport_uuid,
                user_uuid
            )

        if trip is not None:
            print(trip.to_json())


st.divider()
if st.button("Создать поездку", disabled=trip is None):
    register_trip(trip)
    st.switch_page(PAGE_MAIN)
