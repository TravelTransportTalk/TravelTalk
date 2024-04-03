from datetime import date
from uuid import uuid4

import streamlit as st

from webui.common import *
from webui.server_communication import find_trip

st.set_page_config(
    layout="wide",
)

user = User(uuid4(), "General_bum", "Эмир Вильданов", "Люблю болтать", "EmirVildanov")
print(user)
found_trips = None
st.title("Найди себе собеседника!")
st.divider()

transport_type_col, date_col, path_type_col, col_4, col_from_point, col_to_point = st.columns(6)
with transport_type_col:
    available_transport_types = get_available_transport_types()
    chosen_transport = st.selectbox(
        "Транспорт",
        available_transport_types,
        index=None,
        placeholder="Выберите вид транспорта",
        format_func=transport_type_get_readable_view
    )
with date_col:
    chosen_date = st.date_input(
        "Выберите дату отправления",
        value="today",
        min_value=date.today(),
    )
with path_type_col:
    available_path_types = get_available_path_types()
    chosen_path_type = st.selectbox(
        "Тип маршрута",
        available_path_types,
        index=None,
        placeholder="Выберите вид маршрута, который хотите указать...",
        format_func=path_type_get_readable_view
    )

    match chosen_path_type:
        case PathType.CODE:
            with col_4:
                code = st.text_input(
                    "Номер рейса",
                    placeholder="Введите номер рейса, на котором собираетесь добираться..."
                )

                if code is not None and len(code) != 0:
                    found_trips = find_trip(dict())
        case PathType.FROM_TO:
            with col_4:
                chosen_time = st.time_input(
                    "Укажите время начала поездки",
                    value=None
                )
            with col_from_point:
                available_locations = get_available_locations()
                point_from = st.selectbox(
                    "Пункт отправления",
                    available_locations,
                    index=None,
                    placeholder="Выберите пункт отправления...",
                )
            with col_to_point:
                point_to = st.selectbox(
                    "Пункт прибытия",
                    available_locations,
                    index=None,
                    placeholder="Выберите пункт прибытия...",
                )
            if chosen_time is not None and point_from is not None and point_to is not None:
                found_trips = find_trip(dict())

if found_trips is not None:
    st.divider()
    with st.container():
        col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
        with col_1:
            st.write("Вид транспорта")
        with col_2:
            st.write("Дата отправления")
        with col_3:
            st.write("Автор")
        with col_4:
            st.write("Номер рейса")
        with col_5:
            st.write("Точка отправления")
        with col_6:
            st.write("Точка прибытия")

        for trip in found_trips:
            with st.container(border=True):
                col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
                with col_1:
                    st.write(trip.transport_type)
                with col_2:
                    st.write(trip.date)
                with col_3:
                    # WORKAROUND: we have to give it a key because we use page switching below.
                    if st.button(trip.author.tg_username, key=uuid4()):
                        st.switch_page("specific_trip.py")
                with col_4:
                    st.write(trip.code)
                with col_5:
                    st.write(trip.from_location)
                with col_6:
                    st.write(trip.to_location)