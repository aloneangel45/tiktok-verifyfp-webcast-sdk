import requests
from typing import Dict, Any

class TikTokWebcastClient:
    """Enterprise client for TikTok Live Webcast telemetry & verifyFp signature generation."""
    
    def __init__(self, rapidapi_key: str, host: str = "tiktok-signature-verifyfp-live-webcast-api.p.rapidapi.com"):
        self.rapidapi_key = rapidapi_key
        self.host = host
        self.base_url = f"https://{host}/api/v1/tiktok"

    def get_webcast_live_session(self, room_id: str) -> Dict[str, Any]:
        """Generate verified room signatures and WebSocket connection telemetry for live room."""
        headers = {
            "x-rapidapi-host": self.host,
            "x-rapidapi-key": self.rapidapi_key,
            "Content-Type": "application/json"
        }
        body = { "room_id": room_id }
        response = requests.post(f"{self.base_url}/webcast-live", json=body, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
