import os
from flask import Flask, render_template, request, jsonify
from threading import Thread

data = {}
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("location.html")

@app.route('/send_location', methods=['POST'])
def receive_location():
    content = request.get_json()
    if content is None:
        return jsonify({"에러": "위치 정보가 없습니다"}), 400

    lat = content.get("latitude")
    lon = content.get("longitude")

    if lat and lon:
        data["location"] = {"lat": lat, "lon": lon}
        return jsonify({"message": "위치 저장 완료"}), 200
    else:
        return jsonify({"에러": "위도 또는 경도 누락"}), 400

@app.route('/delete_location', methods=['POST'])
def delete_location():
    data.pop("location", None)  # 위치 정보 제거
    return jsonify({"message": "위치 정보 삭제 완료"}), 200

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def run_forever():
    t = Thread(target=run)
    t.start()
