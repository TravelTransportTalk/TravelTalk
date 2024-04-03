from datetime import date

import streamlit as st
from st_pages import hide_pages

from webui.constants import SPECIFIC_USER_ID_KEY_NAME
from webui.server_communication import *

st.set_page_config(
    layout="wide",
)

hide_pages(["Просмотр заявки"])

found_trips = None
st.title("Найди себе собеседника!")
st.divider()

chosen_transport_type = None
transport_type_col, date_col, code_col, time_col, from_point_col, to_point_col = st.columns(6)
with transport_type_col:
    available_transport_types = get_available_transport_types()
    chosen_transport_type = st.selectbox(
        "Транспорт",
        available_transport_types,
        index=None,
        placeholder="Выберите вид транспорта",
        format_func=transport_type_get_readable_view
    )
if chosen_transport_type is not None:
    chosen_transport_api_name = transport_type_get_api_view(chosen_transport_type)
    chosen_transport_uuid = get_transport_by_name(chosen_transport_api_name).id
    available_stations = get_stations_by_type(chosen_transport_type)
    available_stations_id_name_pairs = [StationIdNamePair(station.station_code, station.short_name) for station in available_stations]

    with date_col:
        chosen_date = st.date_input(
            "Выберите дату отправления",
            value="today",
            min_value=date.today(),
        )
    with code_col:
        chosen_code = st.text_input(
            "Номер рейса",
            placeholder="Введите номер рейса, на котором собираетесь добираться...",
            value=None
        )
    with time_col:
        chosen_time = st.time_input(
            "Укажите время начала поездки",
            value=None
        )
    with from_point_col:
        point_from = st.selectbox(
            "Пункт отправления",
            available_stations_id_name_pairs,
            index=None,
            placeholder="Выберите пункт отправления...",
            format_func=station_id_name_pair_get_readable_view
        )
    with to_point_col:
        point_to = st.selectbox(
            "Пункт прибытия",
            available_stations_id_name_pairs,
            index=None,
            placeholder="Выберите пункт прибытия...",
            format_func=station_id_name_pair_get_readable_view
        )

    find_transport_request = FindTripRequest()
    find_transport_request.transportId = chosen_transport_uuid
    if point_from is not None:
        find_transport_request.fromId = point_from.id
    if point_to is not None:
        find_transport_request.toId = point_to.id
    found_trip_response = find_trips(find_transport_request)
    found_trips = found_trip_response.trips
    if found_trips is not None:
        st.divider()
        with st.container():
            transport_type, date, author, code, from_point, to_point = st.columns(6)
            with transport_type:
                st.write("Вид транспорта")
            with date:
                st.write("Дата отправления")
            with author:
                st.write("Автор")
            with code:
                st.write("Номер рейса")
            with from_point:
                st.write("Точка отправления")
            with to_point:
                st.write("Точка прибытия")

            for trip in found_trips:
                with st.container(border=True):
                    tr_transport_type, tr_date, tr_author, tr_code, tr_from_point, tr_to_point = st.columns(6)
                    with tr_transport_type:
                        st.write(trip.transport.name)
                    with tr_date:
                        date_object = datetime.strptime(trip.date, "%Y-%m-%dT%H:%M:%S.%f%z")
                        st.write(date_object.strftime("%Y-%m-%d"))
                    with tr_author:
                        if st.button(trip.authorId.tgUsername):
                            st.session_state[SPECIFIC_USER_ID_KEY_NAME] = trip.authorId
                            st.switch_page("pages/specific_trip.py")
                    with tr_code:
                        if trip.code is None or len(trip.code) == 0:
                            st.write(None)
                        else:
                            st.write(trip.code)
                    with tr_from_point:
                        st.write(trip.from_location.short_name)
                    with tr_to_point:
                        st.write(trip.to_location.short_name)