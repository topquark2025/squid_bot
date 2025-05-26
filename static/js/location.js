function getLocation() {
  if (!navigator.geolocation) {
    document.getElementById("status").textContent = "브라우저가 위치를 지원하지 않아요.";
    return;
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      document.getElementById("status").textContent = `위치: ${latitude}, ${longitude}`;

      // Flask 서버에 위치 정보 전송
      fetch("/send_location", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ latitude, longitude })
      })
      .then(response => response.json())
      .then(data => console.log("[클라이언트] 응답:", data))
      .catch(error => console.error("[클라이언트] 에러:", error));
    },
    () => {
      document.getElementById("status").textContent = "위치 접근이 거부되었어요.";
    }
  );
}
