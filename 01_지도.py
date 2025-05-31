import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 데이터
travel_destinations = [
    {"name": "Maui, Hawaii", "lat": 20.7984, "lon": -156.3319, "desc": "열대 파라다이스, 서핑과 휴양의 천국"},
    {"name": "New York City, NY", "lat": 40.7128, "lon": -74.0060, "desc": "브로드웨이, 센트럴파크, 도시의 에너지"},
    {"name": "Las Vegas, NV", "lat": 36.1699, "lon": -115.1398, "desc": "불야성 카지노와 엔터테인먼트의 중심"},
    {"name": "Orlando, FL", "lat": 28.5383, "lon": -81.3792, "desc": "디즈니월드와 유니버설의 모험 도시"},
    {"name": "San Francisco, CA", "lat": 37.7749, "lon": -122.4194, "desc": "금문교와 자유로운 분위기의 도시"},
    {"name": "Honolulu, Hawaii", "lat": 21.3069, "lon": -157.8583, "desc": "와이키키 해변과 하와이 문화의 중심"},
    {"name": "Chicago, IL", "lat": 41.8781, "lon": -87.6298, "desc": "건축, 재즈, 호숫가 도시의 매력"},
    {"name": "Washington, D.C.", "lat": 38.9072, "lon": -77.0369, "desc": "미국의 역사와 박물관의 보고"},
    {"name": "Los Angeles, CA", "lat": 34.0522, "lon": -118.2437, "desc": "할리우드, 해변, 다문화의 만남"},
    {"name": "New Orleans, LA", "lat": 29.9511, "lon": -90.0715, "desc": "재즈와 크레올 문화의 향연"},
]

# Streamlit 타이틀
st.set_page_config(page_title="미국 여행지 Top 10", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: #006666;'>🌴 미국인들이 사랑하는 Top 10 여행지 🌴</h1>",
    unsafe_allow_html=True,
)

# 폴리움 지도 생성
m = folium.Map(location=[39.5, -98.35], zoom_start=4, tiles='CartoDB positron')

# 마커 추가
for place in travel_destinations:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(color="green", icon="cloud"),
    ).add_to(m)

# 지도 출력
st_folium(m, width=1000, height=600)

# 이국적인 설명 박스
st.markdown("---")
st.markdown("### ✈️ 당신의 다음 여행지는 어디인가요?")
for i, place in enumerate(travel_destinations, 1):
    st.markdown(
        f"**{i}. {place['name']}**  
        _{place['desc']}_\n"
    )
