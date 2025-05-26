import requests

def send_location_to_server(lat, lon):
    try:
        response = requests.post("http://YOUR_FLASK_SERVER/loc", json={"lat": lat, "lon": lon})
        print("전송 완료:", response.status_code)
    except Exception as e:
        print("전송 실패:", e)
