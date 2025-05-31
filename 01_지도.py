import streamlit as st

# 여행지 데이터 (Top 10)
destinations = [
    {"name": "Maui, Hawaii", "lat": 20.7984, "lon": -156.3319, "desc": "🌺 파도와 야자수의 천국"},
    {"name": "New York City, NY", "lat": 40.7128, "lon": -74.0060, "desc": "🗽 잠들지 않는 도시"},
    {"name": "Las Vegas, NV", "lat": 36.1699, "lon": -115.1398, "desc": "🎰 카지노와 쇼의 천국"},
    {"name": "Orlando, FL", "lat": 28.5383, "lon": -81.3792, "desc": "🎢 테마파크의 제왕"},
    {"name": "San Francisco, CA", "lat": 37.7749, "lon": -122.4194, "desc": "🌉 안개 속 금문교"},
    {"name": "Honolulu, Hawaii", "lat": 21.3069, "lon": -157.8583, "desc": "🏖 와이키키 해변의 낭만"},
    {"name": "Chicago, IL", "lat": 41.8781, "lon": -87.6298, "desc": "🎷 시카고 블루스와 호수"},
    {"name": "Washington, D.C.", "lat": 38.9072, "lon": -77.0369, "desc": "🏛 미국의 수도, 역사"},
    {"name": "Los Angeles, CA", "lat": 34.0522, "lon": -118.2437, "desc": "🌴 할리우드와 해변"},
    {"name": "New Orleans, LA", "lat": 29.9511, "lon": -90.0715, "desc": "🎺 재즈와 마디그라의 도시"},
]

# 페이지 설정
st.set_page_config(page_title="Top 10 미국 여행지", layout="wide")

# 타이틀 영역
st.markdown("""
    <div style='text-align: center; padding: 1rem; background: linear-gradient(to right, #e0f7fa, #ffe0b2); border-radius: 12px;'>
        <h1 style='color: #00695c;'>🇺🇸 미국인이 사랑하는 여행지 Top 10</h1>
        <p style='font-size: 1.1rem;'>미국 전역의 이국적이고 매력적인 여행지를 만나보세요!</p>
    </div>
""", unsafe_allow_html=True)

# 지도 초기화
map_center = [39.5, -98.35]  # 미국 중심
m = folium.Map(location=map_center, zoom_start=4, tiles="CartoDB positron")

# 마커 추가
for place in destinations:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"]
    ).add_to(m)

# 지도 출력
st_folium(m, height=600, width=1000)

# 여행지 목록 소개
st.markdown("---")
st.subheader("🌎 여행지 소개")

for i, place in enumerate(destinations, 1):
    st.markdown(f"**{i}. {place['name']}** — {place['desc']}")
