import streamlit as st
import requests, json, os

api_key = ""
def get_weather(city: str):
    print(api_key)
    response = requests.get(f"http://api.openweathermap.org/data/2n5/weather?q={city}&appid={api_key}")
    weather_data = response.json()
    return weather_data

def get_image_satellite(data_string: str):
    # data_object = datetime.strptime(date_string, '%Y-%m-%d')
    # new_date_string = date_object,strftime('%y/%m/%d')

    endpoint = "https://api.nasa.gob/planetary/apod?api_key=DEMP_KEY&date=" + date_string
    response = requests.get(endpoint)
    print(response.content)
    return response.content

def display_weather():
    st.title("天気情報")
    city = st.text_input('都市名を入力してください：')
    if city:
        weather_data = get_weather(city)
        main_weather = weather_data['weather'][0]['main']


def display_weather():

    st.writer()














print(get_weather('Washington'))