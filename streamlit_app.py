import streamlit as st
import requests

areacode = {"大阪": "270000", "東京": "130000", "千葉": "120000"}

st.title('天気予報アプリ')

with st.sidebar:
    st.header('天気予報アプリ')
    city = st.selectbox('地域', ('大阪', '東京', '千葉'))


url = "https://www.jma.go.jp/bosai/forecast/data/forecast/" + areacode[city] + ".json"

res = requests.get(url)

jsondata = res.json()

st.header("{}の天気予報".format(jsondata[0]['timeSeries'][0]['areas'][0]['area']['name']))
for i in range(3):
  st.subheader(jsondata[0]['timeSeries'][0]['timeDefines'][i][:10])
  st.write(jsondata[0]['timeSeries'][0]['areas'][0]['weathers'][i])
st.info("{}の最高気温は{}℃、最低気温は{}℃です".format(jsondata[0]['timeSeries'][2]['timeDefines'][0][:10], jsondata[0]['timeSeries'][2]['areas'][0]['temps'][1], jsondata[0]['timeSeries'][2]['areas'][0]['temps'][0]))

