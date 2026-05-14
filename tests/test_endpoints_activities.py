def test_get_activities_returns_all_expected_fields(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in payload
    assert "description" in payload["Chess Club"]
    assert "participants" in payload["Chess Club"]


def test_get_activities_starts_with_empty_participants(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for details in payload.values():
        assert details["participants"] == []
