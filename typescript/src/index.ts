export class TikTokWebcastClient {
  private rapidApiKey: string;
  private host: string;

  constructor(apiKey: string, host = "tiktok-signature-verifyfp-live-webcast-api.p.rapidapi.com") {
    this.rapidApiKey = apiKey;
    this.host = host;
  }

  async getWebcastLiveSession(roomId: string) {
    const res = await fetch(`https://${this.host}/api/v1/tiktok/webcast-live`, {
      method: "POST",
      headers: {
        "x-rapidapi-host": this.host,
        "x-rapidapi-key": this.rapidApiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ room_id: roomId })
    });

    if (!res.ok) {
      throw new Error(`TikTok API error: ${res.status} ${res.statusText}`);
    }
    return await res.json();
  }
}
