import requests
import json

def test_health_check_integration():
    response = requests.get("http://localhost:8080/health")
    assert response.status_code == 200

def test_rps_endpoint():
    for hand in ['Rock', 'Paper', 'Scissors']:
        url = "http://localhost:8080/rps"
        payload = json.dumps({
            "move": hand
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200
        game = json.loads(response.text)
        assert game['pc_choice'] in [0, 1, 2]
        assert game['game_result'] in [-1, 0, 1]
        assert game['result'] == 'Tie' or hand in game['result']
        