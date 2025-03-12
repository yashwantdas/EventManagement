from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_event():
    response = client.post("/api/events/", json={
        "name": "Tech Conference",
        "description": "A conference on AI",
        "start_time": "2025-03-12T10:00:00",
        "end_time": "2025-03-12T18:00:00",
        "location": "NYC",
        "max_attendees": 100
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Tech Conference"
