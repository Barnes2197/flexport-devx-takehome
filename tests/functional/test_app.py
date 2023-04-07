import json

from rock_paper_scissors.app import app


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors
    """

    with app.test_client() as test_client:
        for hand in ["Rock", "Paper", "Scissors"]:
            response = test_client.post(
                "/rps",
                data=json.dumps(dict(move=hand)),
                content_type="application/json",
            )
            assert response.status_code == 200

        response = test_client.post(
            "/rps",
            data=json.dumps(dict(move="Rocket")),
            content_type="application/json",
        )
        assert response.status_code == 500


def test_health_check():
    with app.test_client() as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
