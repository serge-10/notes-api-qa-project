import requests

BASE_URL = "https://practice.expandtesting.com/notes/api/notes"

def test_create_note_without_request_id():
    """Проверка: нельзя создать заметку без связи с заявкой"""
    payload = {
        "note": "Тестовая заметка без requestId"
    }

    response = requests.post(BASE_URL, json=payload)

    print(f"\nStatus: {response.status_code}")
    print(f"Body: {response.text}")

    assert response.status_code != 201, "Заметка была создана, хотя не указана заявка"
    assert response.status_code in (400, 422), f"Неверный код ответа: {response.status_code}"
